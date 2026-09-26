"""Independent check of the two agent-produced portability instances."""
from __future__ import annotations

import csv
from decimal import Decimal
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def totals(sales: list[dict[str, str]], expenses: list[dict[str, str]]) -> dict[str, dict[str, Decimal]]:
    months: dict[str, dict[str, Decimal]] = {}
    for records, key in ((sales, 'ventas'), (expenses, 'gastos')):
        for row in records:
            month = row['fecha'][:7]
            bucket = months.setdefault(month, {'ventas': Decimal('0'), 'gastos': Decimal('0')})
            bucket[key] += Decimal(row['importe_eur'])
    for bucket in months.values():
        bucket['diferencia'] = bucket['ventas'] - bucket['gastos']
    return months


def normalized_report(path: Path) -> dict[str, dict[str, Decimal]]:
    raw = json.loads(path.read_text(encoding='utf-8'))
    return {month: {key: Decimal(str(value[key])) for key in ('ventas', 'gastos', 'diferencia')}
            for month, value in raw.items()}


def command(args: list[str], cwd: Path) -> tuple[int, str]:
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return result.returncode, (result.stdout + result.stderr).strip()


def verify(agent: str) -> dict:
    area = ROOT / agent
    instance = area / 'instance'
    errors: list[str] = []
    results: dict[str, int] = {}
    if not instance.is_dir():
        return {'agent': agent, 'errors': ['instance/ missing']}
    inputs = {name: area / 'inputs' / f'{name}.csv' for name in ('ventas', 'gastos')}
    originals = {name: instance / 'proyectos/entradas' / f'{name}.csv' for name in inputs}
    working = {name: instance / 'proyectos' / name / f'{name}.csv' for name in inputs}
    try:
        for name in inputs:
            if inputs[name].read_bytes() != originals[name].read_bytes():
                errors.append(f'{name}: original changed')
        base_sales, base_expenses = rows(inputs['ventas']), rows(inputs['gastos'])
        sales, expenses = rows(working['ventas']), rows(working['gastos'])
        added = {'id': 'V-004', 'fecha': '2026-01-25', 'importe_eur': '25.00'}
        if sales != [*base_sales, added]:
            errors.append('working sales do not equal original rows plus exactly one V-004')
        if expenses != base_expenses:
            errors.append('working expenses differ from original rows')
        initial = normalized_report(instance / 'reports/resumen-inicial.json')
        final_path = instance / 'proyectos/seguimiento/resumen.json'
        final = normalized_report(final_path)
        expected_initial = totals(base_sales, base_expenses)
        expected_final = totals(sales, expenses)
        if initial != expected_initial:
            errors.append('initial monthly report differs from independently calculated totals')
        if final != expected_final:
            errors.append('final monthly report differs from independently calculated totals')
        if (instance / 'proyectos/resumen').exists():
            errors.append('old resumen/ folder still exists')
        script = instance / 'proyectos/seguimiento/resumen.py'
        code, output = command([sys.executable, str(script)], instance)
        results['rerun_final_script'] = code
        if code != 0:
            errors.append(f'final script failed: {output[:300]}')
        elif normalized_report(final_path) != expected_final:
            errors.append('rerun final script changed totals incorrectly')
        for script_name in ('validate_workspace.py', 'validate_okf_nodes.py', 'check_first_run.py'):
            code, output = command([sys.executable, f'scripts/{script_name}'], instance)
            results[script_name] = code
            if code != 0:
                errors.append(f'{script_name} failed: {output[:300]}')
        if not (instance / 'reports/caso-portabilidad.json').is_file():
            errors.append('agent execution report missing')
        if not [p for p in (instance / 'skills').glob('*.md') if p.name not in {'index.md', 'primer-uso.md'}]:
            errors.append('custom reusable skill missing')
        if not [p for p in (instance / 'contracts').glob('*.md') if p.name not in {'index.md', 'primer-uso.md'}]:
            errors.append('custom task contract missing')
        return {'agent': agent, 'errors': errors, 'exit_codes': results,
                'expected_initial': {k: {n: str(v) for n, v in row.items()} for k, row in expected_initial.items()},
                'expected_final': {k: {n: str(v) for n, v in row.items()} for k, row in expected_final.items()}}
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        errors.append(f'cannot inspect output: {exc}')
        return {'agent': agent, 'errors': errors, 'exit_codes': results}


if __name__ == '__main__':
    reports = [verify(name) for name in ('codex', 'glm')]
    print(json.dumps(reports, ensure_ascii=False, indent=2))
    sys.exit(1 if any(report['errors'] for report in reports) else 0)

"""Oráculo independiente para el resumen mensual de ventas y gastos."""

import csv
import json
import sys
from collections import defaultdict
from datetime import date
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def totals(path):
    months = defaultdict(lambda: Decimal("0"))
    with path.open(newline="", encoding="utf-8-sig") as source:
        rows = csv.DictReader(source)
        if rows.fieldnames != ["id", "fecha", "importe_eur"]:
            raise ValueError(f"Cabecera inesperada: {path}")
        for row in rows:
            if set(row) != {"id", "fecha", "importe_eur"} or None in row.values():
                raise ValueError(f"Fila incompleta: {path}")
            month = date.fromisoformat(row["fecha"]).strftime("%Y-%m")
            months[month] += Decimal(row["importe_eur"])
    return months


def check():
    projects = ROOT / "proyectos"
    sales = totals(projects / "ventas" / "ventas.csv")
    expenses = totals(projects / "gastos" / "gastos.csv")
    expected = {
        month: {
            "ventas": sales[month],
            "gastos": expenses[month],
            "diferencia": sales[month] - expenses[month],
        }
        for month in sorted(sales.keys() | expenses.keys())
    }
    actual = json.loads(
        (projects / "seguimiento" / "resumen.json").read_text(encoding="utf-8"),
        parse_float=Decimal,
        parse_int=Decimal,
    )
    if actual != expected:
        raise AssertionError(f"El resumen no coincide con los CSV: {actual!r} != {expected!r}")
    print(f"Resumen comprobado contra CSV de trabajo: {len(expected)} meses")


if __name__ == "__main__":
    try:
        check()
    except (OSError, ValueError, AssertionError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

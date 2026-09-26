#!/usr/bin/env python3
"""Oráculo del contrato recalcular-resumen (independiente de resumen.py).

Recalcula los importes por mes desde los CSV de trabajo y los contrasta con
proyectos/seguimiento/resumen.json. Código 0 solo si coinciden.
Se ejecuta desde la raíz de la instancia.
"""
from __future__ import annotations
import csv
import json
import re
import sys
from decimal import Decimal
from pathlib import Path

VENTAS = Path('proyectos') / 'ventas' / 'ventas.csv'
GASTOS = Path('proyectos') / 'gastos' / 'gastos.csv'
RESUMEN = Path('proyectos') / 'seguimiento' / 'resumen.json'
CAMPOS = {'ventas', 'gastos', 'diferencia'}
MES = re.compile(r'\d{4}-\d{2}\Z')


def totales(ruta: Path) -> dict[str, Decimal]:
    if not ruta.is_file():
        raise FileNotFoundError(f'Falta {ruta}')
    acumulado: dict[str, Decimal] = {}
    with ruta.open(encoding='utf-8', newline='') as fichero:
        for fila in csv.DictReader(fichero):
            fecha = fila['fecha']
            if len(fecha) != 10 or fecha[4] != '-' or fecha[7] != '-':
                raise ValueError(f'{ruta}: fecha inválida: {fecha}')
            mes = fecha[:7]
            acumulado[mes] = acumulado.get(mes, Decimal('0')) + Decimal(fila['importe_eur'])
    return acumulado


def comprobar() -> None:
    ventas, gastos = totales(VENTAS), totales(GASTOS)
    esperado = {mes: (ventas.get(mes, Decimal('0')), gastos.get(mes, Decimal('0')))
                for mes in sorted(set(ventas) | set(gastos))}
    if not RESUMEN.is_file():
        raise FileNotFoundError(f'Falta {RESUMEN}')
    observado = json.loads(RESUMEN.read_text(encoding='utf-8'))
    if set(observado) != set(esperado):
        raise ValueError(f'Meses distintos: JSON {sorted(observado)} vs CSV {sorted(esperado)}')
    for mes, (v, g) in esperado.items():
        campo = observado[mes]
        if set(campo) != CAMPOS:
            raise ValueError(f'{mes}: campos inesperados o ausentes: {sorted(campo)}')
        for nombre, valor in (('ventas', v), ('gastos', g), ('diferencia', v - g)):
            observado_valor = campo[nombre]
            if not isinstance(observado_valor, (int, float)) or isinstance(observado_valor, bool):
                raise ValueError(f'{mes}.{nombre}: no es número: {observado_valor!r}')
            if Decimal(str(observado_valor)) != Decimal(str(round(float(valor), 2))):
                raise ValueError(f'{mes}.{nombre}: JSON {observado_valor} vs CSV {valor}')


def main() -> int:
    try:
        comprobar()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f'FAIL: {exc}')
        return 1
    print(f'OK: resumen coincide con los CSV de trabajo ({RESUMEN})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
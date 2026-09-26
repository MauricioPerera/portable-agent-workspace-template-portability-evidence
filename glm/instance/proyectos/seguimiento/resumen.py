#!/usr/bin/env python3
"""Agrupa ventas y gastos por mes y produce resumen.json.

Se ejecuta desde la raíz de la instancia:
    python proyectos/seguimiento/resumen.py

Entradas: proyectos/ventas/ventas.csv y proyectos/gastos/gastos.csv (id, fecha, importe_eur).
Salida: proyectos/seguimiento/resumen.json con claves AAAA-MM y valores
{ventas, gastos, diferencia} (ventas menos gastos).
"""
from __future__ import annotations
import csv
import json
from decimal import Decimal
from pathlib import Path

VENTAS = Path('proyectos') / 'ventas' / 'ventas.csv'
GASTOS = Path('proyectos') / 'gastos' / 'gastos.csv'
SALIDA = Path('proyectos') / 'seguimiento' / 'resumen.json'


def cargar(ruta: Path) -> dict[str, Decimal]:
    totales: dict[str, Decimal] = {}
    with ruta.open(encoding='utf-8', newline='') as fichero:
        for fila in csv.DictReader(fichero):
            mes = fila['fecha'][:7]
            totales[mes] = totales.get(mes, Decimal('0')) + Decimal(fila['importe_eur'])
    return totales


def construir(ventas: dict[str, Decimal], gastos: dict[str, Decimal]) -> dict:
    resumen = {}
    for mes in sorted(set(ventas) | set(gastos)):
        v, g = ventas.get(mes, Decimal('0')), gastos.get(mes, Decimal('0'))
        resumen[mes] = {
            'ventas': float(round(v, 2)),
            'gastos': float(round(g, 2)),
            'diferencia': float(round(v - g, 2)),
        }
    return resumen


def main() -> int:
    resumen = construir(cargar(VENTAS), cargar(GASTOS))
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(resumen, indent=2) + '\n', encoding='utf-8')
    print(f'OK: {SALIDA} ({len(resumen)} meses)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
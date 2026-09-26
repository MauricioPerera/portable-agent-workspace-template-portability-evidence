"""Calcula ventas, gastos y diferencia mensual desde la raíz de la instancia."""

import csv
import json
from collections import defaultdict
from datetime import date
from decimal import Decimal
from pathlib import Path


BASE = Path("proyectos")
SALIDA = BASE / "seguimiento" / "resumen.json"


def importes(path):
    totales = defaultdict(lambda: Decimal("0.00"))
    with path.open(newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != ["id", "fecha", "importe_eur"]:
            raise ValueError(f"Columnas inesperadas en {path}")
        for fila in lector:
            mes = date.fromisoformat(fila["fecha"][:10]).strftime("%Y-%m")
            totales[mes] += Decimal(fila["importe_eur"])
    return totales


def main():
    ventas = importes(BASE / "ventas" / "ventas.csv")
    gastos = importes(BASE / "gastos" / "gastos.csv")
    resumen = {}
    for mes in sorted(ventas.keys() | gastos.keys()):
        v, g = ventas[mes], gastos[mes]
        resumen[mes] = {
            "ventas": float(v),
            "gastos": float(g),
            "diferencia": float(v - g),
        }
    SALIDA.write_text(json.dumps(resumen, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Resumen escrito en {SALIDA}")


if __name__ == "__main__":
    main()

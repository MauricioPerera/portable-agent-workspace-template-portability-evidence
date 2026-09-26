---
type: 'Task Contract'
name: 'recalcular-resumen'
version: '1.0.0'
inputs: 'proyectos/ventas/ventas.csv y proyectos/gastos/gastos.csv (copia de trabajo, columnas id, fecha, importe_eur).'
outputs: 'proyectos/seguimiento/resumen.json: meses AAAA-MM con ventas, gastos y diferencia (ventas menos gastos).'
scope: 'Recalculo local desde la raíz de la instancia; no modifica los CSV ni las copias de proyectos/entradas/.'
test_command: 'python scripts/comprobar_resumen.py'
---

# Contrato: Recalcular resumen mensual

## Entrada

Los CSV de trabajo `proyectos/ventas/ventas.csv` y `proyectos/gastos/gastos.csv` con cabecera `id,fecha,importe_eur`. Ejecutar desde la raíz de la instancia: `python proyectos/seguimiento/resumen.py`.

## Salida

`proyectos/seguimiento/resumen.json`: objeto cuyas claves son meses `AAAA-MM` y cuyos valores contienen los números `ventas`, `gastos` y `diferencia`, con `diferencia = ventas - gastos`.

## Perímetro

El cálculo solo usa los importes presentes en los CSV de trabajo; no se inventan meses ni valores. Las copias en `proyectos/entradas/` se conservan sin cambios.

## Aceptación

`test_command` debe recomputar de forma independiente (oráculo propio, sin importar `resumen.py`) los totales por mes desde los CSV de trabajo y contrastarlos con el JSON final: mismo conjunto de meses, mismos importes por campo y coherencia aritmética. Devuelve código 0 solo si coinciden; cualquier desviación falla.
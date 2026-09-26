---
type: "Task Contract"
title: "Contrato de resumen mensual"
name: "resumen-mensual"
version: "1.0.0"
inputs: "CSV de trabajo en proyectos/ventas/ventas.csv y proyectos/gastos/gastos.csv."
outputs: "JSON mensual en proyectos/seguimiento/resumen.json."
scope: "Cálculo local en EUR; no modifica originales en proyectos/entradas/."
test_command: "python scripts/check_resumen.py"
---

# Aceptación

El oráculo lee ambos CSV de trabajo, agrupa los importes por mes con `Decimal` y compara las claves y los tres valores numéricos de cada mes con el JSON final. La prueba devuelve código 0 solo si coinciden.

---
type: "Skill"
title: "Resumen mensual de ventas y gastos"
name: "resumen-mensual"
version: "1.0.0"
contract: "../contracts/resumen-mensual.md"
test_command: "python scripts/check_resumen.py"
---

# Recalcular el resumen

1. Conserva los CSV originales en `proyectos/entradas/` y trabaja con `proyectos/ventas/ventas.csv` y `proyectos/gastos/gastos.csv`.
2. Desde la raíz de la instancia, ejecuta `python proyectos/seguimiento/resumen.py`.
3. Comprueba `proyectos/seguimiento/resumen.json` con `python scripts/check_resumen.py`.
4. Registra los comandos y códigos de salida en `reports/`.

El [contrato](../contracts/resumen-mensual.md) define el criterio de aceptación.

---
type: 'Skill'
name: 'recalcular-resumen'
version: '1.0.0'
contract: '../contracts/recalcular-resumen.md'
test_command: 'python scripts/comprobar_resumen.py'
---

# Recalcular el resumen mensual

1. Leer el [contrato](../contracts/recalcular-resumen.md) y comprobar que existen `proyectos/ventas/ventas.csv` y `proyectos/gastos/gastos.csv`.
2. Ejecutar desde la raíz de la instancia: `python proyectos/seguimiento/resumen.py`.
3. Verificar el resultado con el oráculo del contrato: `python scripts/comprobar_resumen.py` (debe devolver código 0).
4. Revisar `proyectos/seguimiento/resumen.json`; no editar el JSON a mano. Si el oráculo falla, corregir los CSV o el script y recalcular.
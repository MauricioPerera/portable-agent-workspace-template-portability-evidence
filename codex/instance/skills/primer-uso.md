---
type: "Skill"
title: "Primer uso"
name: "primer-uso"
version: "1.0.0"
contract: "../contracts/primer-uso.md"
test_command: "python scripts/check_first_run.py"
---

# Inventariar el workspace

1. Leer la [constitución](../AGENTS.md), los índices y el [contrato](../contracts/primer-uso.md).
2. Ejecutar `python scripts/first_run.py` desde la raíz. Produce inventario y evidencia; ejecuta su oráculo antes de declarar éxito.
3. Revisar `proyectos/primer-uso/inventario.json` y `reports/primer-uso.json`.
4. Ejecutar `python scripts/check_first_run.py` para comprobar el estado guardado sin regenerarlo.
5. Solicitar la primera tarea y las fuentes que realmente necesite. No hay políticas ni datos de negocio incluidos.

---
type: "Workspace Guide"
title: "Portability Trial 042"
---

# Tu workspace está preparado

Abre esta carpeta con tu IA y dile: «Lee AGENTS.md y ayúdame con mi primera tarea».
La inicialización ejecutó el procedimiento de [primer uso](skills/primer-uso.md).

- Inventario en `proyectos/primer-uso/inventario.json`: fuentes y capacidades disponibles.
- Evidencia en `reports/primer-uso.json`: entradas, resultado y duración observada.
- [Conocimiento](context/index.md), [contratos](contracts/index.md) y [memoria](memoria/preferencias_consolidadas.md).

Desde esta carpeta puedes repetir el diagnóstico con `python scripts/first_run.py`.
Comprueba la estructura con `python scripts/validate_workspace.py` y el último resultado con `python scripts/check_first_run.py`.
Si cambia un archivo registrado en la evidencia, repite primer uso. No ejecutes aquí el validador del repositorio distribuidor.

Para actualizar: genera una instancia nueva en otra carpeta, compara reglas y scripts y migra los cambios conservando tus insumos y preferencias. Nunca ejecutes el inicializador sobre esta carpeta ya poblada.

# Caso de portabilidad: ventas y gastos

Trabaja solo dentro de esta carpeta de prueba. La distribución está en `distribution/`, los CSV recibidos en `inputs/` y tu instancia debe crearse en `instance/`. No modifiques `distribution/` ni los CSV de `inputs/`. Usa únicamente los archivos del workspace y Python estándar; no necesitas red.

1. Lee las reglas e índices pertinentes de `distribution/`. Ejecuta su generador para crear `instance/` y comprueba el primer uso.
2. Conserva copias byte a byte de `inputs/ventas.csv` y `inputs/gastos.csv` en `instance/proyectos/entradas/`. Crea copias de trabajo en `instance/proyectos/ventas/ventas.csv` y `instance/proyectos/gastos/gastos.csv`.
3. Crea `instance/proyectos/resumen/resumen.py` para agrupar los importes por mes a partir de ambos CSV y producir `resumen.json` con este formato: un objeto cuyas claves son meses `AAAA-MM` y cuyos valores tienen números `ventas`, `gastos` y `diferencia` (ventas menos gastos). Ejecuta el cálculo inicial y guarda una copia del JSON inicial en `instance/reports/resumen-inicial.json`.
4. Añade una sola venta de 25.00 EUR con id `V-004` y fecha `2026-01-25` a la copia de trabajo de ventas. Mueve el script y su resultado al proyecto `instance/proyectos/seguimiento/`, elimina la carpeta antigua `proyectos/resumen/`, ajusta las rutas y recalcula. El resultado final debe ser `instance/proyectos/seguimiento/resumen.json`; el script debe funcionar desde la raíz de la instancia después del traslado.
5. Añade una skill y un contrato para recalcular y comprobar el resumen, actualiza sus índices y ejecuta el `test_command` del contrato. El test debe contrastar el JSON final con los CSV de trabajo, no limitarse a ejecutar el script. Ejecuta los validadores de la instancia y vuelve a ejecutar primer uso para que la evidencia refleje la nueva skill.
6. Guarda en `instance/reports/caso-portabilidad.json` los comandos y códigos de salida relevantes, la ubicación final del resumen y una descripción breve de lo hecho. Termina con un resumen de los resultados observados.

No se proporcionan cifras esperadas: calcula los importes desde los CSV. Los datos son ficticios y sirven para comparar dos agentes con la misma petición.

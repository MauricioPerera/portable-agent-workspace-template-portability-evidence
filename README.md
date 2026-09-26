# Evidencia reproducible de portabilidad 0.4.2

Este repositorio conserva el caso ficticio descrito en el [informe de portabilidad](https://github.com/MauricioPerera/portable-agent-workspace-template/blob/main/reports/portability-0.4.2.md). Se mantuvo separado del distribuidor para que sus datos y las instancias de prueba no entren en el contexto inicial de una plantilla nueva.

## Contenido

- `shared/`: brief y dos CSV originales. Los mismos bytes se entregaron a Codex y GLM.
- `codex/` y `glm/`: copias del brief, los CSV entregados y las instancias resultantes. Se excluyeron las distribuciones duplicadas y las cachés Python; los archivos de trabajo, contratos, scripts, informes y evidencia de primer uso se conservan.
- `verify_results.py`: verificador externo a las instancias, que calcula con `Decimal` los totales desde los CSV, comprueba los originales preservados, la venta añadida, el traslado del resumen y los validadores de cada instancia.
- `verification.json`: salida guardada del verificador sobre estas copias.

## Comprobar la evidencia publicada

Se necesita Python 3.10 o posterior. Desde la raíz:

```sh
python verify_results.py
```

El comando devuelve 0 solo si las dos instancias pasan. Las entradas originales tienen SHA-256:

| Archivo | SHA-256 |
| --- | --- |
| `shared/brief.md` | `07550b07f915e03ad122ffa46ea474c60f31880490c07e95eb257956531019ac` |
| `shared/ventas.csv` | `9f37384d259484f9aa887607a024ed3db357c1e177006c24076da1782a21375d` |
| `shared/gastos.csv` | `0681f96ce4425fdbb0ad9f90683167a235208b68c920436f9c1c4efe6a4cecb7` |

## Repetir el experimento con otros agentes

1. Descarga la [distribución 0.4.2](https://github.com/MauricioPerera/portable-agent-workspace-template/releases/tag/v0.4.2) y comprueba el ZIP con su archivo `.sha256`.
2. Crea dos carpetas aisladas. En cada una coloca la distribución en `distribution/`, una copia de `shared/brief.md` como `brief.md` y copias de ambos CSV en `inputs/`.
3. Entrega el mismo `brief.md` a cada agente. Registra el modelo, entorno, comandos, códigos de salida y cualquier intervención humana. No modifiques el brief ni las entradas entre ejecuciones.
4. Coloca las dos carpetas resultantes como `codex/` y `glm/` en una copia de este repositorio y ejecuta `python verify_results.py`.

El verificador puede comprobar los archivos y resultados guardados. Los identificadores de modelo y las acciones de los agentes proceden del informe original y de sus reportes; estos archivos no contienen una transcripción completa ni demuestran por sí solos qué modelo produjo cada cambio. El caso usa datos ficticios y no prueba portabilidad universal.

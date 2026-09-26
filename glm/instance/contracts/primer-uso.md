---
type: "Task Contract"
title: "Contrato de primer uso"
name: "primer-uso"
version: "1.0.0"
inputs: "Manifiesto, reglas, índices y archivos actuales."
outputs: "Inventario JSON y evidencia con hashes y duración."
scope: "Diagnóstico local; no modifica insumos ni inventa conocimiento de dominio."
test_command: "python scripts/check_first_run.py"
---

# Aceptación

El inventario debe coincidir con la identidad del manifiesto y los archivos de fuentes y skills actuales. La evidencia identifica contrato, comando, duración e inputs; sus hashes deben coincidir con entradas y resultado. Un resultado modificado o evidencia ausente debe fallar.

Los hashes detectan cambios respecto del registro, no certifican autenticidad frente a alguien que altere código y evidencia. No se evalúa la veracidad de futuras fuentes ni se ejecutan contratos externos.

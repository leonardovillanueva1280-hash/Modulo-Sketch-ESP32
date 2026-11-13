# Informe de avance — Módulo Sketch ESP32 (Backend ESP-IDF)

**Elaboró:** Salvador García Vázquez — Presupuesto y depuración
**Fecha:** 11/11/2026
**Materia:** Fundamentos de Comunicaciones — Universidad de Guadalajara, CUCEI

## 1. Objetivo del módulo

Migrar el backend de compilación del módulo Sketch, parte de una IDE para placas ESP32, a ESP-IDF. El backend recibe la ruta de un proyecto ESP-IDF, compila, identifica los archivos `.bin` y devuelve un resultado JSON para los demás módulos (Editor/Compilador y Log).

## 2. Estado actual

Según la matriz de pruebas del repositorio (`docs/05_matriz_pruebas.md`):

| Estado | Pruebas |
|---|---|
| Completadas (7 de 13) | P-01 Python, P-02 ESP-IDF v6.1, P-03 objetivo `esp32`, P-04 compilación de `hello_idf`, P-05 identificación de `.bin`, P-06 ruta inexistente, P-07 proyecto sin `CMakeLists.txt` |
| Pendientes (6 de 13) | P-08 detección de puertos, P-09 carga a placa, P-10 proyecto con biblioteca, P-11 integración con Sketch, P-12 otros objetivos, P-13 exportación de artefactos |

Resultado registrado de la compilación de `hello_idf`: `success: true`, `returncode: 0`, artefactos `hello_idf.bin`, `bootloader.bin` y `partition-table.bin`.

**Alcance:** lo completado valida el backend con un proyecto de ejemplo. No demuestra la integración con la interfaz, la detección de puertos ni la carga en una placa física.

## 3. Trabajo de depuración realizado

Se revisó todo el repositorio y se documentaron 12 hallazgos en `docs/07_depuracion.md`:

- **7 corregidos en el código** (`src/esp_idf_backend.py`): D-01 a D-07.
- **5 pendientes** de documentación, evidencia o decisión del equipo: D-08 a D-12.

Mejoras principales del backend:

1. Evita repetir `set-target` (que fuerza una compilación completa) cuando el objetivo ya está configurado.
2. Identifica los artefactos con `flasher_args.json`, con su dirección de carga, información necesaria para la futura carga a la placa.
3. Cierra todos los procesos hijos cuando se agota el tiempo máximo.
4. Devuelve un resumen corto en `error`; el log completo sigue en `stdout` y `stderr`.
5. Valida el objetivo, ejecuta `idf.py` con Python y evita errores de codificación en Windows.
6. Agrega `--json-out` para guardar el resultado como evidencia.

El contrato de integración conserva todos sus campos; solo se añadieron `flash_files`, `app_bin` y `notes`, y el campo `error` ahora es un resumen.

## 4. Pruebas de la depuración

Se creó `tests/test_esp_idf_backend.py` con 12 pruebas sobre un `idf.py` simulado (validaciones, objetivo, artefactos, fallos, tiempo máximo). **Resultado: 12 de 12 correctas.** Una de ellas se comprobó contra el comportamiento anterior y falla, como debe.

**Límite:** son pruebas de lógica con una simulación. No reemplazan la compilación real con ESP-IDF; las correcciones se consideran validadas solo después de repetir P-04 en el equipo con ESP-IDF.

## 5. Evidencia y documentación pendientes

- La captura de `evidence/` corresponde a Arduino CLI, y los JSON de P-03 a P-07 no están guardados (D-08).
- Faltan `examples/` y hay referencias rotas y textos contradictorios (D-09, D-12).
- La bitácora `06_bitacora.md` necesita corregir el formato (D-10).

## 6. Presupuesto

El presupuesto de hardware **no puede cerrarse** hasta confirmar el modelo exacto de la placa, que el repositorio deja pendiente (`docs/03_dependencias_placas.md`). Para P-09 se necesitará como mínimo la placa, un cable USB de datos y, según el modelo, el driver USB-serial.

Un informe de presupuesto y de la placa se elaborará cuando se confirme el modelo.

## 7. Riesgos

- Las correcciones del backend no se han probado con ESP-IDF real.
- Sin evidencia verificable, las pruebas P-03 a P-07 no se sostienen ante una revisión.
- Sin definir el contrato con Editor, IDE principal y Log (`docs/04`, sección 7), la integración (P-11) no puede avanzar.
- Sin confirmar el modelo de placa no se puede probar la carga ni cerrar el presupuesto.

## 8. Próximos pasos

1. Reemplazar `src/esp_idf_backend.py`, agregar `tests/` y `docs/07_depuracion.md`, y repetir P-04 con ESP-IDF real usando `--json-out`.
2. Guardar la evidencia de P-03 a P-07 en `evidence/`.
3. Corregir las referencias rotas y subir `examples/hello_idf/` completo.
4. Confirmar el modelo de la placa y elaborar el informe de presupuesto.
5. Acordar con Editor, IDE principal y Log el contrato pendiente.

# Bitácora de depuración — Módulo Sketch (ESP-IDF)

**Responsable:** Salvador García Vázquez (Presupuesto y depuración)
**Fecha de revisión:** 11/11/2026
**Alcance revisado:** `src/esp_idf_backend.py`, `src/arduino_backend.py`, `README.md`, `README_ESP.md`, `docs/01` a `docs/06`, `docs/_ESP_IDF.md` y `evidence/`.

## Método

1. Lectura completa del código y de la documentación del repositorio.
2. Comparación entre lo que afirma la documentación y lo que contiene el repositorio.
3. Corrección del backend y prueba de la lógica con un `idf.py` **simulado** (`tests/test_esp_idf_backend.py`, 12 pruebas, todas correctas).

> **Limitación:** la revisión se hizo sin ESP-IDF instalado. Las correcciones del código están verificadas contra un `idf.py` simulado, **no** contra una compilación real. Antes de marcarlas como validadas hay que repetir P-04 en el equipo con ESP-IDF y guardar la evidencia (ver D-08).

## Resumen

| ID | Componente | Problema | Estado |
|---|---|---|---|
| D-01 | Backend | `set-target` se ejecutaba en cada compilación | Corregido (probado con simulación) |
| D-02 | Backend | Los `.bin` se buscaban por extensión | Corregido (probado con simulación) |
| D-03 | Backend | El tiempo máximo no cerraba los procesos hijos | Corregido (probado con simulación) |
| D-04 | Backend | El campo `error` contenía el log completo | Corregido (probado con simulación) |
| D-05 | Backend | `idf.py` se ejecutaba directamente | Mejorado (pendiente de probar en Windows) |
| D-06 | Backend | Posible error de codificación al imprimir el JSON | Mejorado (preventivo, no reproducido) |
| D-07 | Backend | El objetivo (`--target`) no se validaba | Corregido (probado con simulación) |
| D-08 | Evidencia | La evidencia no corresponde a las pruebas declaradas | **Pendiente** |
| D-09 | Documentación | Referencias a archivos inexistentes y textos contradictorios | **Pendiente** |
| D-10 | Documentación | `06_bitacora.md` muestra caracteres de escape | **Pendiente** |
| D-11 | Repositorio | `arduino_backend.py` sigue en `src/` | **Pendiente (decisión del equipo)** |
| D-12 | Evidencia | `evidence/` no contiene un proyecto compilable | **Pendiente** |

## Detalle

### D-01 — `set-target` en cada compilación
- **Descripción:** si se pasaba `--target`, el backend ejecutaba siempre `idf.py set-target`.
- **Causa:** `set-target` borra la carpeta `build` y reconfigura el proyecto, así que cada compilación era completa y lenta.
- **Solución:** `objetivo_configurado()` lee `CONFIG_IDF_TARGET` de `sdkconfig`. Si ya coincide con el objetivo pedido, se omite `set-target` y se deja una nota en `notes`. Si el objetivo cambia, se ejecuta.
- **Prueba:** `test_set_target_solo_cuando_hace_falta`.

### D-02 — Identificación de artefactos
- **Descripción:** `bin_files` se obtenía con `build.rglob("*.bin")`, que puede incluir archivos que no se graban en la placa.
- **Causa:** búsqueda solo por extensión.
- **Solución:** `leer_artefactos()` usa `build/flasher_args.json`, que lista los archivos exactos y su dirección. Se agregan los campos opcionales `flash_files` (offset y ruta) y `app_bin`. Si el JSON no existe, se usa la búsqueda anterior (sin `CMakeFiles`) y se avisa en `notes`. Los nombres de campos del contrato no cambian.
- **Prueba:** `test_build_ok_artefactos`, `test_build_ok_sin_flasher_args_usa_respaldo`. Con esto P-05 queda mejor soportada y se prepara P-09 (carga).

### D-03 — Tiempo máximo y procesos hijos
- **Descripción:** al agotarse `--timeout`, `subprocess.run` terminaba solo el proceso principal.
- **Causa:** `idf.py` lanza `cmake`, `ninja` y compiladores; en Windows pueden quedar ejecutándose.
- **Solución:** `ejecutar()` usa `Popen` en un grupo de procesos y `terminar_arbol()` cierra todo el árbol (`taskkill /T /F` en Windows, `killpg` en Linux/macOS).
- **Prueba:** `test_timeout_termina_proceso_y_hijos` (se comprobó que falla con el comportamiento anterior).

### D-04 — Campo `error` demasiado largo
- **Descripción:** ante una falla, `error` contenía todo el log de compilación.
- **Causa:** se copiaba `stderr` o `stdout` completos.
- **Solución:** `resumir_error()` conserva las últimas 15 líneas relevantes (máximo 2000 caracteres). El log completo sigue en `stdout` y `stderr`. **Cambio de comportamiento:** el módulo Log debe leer `error` como resumen.
- **Prueba:** `test_fallo_no_informa_bin_antiguos`, `test_resumir_error_limita_tamano`.

### D-05 — Invocación de `idf.py`
- **Descripción:** se ejecutaba la ruta de `idf.py` directamente.
- **Causa:** en Windows, ejecutar un `.py` sin intérprete puede fallar (WinError 193) según la asociación de archivos. En el equipo del autor funcionó.
- **Solución:** `construir_comando()` ejecuta `python idf.py ...` cuando la ruta termina en `.py`. Además, si `idf.py` no está en `PATH`, se busca en `IDF_PATH/tools/`.
- **Pendiente:** confirmarlo en Windows con ESP-IDF real.

### D-06 — Codificación de la salida
- **Descripción:** imprimir un log con caracteres especiales en una consola de Windows con codificación distinta de UTF-8 puede provocar `UnicodeEncodeError`.
- **Solución:** se reconfigura `stdout` a UTF-8 al iniciar. No se reprodujo el fallo; es una medida preventiva.

### D-07 — Validación del objetivo
- **Descripción:** `--target` se pasaba a `idf.py` sin revisar.
- **Causa:** un valor que empiece con `-` se interpretaría como opción de `idf.py`.
- **Solución:** se acepta solo `^[a-z0-9][a-z0-9_-]*$` (por ejemplo `esp32`, `esp32s3`). Otro valor devuelve error sin ejecutar nada.
- **Prueba:** `test_target_invalido`.

### D-08 — La evidencia no corresponde a lo declarado
- **Descripción:** `evidence/compilacion_esp32_2026-10-22.png` muestra **Arduino CLI** (`arduino-cli_1.5.2`, `PruebaESP32.ino`), no ESP-IDF con `hello_idf`. La matriz de pruebas marca P-03 a P-07 como completadas con "Resultado JSON", pero ese JSON no está en el repositorio.
- **Causa:** la evidencia de la prueba con ESP-IDF no se guardó.
- **Acción propuesta:** en el equipo con ESP-IDF, ejecutar
  `python src\esp_idf_backend.py C:\ruta\hello_idf --target esp32 --json-out evidence\hello_idf_resultado.json`
  y agregar una captura de la terminal. Para P-06 y P-07 se puede repetir con una ruta inexistente y con una carpeta sin `CMakeLists.txt`, guardando cada resultado.
- **Estado:** pendiente; requiere ejecutarse en el equipo del responsable de Sketch.

### D-09 — Referencias rotas y textos contradictorios
- `README.md` menciona la carpeta `examples/`, que no existe en el repositorio.
- `README_ESP.md` apunta a `examples/hello_idf/` y a `docs/MIGRACION_ESP_IDF.md`; el archivo real es `docs/_ESP_IDF.md`.
- `README_ESP.md` y `docs/_ESP_IDF.md` dicen que no hay validación, lo que contradice al README principal.
- **Acción propuesta:** subir `examples/hello_idf/` completo, corregir las rutas y actualizar o eliminar `README_ESP.md`.

### D-10 — Formato de `06_bitacora.md`
- **Descripción:** el archivo tiene caracteres de escape (`\###`, `\*\*`) y se ve como texto crudo en GitHub.
- **Acción propuesta:** quitar las barras invertidas. Además, esa entrada describe una prueba con Arduino CLI; conviene indicarlo o agregar una entrada nueva para la prueba con ESP-IDF.

### D-11 — `arduino_backend.py`
- **Descripción:** el objetivo del módulo es no depender de Arduino CLI, pero el archivo sigue en `src/`.
- **Acción propuesta:** el equipo decide si se elimina o se marca como obsoleto. Su función `list-ports` podría servir de referencia para P-08 (detección de puertos).

### D-12 — `evidence/` no es un proyecto compilable
- **Descripción:** `evidence/main.c` y `evidence/CMakeLists.txt` están en la misma carpeta; ESP-IDF espera `main/main.c` y `main/CMakeLists.txt` (con `idf_component_register`).
- **Acción propuesta:** subir `examples/hello_idf/` completo (D-09) y dejar en `evidence/` solo capturas y JSON.

## Cómo ejecutar las pruebas del backend

```
python -m unittest discover -s tests -v
```

Estas pruebas usan un `idf.py` simulado. **No sustituyen** P-04 (compilación real).

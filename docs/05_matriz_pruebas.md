# Matriz de pruebas

**Estado:** actualizar cada prueba unicamente despues de ejecutarla y conservar evidencia verificable.

| ID | Prueba | Criterio de aceptacion | Estado | Evidencia |
|---|---|---|---|---|
| P-01 | Consultar y seleccionar Python | Python responde con su version y el backend selecciona el entorno virtual de ESP-IDF | Completada | Python 3.14.0; seleccion verificada de `idf6.1_py3.14_env` el 12/11/2026 |
| P-02 | Consultar version de ESP-IDF | ESP-IDF responde con su version | Completada | ESP-IDF v6.1 |
| P-03 | Configurar objetivo ESP32 | El backend ejecuta `set-target esp32` correctamente | Completada | Resultado JSON con `target: esp32` |
| P-04 | Compilar proyecto de ejemplo | La compilacion termina con codigo de salida 0 | Completada | Compilacion real de `hello_idf` mediante el backend desde PowerShell normal. `compilacion_hello_idf_2026-11-12.json` |
| P-05 | Identificar archivos `.bin` | Se identifican los artefactos relevantes sin archivos auxiliares de CMake | Completada | JSON del 12/11/2026 con `hello_idf.bin`, `bootloader.bin` y `partition-table.bin` |
| P-06 | Manejar una ruta inexistente | El backend informa el error sin declarar exito | Completada | JSON con `success: false` y error de carpeta inexistente |
| P-07 | Manejar un proyecto invalido | El backend informa la ausencia de `CMakeLists.txt` | Completada | JSON con `success: false` y error por falta de `CMakeLists.txt` |
| P-08 | Detectar puertos | Se identifican los puertos disponibles mediante una implementacion definida | Pendiente | Salida de la herramienta seleccionada |
| P-09 | Cargar firmware en hardware | La carga termina correctamente en una placa real | Pendiente | Registro de carga y modelo de placa |
| P-10 | Compilar un proyecto con biblioteca | Un proyecto que utiliza la biblioteca compila correctamente | Pendiente | Proyecto y registro de compilacion |
| P-11 | Integracion con otros modulos | Los modulos intercambian datos conforme al contrato | Pendiente | Prueba conjunta |
| P-12 | Probar otros objetivos ESP32 | Cada objetivo requerido compila correctamente | Pendiente | Resultados por objetivo |
| P-13 | Exportar artefactos | Los archivos se guardan o exportan segun el contrato acordado | Pendiente | Archivos y registro de exportacion |

## Incidencia corregida

El 12/11/2026 se detecto que Windows podia entregar la variable de entorno como `Path`, mientras el backend consultaba `PATH`. Esto ocasionaba que se seleccionara el Python global en lugar del entorno virtual de ESP-IDF.

Se normalizo la clave de la variable de entorno y se verifico que el backend seleccionara el ejecutable correcto. Posteriormente se realizo una compilacion real exitosa de `hello_idf`.

El diagnostico inicial se conserva en `evidence/diagnostico_entorno_python_2026-11-12.json`.

## Alcance de las pruebas

Las pruebas completadas validan el entorno ESP-IDF 6.1, la preparacion automatica del entorno de ejecucion, la seleccion del Python correspondiente, la compilacion de un proyecto de ejemplo mediante el backend, la identificacion de los archivos `.bin` y el manejo de dos entradas invalidas.

Tambien se comprobo que el backend puede ejecutarse desde una terminal PowerShell normal, sin necesidad de activar manualmente el entorno ESP-IDF.

Estas pruebas no demuestran por si solas la integracion completa con el Editor, el IDE principal ni Log, tampoco la deteccion de puertos o la carga del firmware en una placa fisica.

Las pruebas de integracion deben ejecutarse cuando esten disponibles los modulos participantes y se hayan acordado sus interfaces.

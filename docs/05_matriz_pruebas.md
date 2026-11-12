# Matriz de pruebas

**Estado:** actualizar cada prueba únicamente después de ejecutarla y conservar evidencia verificable.

| ID | Prueba | Criterio de aceptación | Estado | Evidencia |
|---|---|---|---|---|
| P-01 | Consultar versión de Python | Python responde con su versión | Completada | Python 3.14.0 |
| P-02 | Consultar versión de ESP-IDF | ESP-IDF responde con su versión | Completada | ESP-IDF v6.1 |
| P-03 | Configurar objetivo ESP32 | El backend ejecuta `set-target esp32` correctamente | Completada | Resultado JSON con `target: esp32` |
| P-04 | Compilar proyecto de ejemplo | La compilación termina con código de salida 0 | Completada | Compilación exitosa de `hello_idf` mediante el backend desde PowerShell normal |
| P-05 | Identificar archivos `.bin` | Se identifican los artefactos relevantes sin archivos auxiliares de CMake | Completada | `hello_idf.bin`, `bootloader.bin` y `partition-table.bin` |
| P-06 | Manejar una ruta inexistente | El backend informa el error sin declarar éxito | Completada | JSON con `success: false` y error de carpeta inexistente |
| P-07 | Manejar un proyecto inválido | El backend informa la ausencia de `CMakeLists.txt` | Completada | JSON con `success: false` y error por falta de `CMakeLists.txt` |
| P-08 | Detectar puertos | Se identifican los puertos disponibles mediante una implementación definida | Pendiente | Salida de la herramienta seleccionada |
| P-09 | Cargar firmware en hardware | La carga termina correctamente en una placa real | Pendiente | Registro de carga y modelo de placa |
| P-10 | Compilar un proyecto con biblioteca | Un proyecto que utiliza la biblioteca compila correctamente | Pendiente | Proyecto y registro de compilación |
| P-11 | Integración con otros módulos | Los módulos intercambian datos conforme al contrato | Pendiente | Prueba conjunta |
| P-12 | Probar otros objetivos ESP32 | Cada objetivo requerido compila correctamente | Pendiente | Resultados por objetivo |
| P-13 | Exportar artefactos | Los archivos se guardan o exportan según el contrato acordado | Pendiente | Archivos y registro de exportación |

## Alcance de las pruebas

Las pruebas completadas validan el entorno ESP-IDF 6.1, la preparación automática del entorno de ejecución, la compilación de un proyecto de ejemplo mediante el backend, la identificación de los archivos `.bin` y el manejo de dos entradas inválidas.

También se comprobó que el backend puede ejecutarse desde una terminal PowerShell normal, sin necesidad de activar manualmente el entorno ESP-IDF.

Estas pruebas no demuestran por sí solas la integración completa con el Editor, el IDE principal ni Log, tampoco la detección de puertos o la carga del firmware en una placa física.

Las pruebas de integración deben ejecutarse cuando estén disponibles los módulos participantes y se hayan acordado sus interfaces.
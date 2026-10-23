# Matriz de pruebas

**Estado:** actualizar cada prueba unicamente despues de ejecutarla y conservar evidencia verificable.

| ID | Prueba | Criterio de aceptacion | Estado | Evidencia |
|---|---|---|---|---|
| P-01 | Consultar version de Python | Python responde con su version | Completada | Python 3.14.0 |
| P-02 | Consultar version de ESP-IDF | ESP-IDF responde con su version | Completada | ESP-IDF v6.1 |
| P-03 | Configurar objetivo ESP32 | El backend ejecuta `set-target esp32` correctamente | Completada | Resultado JSON con `target: esp32` |
| P-04 | Compilar proyecto de ejemplo | La compilacion termina con codigo de salida 0 | Completada | Resultado JSON de `hello_idf` |
| P-05 | Identificar archivos `.bin` | Se identifican los artefactos relevantes sin archivos auxiliares de CMake | Completada | `hello_idf.bin`, `bootloader.bin` y `partition-table.bin` |
| P-06 | Manejar una ruta inexistente | El backend informa el error sin declarar exito | Completada | JSON con error de carpeta inexistente |
| P-07 | Manejar un proyecto invalido | El backend informa la ausencia de `CMakeLists.txt` | Completada | JSON con error por falta de `CMakeLists.txt` |
| P-08 | Detectar puertos | Se identifican los puertos disponibles mediante una implementacion definida | Pendiente | Salida de la herramienta seleccionada |
| P-09 | Cargar firmware en hardware | La carga termina correctamente en una placa real | Pendiente | Registro de carga y modelo de placa |
| P-10 | Compilar un proyecto con biblioteca | Un proyecto que utiliza la biblioteca compila correctamente | Pendiente | Proyecto y registro de compilacion |
| P-11 | Integracion con Sketch | Los modulos intercambian datos conforme al contrato | Pendiente | Prueba conjunta |
| P-12 | Probar otros objetivos ESP32 | Cada objetivo requerido compila correctamente | Pendiente | Resultados por objetivo |
| P-13 | Exportar artefactos | Los archivos se guardan o exportan segun el contrato acordado | Pendiente | Archivos y registro de exportacion |

## Alcance de las pruebas

Las pruebas completadas validan el entorno ESP-IDF, la compilacion de un proyecto de ejemplo mediante el backend, la identificacion de artefactos y el manejo de dos entradas invalidas.

Estas pruebas no demuestran por si solas la integracion completa con el editor Sketch, la deteccion de puertos ni la carga del firmware en una placa fisica.

Las pruebas de integracion deben ejecutarse cuando esten disponibles los modulos participantes y se hayan acordado sus interfaces.

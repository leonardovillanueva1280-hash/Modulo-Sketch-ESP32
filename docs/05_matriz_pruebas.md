# Matriz de pruebas

**Estado:** actualizar cada prueba unicamente despues de ejecutarla y conservar evidencia verificable.

| ID | Prueba | Criterio de aceptacion | Estado | Evidencia |
|---|---|---|---|---|
| P-01 | Consultar version de Python | Python responde con su version | Completada | Python 3.14.0 |
| P-02 | Consultar version de ESP-IDF | ESP-IDF responde con su version | Completada | ESP-IDF v6.1 |
| P-03 | Configurar objetivo ESP32 | El proyecto acepta el objetivo requerido | Pendiente | Salida de `idf.py set-target esp32` |
| P-04 | Compilar proyecto de ejemplo | El proceso termina con codigo 0 | Completada | Resultado JSON de `hello_idf` |
| P-05 | Identificar artefactos `.bin` | Se identifican los artefactos relevantes sin archivos auxiliares de CMake | Completada | `hello_idf.bin`, `bootloader.bin` y `partition-table.bin` |
| P-06 | Manejar una ruta inexistente | El backend informa el error sin declarar exito | Pendiente | Resultado JSON |
| P-07 | Manejar un proyecto invalido | El backend informa la ausencia de `CMakeLists.txt` | Pendiente | Resultado JSON |
| P-08 | Detectar puertos | Se identifican los puertos disponibles mediante una implementacion definida | Pendiente | Salida de la herramienta seleccionada |
| P-09 | Cargar firmware en hardware | La carga termina correctamente en una placa real | Pendiente | Registro de carga y modelo de placa |
| P-10 | Compilar un proyecto con biblioteca | El proyecto que utiliza la biblioteca compila correctamente | Pendiente | Proyecto y registro de compilacion |
| P-11 | Integracion con Sketch | Los modulos intercambian datos conforme al contrato | Pendiente | Prueba conjunta |
| P-12 | Probar otros objetivos ESP32 | Cada objetivo requerido compila correctamente | Pendiente | Resultados por objetivo |
| P-13 | Exportar artefactos | Los archivos se guardan o exportan segun el contrato acordado | Pendiente | Archivos y registro de exportacion |

La compilacion exitosa de `hello_idf` valida el entorno y el backend con ese proyecto de ejemplo. No demuestra por si sola la integracion completa del modulo Sketch ni la compatibilidad con todas las placas.

La prueba P-03 debe marcarse como completada unicamente cuando se ejecute y se registre el comando de configuracion del objetivo.

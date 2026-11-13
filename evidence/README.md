# Evidencias de compilacion ESP-IDF

Esta carpeta conserva evidencias relacionadas con la validacion del modulo Sketch mediante ESP-IDF.

## 1. Evidencias disponibles

- `compilacion_hello_idf_2026-11-12.json`: resultado JSON de una compilacion real y exitosa del proyecto `hello_idf` mediante ESP-IDF 6.1.
- `diagnostico_entorno_python_2026-11-12.json`: resultado del diagnostico inicial que permitio identificar un problema en la seleccion del Python de ESP-IDF.
- `compilacion_esp32_2026-10-22.png`: captura historica de una compilacion de ejemplo realizada mediante Arduino CLI. No corresponde a la prueba actual de ESP-IDF.
- `main.c`: archivo de codigo de ejemplo utilizado como referencia.
- `CMakeLists.txt`: archivo de configuracion de ejemplo para el sistema de compilacion CMake.

## 2. Pruebas realizadas

- Verificacion del entorno Python y ESP-IDF.
- Seleccion automatica del Python perteneciente al entorno virtual de ESP-IDF.
- Configuracion del objetivo `esp32`.
- Compilacion exitosa del proyecto `hello_idf` mediante ESP-IDF 6.1 (12/11/2026).
- Identificacion de tres archivos `.bin`: bootloader, aplicacion y tabla de particiones.
- Prueba con una ruta de proyecto inexistente.
- Prueba con una carpeta sin `CMakeLists.txt`.

## 3. Incidencia corregida

Durante la ejecucion desde PowerShell se detecto que el backend podia seleccionar el Python global de Windows en lugar del Python del entorno virtual de ESP-IDF.

La causa fue la diferencia entre `Path` y `PATH` al recuperar las variables de entorno en Windows.

Se corrigio la normalizacion de la variable de entorno y se verifico que el backend seleccionara el ejecutable correcto. Posteriormente, la compilacion real de `hello_idf` finalizo correctamente.

## 4. Pruebas pendientes

- Compilacion de proyectos adicionales.
- Validacion con otras familias de chips ESP32.
- Deteccion de puertos USB/serial.
- Carga del firmware en una placa fisica.
- Integracion del backend con la interfaz Sketch y los demas modulos.

## 5. Criterios de evidencia

Cada prueba debe indicar que se ejecuto, el resultado obtenido y cualquier error relevante. No se debe presentar una prueba pendiente como completada.

La compilacion de un proyecto de ejemplo demuestra el funcionamiento del backend con ese proyecto, pero no confirma por si sola la integracion completa del modulo Sketch ni la carga del firmware en una placa fisica.

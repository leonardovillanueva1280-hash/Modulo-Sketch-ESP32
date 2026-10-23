# Migración inicial a ESP-IDF

## Objetivo
Eliminar la dependencia de Arduino IDE y Arduino CLI. Este prototipo llama a `idf.py build`.

## Importante
- El ejemplo es un proyecto ESP-IDF en C, no un sketch `.ino`.
- El backend Python es un adaptador, no un compilador propio.
- Requiere ESP-IDF y su toolchain instalados.
- No se ha validado aún en el equipo del autor; no declarar la prueba exitosa hasta ejecutarla.

## Prueba en Windows
1. Instala ESP-IDF desde la guía oficial de Espressif.
2. Abre la terminal de ESP-IDF configurada.
3. Copia `examples/hello_idf` a una ruta sin espacios, por ejemplo `C:\\esp\\hello_idf`.
4. Entra a esa carpeta y ejecuta `idf.py set-target esp32` (para el ESP32 clásico).
5. Ejecuta `idf.py build`.
6. Si compila, revisa los `.bin` en `build`.
7. Desde la raíz del repositorio, prueba el backend:
   `python src/esp_idf_backend.py C:\\esp\\hello_idf`

El objetivo cambia para chips como ESP32-S3, C3, etc. según la placa real.

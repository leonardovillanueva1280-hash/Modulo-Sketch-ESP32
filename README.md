# Modulo Sketch ESP32 — Backend ESP-ID

## Descripcion

Este repositorio contiene avances del modulo Sketch para un IDE orientado a placas ESP32. La migracion del backend de compilacion se esta realizando con ESP-IDF

El objetivo es proporcionar una base para compilar proyectos ESP-IDF, identificar los artefactos generados y entregar resultados que puedan utilizar otros modulos del IDE.

## Estado actual

- Entorno ESP-IDF 6.1 verificado.
- Proyecto de ejemplo `hello_idf` compilado correctamente.
- Backend ESP-IDF ejecutado correctamente contra el proyecto de ejemplo.
- Identificacion de artefactos `.bin` comprobada.
- Integracion con la interfaz Sketch pendiente de validacion.
- Comunicacion con Editor/Compilador y Log pendiente de pruebas conjuntas.
- Carga fisica en una placa ESP32 pendiente.
- Compatibilidad con otras placas y bibliotecas pendiente de validacion.

## Estructura relevante

- `src/esp_idf_backend.py`: backend experimental de compilacion ESP-IDF.
- `docs/`: documentacion, arquitectura, contrato y pruebas.
- `examples/`: proyectos de ejemplo.
- `evidence/`: espacio para conservar evidencias de pruebas, cuando esten disponibles.

La estructura real del repositorio puede cambiar conforme avance la integracion.

## Requisitos

- Windows.
- Python disponible en el entorno de ESP-IDF.
- ESP-IDF instalado y configurado.
- Un proyecto ESP-IDF valido con `CMakeLists.txt` en su raiz.

## Uso del backend

Abre una terminal ESP-IDF configurada y ejecuta el backend indicando la ruta del proyecto:

```powershell
python "C:\ruta\al\repositorio\src\esp_idf_backend.py" "C:\ruta\al\proyecto"
```

Para solicitar un objetivo especifico, por ejemplo ESP32:

```powershell
python "C:\ruta\al\repositorio\src\esp_idf_backend.py" "C:\ruta\al\proyecto" --target esp32
```

Sustituye las rutas de ejemplo por las ubicaciones reales de tu equipo. Usa `--target` solamente cuando el objetivo sea compatible con el proyecto y la placa prevista.

El backend devuelve un resultado JSON con el estado de compilacion, el codigo de retorno, la salida, los errores y las rutas de los artefactos identificados.

## Limitaciones actuales

- El backend no convierte automaticamente archivos `.ino` en proyectos ESP-IDF.
- La integracion con el editor y la interfaz Sketch aun debe definirse y probarse.
- La deteccion y gestion de puertos no esta implementada en este backend.
- La carga fisica del firmware no esta implementada en este backend.
- La compatibilidad con bibliotecas y diferentes objetivos debe validarse individualmente.

## Criterio de validacion

Una funcion se considera validada solamente despues de ejecutar la prueba correspondiente y conservar evidencia verificable. La compilacion del ejemplo `hello_idf` no demuestra por si sola que todo el modulo Sketch este terminado.

## Registro de avance

La prueba local del backend con el proyecto `hello_idf` finalizo con `success: true` y `returncode: 0`. Los artefactos identificados fueron `hello_idf.bin`, `bootloader.bin` y `partition-table.bin`.

Las pruebas de integracion y de hardware permanecen pendientes.

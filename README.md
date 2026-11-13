# Modulo Sketch ESP32 - Backend ESP-IDF

## Descripcion

Este repositorio contiene los avances del modulo Sketch para un IDE orientado a placas ESP32.

El objetivo es proporcionar un backend capaz de preparar el entorno ESP-IDF, compilar proyectos, identificar los artefactos generados y entregar resultados en formato JSON para su utilizacion por otros modulos del IDE.

## Estado actual

- Entorno ESP-IDF 6.1 verificado.
- Preparacion automatica del entorno desde PowerShell.
- Seleccion del entorno Python correspondiente a ESP-IDF.
- Proyecto de ejemplo `hello_idf` compilado correctamente.
- Identificacion de los tres archivos BIN principales comprobada.
- Evidencias de compilacion y diagnostico conservadas.
- Integracion con la interfaz Sketch pendiente de validacion.
- Comunicacion con Editor/Compilador y Log pendiente de pruebas conjuntas.
- Carga fisica del firmware en una placa ESP32 pendiente.
- Compatibilidad con otras placas y bibliotecas pendiente de validacion.

## Estructura relevante

- `src/esp_idf_backend.py`: backend de compilacion ESP-IDF.
- `docs/`: documentacion, arquitectura, contrato de integracion y pruebas.
- `evidence/`: evidencias de compilacion, diagnosticos y registros de validacion.

Los proyectos de prueba pueden encontrarse fuera de este repositorio.

## Requisitos

- Windows.
- Python disponible para ejecutar el backend.
- ESP-IDF instalado y accesible.
- Un proyecto ESP-IDF valido con `CMakeLists.txt` en su directorio raiz.

El backend prepara el entorno ESP-IDF automaticamente. No es necesario abrir previamente una terminal ESP-IDF configurada.

## Uso del backend

Abre PowerShell en la carpeta raiz del repositorio y ejecuta:

```powershell
python .\src\esp_idf_backend.py "C:\ruta\al\proyecto"
```

Para solicitar un objetivo especifico, por ejemplo ESP32:

```powershell
python .\src\esp_idf_backend.py "C:\ruta\al\proyecto" --target esp32
```

Sustituye las rutas de ejemplo por las ubicaciones reales de tu equipo. Utiliza `--target` solamente cuando el objetivo sea compatible con el proyecto y la placa prevista.

El backend devuelve un resultado JSON con informacion sobre el estado de compilacion, codigo de retorno, salida, errores, comando ejecutado y rutas de los artefactos identificados.

## Evidencias disponibles

En la carpeta `evidence/` se conservan:

- `compilacion_hello_idf_2026-11-12.json`: resultado de una compilacion exitosa con ESP-IDF 6.1.
- `diagnostico_entorno_python_2026-11-12.json`: registro del problema inicial de seleccion del entorno Python.
- `README.md`: descripcion de las evidencias y pruebas realizadas.

La matriz de pruebas y la bitacora de desarrollo se encuentran en `docs/`.

## Limitaciones actuales

- El backend no convierte automaticamente archivos `.ino` en proyectos ESP-IDF.
- La integracion con el editor y la interfaz Sketch aun debe definirse y probarse.
- La deteccion y gestion de puertos no esta implementada en este backend.
- La carga fisica del firmware no esta implementada en este backend.
- La compatibilidad con diferentes placas y bibliotecas debe validarse individualmente.
- La integracion con los modulos Compilador y Log requiere pruebas conjuntas.

## Criterio de validacion

Una funcion se considera validada solamente despues de ejecutar la prueba correspondiente y conservar evidencia verificable.

La compilacion exitosa del proyecto `hello_idf` demuestra el funcionamiento del proceso de compilacion del backend, pero no significa que todo el modulo Sketch este terminado.

## Registro de avance

El 12 de noviembre de 2026 se ejecuto el backend desde PowerShell normal utilizando ESP-IDF 6.1.

Resultado registrado:

- `success: true`
- `returncode: 0`
- Tres artefactos BIN identificados:
  - `bootloader.bin`
  - `hello_idf.bin`
  - `partition-table.bin`

Tambien se corrigio la seleccion de la variable PATH del entorno de Windows para evitar utilizar accidentalmente el Python global.

Las pruebas de integracion y de hardware permanecen pendientes.
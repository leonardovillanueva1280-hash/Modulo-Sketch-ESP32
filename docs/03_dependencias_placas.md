# Dependencias y seleccion de placas

## 1. Entorno de desarrollo

El backend de este modulo utiliza ESP-IDF para configurar el objetivo y compilar proyectos destinados a ESP32.

Dependencias principales:

- Python, necesario para ejecutar el backend.
- ESP-IDF instalado y configurado en el entorno de terminal.
- `idf.py`, disponible en el entorno de ejecucion.
- CMake y las herramientas de compilacion requeridas por ESP-IDF.
- Un proyecto ESP-IDF con su archivo `CMakeLists.txt`.
- Bibliotecas compatibles con ESP-IDF que requiera el proyecto.
- Drivers USB/serial correspondientes cuando se realicen pruebas con hardware.

Arduino IDE y Arduino CLI no forman parte del flujo de compilacion definido para este backend.

## 2. Comprobaciones en Windows

Ejecutar desde una terminal configurada para ESP-IDF:

```powershell
python --version
idf.py --version
idf.py --help
```

Para comprobar la compilacion, utilizar un proyecto ESP-IDF valido:

```powershell
idf.py set-target esp32
idf.py build
```

Los comandos de configuracion y compilacion deben ejecutarse desde la carpeta raiz del proyecto que se desea compilar.

La prueba mediante el backend tambien permite ejecutar estas operaciones y recibir un resultado normalizado en JSON.

## 3. Objetivos de compilacion y placas

ESP-IDF admite diferentes objetivos de compilacion. Algunos ejemplos son:

- `esp32`
- `esp32s2`
- `esp32s3`
- `esp32c3`
- `esp32c6`

La lista anterior es orientativa y no significa que todos los objetivos esten instalados, disponibles en el entorno o validados por este modulo.

El objetivo seleccionado debe corresponder al chip de la placa utilizada. La compatibilidad debe comprobarse con el modelo concreto, su configuracion y los requisitos del proyecto.

No se debe asumir que una compilacion exitosa para `esp32` demuestra compatibilidad con todas las placas ESP32.

## 4. Estado de validacion

### Validado

- Python 3.14.0.
- Entorno ESP-IDF v6.1.
- Disponibilidad de `idf.py` en la terminal utilizada.
- Configuracion del objetivo `esp32` en el proyecto de ejemplo.
- Compilacion exitosa del proyecto `hello_idf`.
- Identificacion de los archivos `.bin` relevantes.

### Pendiente

- Compilar proyectos para otros objetivos.
- Confirmar el modelo exacto de la placa fisica disponible.
- Detectar puertos USB/serial.
- Cargar el firmware en hardware real.
- Verificar drivers y comunicacion con el dispositivo.
- Probar bibliotecas adicionales mediante proyectos de ejemplo.

## 5. Bibliotecas

Por cada biblioteca que se incorpore al proyecto, registrar:

- Nombre y version, cuando se conozcan.
- Funcion dentro del proyecto.
- Procedimiento de instalacion.
- Compatibilidad con ESP-IDF.
- Objetivo de compilacion utilizado.
- Resultado de compilacion de un ejemplo minimo.
- Errores o ajustes necesarios.

Una biblioteca no debe marcarse como probada hasta que exista evidencia de una compilacion exitosa del proyecto que la utiliza.

## 6. Carga de firmware

La compilacion genera artefactos, pero no carga automaticamente el firmware en una placa.

La deteccion de puertos, la seleccion del dispositivo y la carga deben implementarse y probarse por separado. La compatibilidad con un metodo de programacion determinado debe confirmarse segun la placa y las herramientas utilizadas.

## 7. Evidencias

Conservar las salidas de las pruebas de entorno y compilacion. Para las pruebas con hardware, registrar tambien el modelo de placa, el puerto utilizado, el resultado de la carga y cualquier error relevante.

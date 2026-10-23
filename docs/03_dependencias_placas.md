# Dependencias y seleccion de placas ESP32

## 1. Requisitos del entorno

El backend de compilacion utiliza ESP-IDF como sistema de desarrollo y compilacion. 

Requisitos principales:

- Sistema operativo Windows.
- Python disponible en el entorno de ESP-IDF.
- ESP-IDF instalado y configurado.
- Herramientas de compilacion requeridas por la version instalada de ESP-IDF.
- Un proyecto ESP-IDF valido con su archivo `CMakeLists.txt`.
- Controladores USB/serial correspondientes, cuando sean necesarios para trabajar con hardware.

## 2. Comprobaciones del entorno

Ejecutar estos comandos desde una terminal ESP-IDF configurada:

```powershell
python --version
idf.py --version
idf.py --help
```

Para comprobar que un proyecto tiene configurado el objetivo ESP32:

```powershell
idf.py set-target esp32
```

Este ultimo comando debe ejecutarse dentro de la carpeta del proyecto. La configuracion del objetivo no sustituye la compilacion: despues debe ejecutarse `idf.py build`.

## 3. Seleccion del objetivo

ESP-IDF permite trabajar con diferentes objetivos de la familia ESP32, pero no todos los proyectos ni todas las placas son compatibles entre si.

Ejemplos de objetivos que pueden existir en ESP-IDF:

- `esp32`
- `esp32s2`
- `esp32s3`
- `esp32c3`
- `esp32c6`
- `esp32h2`

La disponibilidad depende de la version de ESP-IDF instalada.

El objetivo de compilacion identifica la familia de chip seleccionada. No siempre identifica el modelo comercial exacto de la placa. Antes de compilar o cargar firmware se debe confirmar el chip y la configuracion de la placa utilizada.

No se debe asumir que un proyecto compilado para `esp32` funcionara sin cambios en cualquier otra variante.

## 4. Estructura del proyecto

Un proyecto ESP-IDF convencional contiene un archivo `CMakeLists.txt` en la raiz y puede incluir directorios como `main`, componentes y archivos de configuracion.

Un archivo `.ino` no constituye por si solo un proyecto ESP-IDF convencional. La integracion con el editor debe definir como se organiza o adapta el codigo antes de iniciar la compilacion.

## 5. Bibliotecas y componentes

Las dependencias deben registrarse individualmente con la siguiente informacion:

- Nombre del componente o biblioteca.
- Version, cuando se conozca.
- Funcion dentro del proyecto.
- Metodo de incorporacion al proyecto ESP-IDF.
- Objetivos ESP32 compatibles.
- Estado de validacion.
- Resultado de compilacion de un ejemplo minimo.

No se debe marcar una biblioteca como compatible solo porque exista o porque haya funcionado en Arduino. Debe comprobarse su compatibilidad con ESP-IDF y con el objetivo utilizado.

## 6. Puertos y carga de firmware

La deteccion de puertos seriales, la seleccion del dispositivo y la carga de firmware son operaciones diferentes de la compilacion.

Estas funciones deben considerarse pendientes hasta que exista una implementacion integrada y pruebas verificables con el hardware correspondiente.

## 7. Estado de validacion

- Python 3.14.0: version verificada en el entorno utilizado.
- ESP-IDF 6.1: version verificada.
- Compilacion del proyecto de ejemplo `hello_idf`: completada correctamente.
- Compatibilidad con todas las placas enumeradas: pendiente de validacion.
- Compatibilidad de bibliotecas: pendiente de validar caso por caso.
- Deteccion de puertos desde el modulo Sketch: pendiente.
- Carga fisica del firmware: pendiente.

La compilacion satisfactoria de un proyecto de ejemplo valida ese caso concreto, pero no demuestra compatibilidad universal ni integracion completa con el IDE.

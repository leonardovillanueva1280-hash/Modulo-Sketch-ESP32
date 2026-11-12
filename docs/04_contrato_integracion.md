
# Contrato de integración — ESP-IDF

## 1. Objetivo

Definir la comunicación entre el módulo Sketch y el backend de compilación ESP-IDF. Este contrato establece las entradas, el resultado normalizado y las responsabilidades que deben respetar los módulos participantes.

El backend utiliza ESP-IDF y no depende de Arduino IDE ni Arduino CLI.

## 2. Operación disponible

### Compilar proyecto

El backend recibe la ruta de un proyecto ESP-IDF y ejecuta su compilación.

**Entradas:**

- `project`: ruta de la carpeta raíz del proyecto.
- `--target`: objetivo ESP-IDF opcional, por ejemplo `esp32` o `esp32s3`.
- `--timeout`: tiempo máximo por operación, en segundos. El valor predeterminado es 1800.

El proyecto debe contener un archivo `CMakeLists.txt` en su carpeta raíz.

**Preparación automática del entorno:**

Antes de compilar, el backend:

- Busca la instalación de ESP-IDF mediante la variable de entorno `IDF_PATH`.
- Si no encuentra una instalación válida mediante esa variable, utiliza la ruta predeterminada configurada.
- Comprueba la existencia de `export.bat` y `tools/idf.py`.
- Ejecuta `export.bat` para preparar las variables de entorno necesarias.
- Localiza el intérprete de Python del entorno virtual de ESP-IDF.

De esta manera, no es necesario activar manualmente ESP-IDF desde una terminal antes de ejecutar el backend.

**Ejemplo de ejecución:**

`python src/esp_idf_backend.py "ruta_del_proyecto" --target esp32`

## 3. Resultado normalizado

El backend devuelve un objeto JSON con los siguientes campos:

- `success`: indica si la operación de compilación terminó correctamente.
- `returncode`: código de salida del último comando ejecutado, cuando existe.
- `stdout`: salida estándar del proceso.
- `stderr`: salida de error del proceso.
- `command`: lista de comandos ejecutados.
- `framework`: nombre del framework utilizado; debe ser `ESP-IDF`.
- `project_path`: ruta del proyecto.
- `build_path`: ruta de la carpeta de compilación.
- `artifacts_dir`: carpeta donde se encuentran los artefactos.
- `bin_files`: rutas de los archivos `.bin` detectados después de una compilación exitosa.
- `target`: objetivo solicitado, si se proporcionó.
- `error`: descripción del error cuando la operación no termina correctamente.

Los campos deben conservar sus nombres para facilitar la integración con los demás módulos.

## 4. Responsabilidades del backend

El backend es responsable de:

- Validar la existencia de la carpeta del proyecto.
- Validar que exista `CMakeLists.txt` en la raíz del proyecto.
- Localizar la instalación de ESP-IDF.
- Preparar automáticamente el entorno de ejecución.
- Verificar la disponibilidad de `idf.py`.
- Configurar el objetivo solicitado cuando corresponda.
- Ejecutar la compilación mediante ESP-IDF.
- Capturar la salida y el código de retorno.
- Identificar los archivos `.bin` relevantes después de una compilación exitosa.
- Devolver el resultado normalizado en JSON.
- Informar los errores de validación o ejecución.

El tiempo de espera predeterminado es de 1800 segundos por operación de compilación o configuración del objetivo. La preparación del entorno tiene su propio límite de tiempo.

El backend no declara que el firmware fue cargado en una placa. La compilación exitosa no equivale a una carga exitosa.

## 5. Responsabilidades de los otros módulos

### Editor / Sketch

Debe proporcionar la ruta del proyecto que se desea compilar. La forma exacta de obtener y compartir esa ruta debe acordarse con el responsable del Editor.

### IDE principal / selección de placa

Debe comunicar el objetivo ESP-IDF seleccionado. La equivalencia entre las opciones visibles de placa y los objetivos admitidos debe acordarse con el responsable del IDE principal.

### Log / Monitorización

Debe recibir y presentar los mensajes de compilación y los errores. El formato y mecanismo de comunicación entre módulos quedan pendientes de acuerdo.

### Carga de firmware

La detección de puertos y la carga del firmware requieren una implementación y pruebas independientes. No forman parte de las operaciones actualmente verificadas en este backend.

## 6. Eventos propuestos para el log

Se proponen los siguientes eventos:

- `compile_started`
- `compile_succeeded`
- `compile_failed`
- `upload_started`
- `upload_succeeded`
- `upload_failed`

Estos eventos son una propuesta de integración. El backend actual devuelve un resultado JSON, pero aún no implementa por sí solo un sistema de eventos compartido.

## 7. Acuerdos pendientes

- [ ] Confirmar cómo recibe Sketch la ruta del proyecto desde Editor.
- [ ] Confirmar cómo se comunica el objetivo seleccionado por el IDE principal.
- [ ] Definir cómo invoca Sketch al backend.
- [ ] Definir cómo recibe Log el resultado y los mensajes.
- [ ] Definir la detección de puertos.
- [ ] Definir la carga del firmware.
- [ ] Definir cómo se guardan o exportan los archivos `.bin`.
- [ ] Validar el contrato con los responsables de los módulos participantes.

## 8. Límites de las pruebas actuales

Se han realizado las siguientes pruebas:

- Compilación exitosa de un proyecto de ejemplo ESP-IDF (`hello_idf`) con objetivo `esp32`.
- Ejecución del backend desde PowerShell normal, sin activar manualmente el entorno ESP-IDF.
- Preparación automática del entorno mediante `export.bat`.
- Identificación de tres archivos `.bin` generados durante la compilación: `bootloader.bin`, `hello_idf.bin` y `partition-table.bin`.
- Devolución de un resultado JSON con el estado de compilación y las rutas de los artefactos.
- Manejo de una ruta de proyecto inexistente.
- Manejo de un proyecto sin `CMakeLists.txt` en su raíz.

Estas pruebas no demuestran aún la integración completa con el Editor, el IDE principal y Log, ni la carga del firmware en una placa física.

La integración entre módulos y las pruebas de hardware quedan pendientes.
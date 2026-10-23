# Contrato de integracion — ESP-IDF

## 1. Objetivo

Definir la comunicacion entre el modulo Sketch y el backend de compilacion ESP-IDF. Este contrato establece las entradas, el resultado normalizado y las responsabilidades que deben respetar los modulos participantes.

El backend utiliza ESP-IDF y no debe depender de Arduino IDE ni Arduino CLI.

## 2. Operacion disponible

### Compilar proyecto

El backend recibe la ruta de un proyecto ESP-IDF y ejecuta su compilacion.

Entradas:

- `project`: ruta de la carpeta raiz del proyecto.
- `--target`: objetivo ESP-IDF opcional, por ejemplo `esp32` o `esp32s3`.
- `--timeout`: tiempo maximo por operacion, en segundos. El valor predeterminado es 600.

El proyecto debe contener un archivo `CMakeLists.txt` en su carpeta raiz.

Ejemplo de ejecucion:

`python src/esp_idf_backend.py "ruta_del_proyecto" --target esp32`

## 3. Resultado normalizado

El backend devuelve un objeto JSON con los siguientes campos:

- `success`: indica si la operacion de compilacion termino correctamente.
- `returncode`: codigo de salida del ultimo comando ejecutado, cuando existe.
- `stdout`: salida estandar del proceso.
- `stderr`: salida de error del proceso.
- `command`: lista de comandos ejecutados.
- `framework`: nombre del framework utilizado; debe ser `ESP-IDF`.
- `project_path`: ruta del proyecto.
- `build_path`: ruta de la carpeta de compilacion.
- `artifacts_dir`: carpeta donde se encuentran los artefactos.
- `bin_files`: rutas de los archivos `.bin` detectados despues de una compilacion exitosa.
- `target`: objetivo solicitado, si se proporciono.
- `error`: descripcion del error cuando la operacion no termina correctamente.

Los campos deben conservar sus nombres para facilitar la integracion con los demas modulos.

## 4. Responsabilidades del backend

El backend es responsable de:

- Validar la existencia de la carpeta del proyecto.
- Validar que exista `CMakeLists.txt`.
- Verificar que `idf.py` este disponible.
- Configurar el objetivo solicitado cuando corresponda.
- Ejecutar la compilacion.
- Capturar la salida y el codigo de retorno.
- Identificar los archivos `.bin` relevantes despues de una compilacion exitosa.
- Devolver el resultado normalizado en JSON.

El backend no declara que el firmware fue cargado en una placa. La compilacion exitosa no equivale a una carga exitosa.

## 5. Responsabilidades de los otros modulos

### Editor / Sketch

Debe proporcionar la ruta del proyecto que se desea compilar. La forma exacta de obtener y compartir esa ruta debe acordarse con el responsable del Editor.

### IDE principal / seleccion de placa

Debe comunicar el objetivo ESP-IDF seleccionado. La equivalencia entre las opciones visibles de placa y los objetivos admitidos debe acordarse con el responsable del IDE principal.

### Log / Monitorizacion

Debe recibir y presentar los mensajes de compilacion y los errores. El formato y mecanismo de comunicacion entre modulos quedan pendientes de acuerdo.

### Carga de firmware

La deteccion de puertos y la carga del firmware requieren una implementacion y pruebas independientes. No forman parte de las operaciones actualmente verificadas en este backend.

## 6. Eventos propuestos para el log

Se proponen los siguientes eventos:

- `compile_started`
- `compile_succeeded`
- `compile_failed`
- `upload_started`
- `upload_succeeded`
- `upload_failed`

Estos eventos son una propuesta de integracion. El backend actual devuelve un resultado JSON, pero aun no implementa por si solo un sistema de eventos compartido.

## 7. Acuerdos pendientes

- [ ] Confirmar como recibe Sketch la ruta del proyecto desde Editor.
- [ ] Confirmar como se comunica el objetivo seleccionado por el IDE principal.
- [ ] Definir como invoca Sketch al backend.
- [ ] Definir como recibe Log el resultado y los mensajes.
- [ ] Definir la deteccion de puertos.
- [ ] Definir la carga del firmware.
- [ ] Definir como se guardan o exportan los archivos `.bin`.
- [ ] Validar el contrato con los responsables de los modulos participantes.

## 8. Limites de las pruebas actuales

Se ha comprobado la compilacion de un proyecto de ejemplo ESP-IDF con objetivo `esp32`, la identificacion de archivos `.bin` y el manejo de dos entradas invalidas.

Estas pruebas no demuestran aun la integracion completa con el Editor, el IDE principal, Log ni una placa fisica.

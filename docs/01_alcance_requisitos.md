# Alcance y requisitos

## Proposito

Desarrollar el modulo Sketch de un IDE orientado a ESP32, utilizando ESP-IDF como sistema de compilacion y tomando como referencia general el flujo de trabajo de un IDE de desarrollo embebido.

El backend de este modulo no debe depender de Arduino IDE ni Arduino CLI.

## Funciones dentro del alcance

- Recibir la ruta del proyecto que se desea compilar.
- Configurar el objetivo ESP-IDF seleccionado.
- Validar la estructura basica del proyecto.
- Ejecutar la compilacion y comunicar el resultado.
- Mostrar la salida estandar y los mensajes de error.
- Identificar los archivos de firmware `.bin` generados.
- Permitir definir una carpeta de salida cuando se acuerde e implemente esa funcion.
- Detectar y seleccionar puertos para la carga del firmware.
- Cargar el firmware en un dispositivo compatible.
- Considerar la carga mediante programador segun la compatibilidad.
- Exportar el firmware generado.
- Mostrar o abrir la carpeta del proyecto.
- Facilitar la inclusion de bibliotecas y archivos compatibles con ESP-IDF.
- Integrarse con Editor, Log/Monitorizacion e IDE principal.

Las funciones anteriores representan el alcance previsto. No todas se encuentran implementadas ni verificadas en el estado actual.

## Requisitos funcionales

- RF-01: recibir la ruta de la carpeta raiz del proyecto ESP-IDF.
- RF-02: recibir el objetivo ESP-IDF seleccionado, por ejemplo `esp32` o `esp32s3`.
- RF-03: ejecutar la compilacion mediante `idf.py`, sin utilizar Arduino CLI.
- RF-04: informar el resultado segun el codigo de salida del proceso.
- RF-05: devolver la salida estandar y los mensajes de error.
- RF-06: validar la existencia del proyecto y de su archivo `CMakeLists.txt`.
- RF-07: permitir configurar el tiempo maximo de ejecucion de la operacion.
- RF-08: identificar los archivos `.bin` relevantes despues de una compilacion exitosa.
- RF-09: permitir indicar una carpeta de salida cuando se defina e implemente esa funcion.
- RF-10: detectar los puertos disponibles mediante una herramienta compatible.
- RF-11: permitir seleccionar el puerto para la carga del firmware.
- RF-12: separar compilacion, exportacion y carga para poder probarlas individualmente.
- RF-13: registrar y comunicar las acciones y sus resultados.
- RF-14: integrar el backend con Editor, Log/Monitorizacion e IDE principal mediante un contrato acordado.

## Requisitos no funcionales

- Mostrar mensajes tecnicos claros y legibles.
- Mantener una estructura de resultado consistente para facilitar la integracion.
- No declarar exito cuando la compilacion termina con error.
- No informar archivos de firmware como resultado de una compilacion fallida.
- No asumir que todos los objetivos ESP32 son compatibles con todos los modelos de placa.
- Mantener un registro de pruebas y evidencias verificables.
- Evitar dependencias de Arduino IDE y Arduino CLI en el flujo de compilacion.

## Estado de implementacion

### Implementado y probado

- Backend independiente para ESP-IDF.
- Validacion de la ruta del proyecto.
- Validacion de la presencia de `CMakeLists.txt`.
- Configuracion del objetivo `esp32`.
- Compilacion de un proyecto de ejemplo.
- Resultado normalizado en JSON.
- Identificacion de los archivos `.bin` relevantes.
- Manejo de rutas inexistentes y proyectos sin `CMakeLists.txt`.

### Pendiente de implementar o validar

- Integracion real con el editor Sketch.
- Comunicacion con Log/Monitorizacion e IDE principal.
- Deteccion y seleccion de puertos.
- Carga del firmware en una placa fisica.
- Exportacion configurable de artefactos.
- Pruebas con bibliotecas y otros objetivos ESP32.
- Validacion conjunta de los modulos participantes.

## Limites de este hito

Las pruebas realizadas validan el backend con un proyecto de ejemplo. No demuestran la integracion completa del IDE, la carga fisica del firmware ni la compatibilidad con todas las placas ESP32.

No se debe afirmar que un requisito esta completado hasta contar con una implementacion y evidencia de prueba adecuadas.

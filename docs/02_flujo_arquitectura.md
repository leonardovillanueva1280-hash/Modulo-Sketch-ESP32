# Flujo y arquitectura — Modulo Sketch ESP32

## 1. Flujo principal

**Solicitud de compilacion → validacion del proyecto → ejecucion del backend ESP-IDF → recopilacion del resultado → identificacion de artefactos → comunicacion del resultado.**

La carga de firmware a una placa fisica es una operacion independiente. No se considera implementada hasta que se integre y se pruebe con hardware real.

## 2. Componentes

### Interfaz Sketch

- Recibe la accion solicitada por el usuario.
- Proporciona la ruta del proyecto y el objetivo de compilacion, cuando corresponda.
- Muestra el resultado de la operacion.

### Backend ESP-IDF

- Recibe la ruta de un proyecto ESP-IDF.
- Ejecuta las operaciones de compilacion admitidas.
- Captura el codigo de salida y los mensajes del proceso.
- Identifica los archivos `.bin` disponibles.
- Devuelve el resultado en formato JSON.

### Editor/Compilador

- Proporciona el codigo que se desea compilar.
- Debe definir como preparar un proyecto compatible con ESP-IDF.
- Debe acordar con Sketch la forma de entregar el proyecto al backend.

ESP-IDF utiliza proyectos basados en CMake. Un archivo `.ino` aislado no se compila directamente como un proyecto ESP-IDF convencional. La adaptacion del codigo del editor sigue siendo un punto de integracion que debe definirse.

### Log/Monitorizacion

- Presenta los mensajes de compilacion.
- Permite distinguir resultados exitosos, advertencias y errores.
- Facilita el diagnostico de fallos.

La comunicacion efectiva con este modulo debe validarse mediante pruebas conjuntas.

### Gestion de artefactos

- Identifica los archivos generados por el proceso.
- Devuelve las rutas de los artefactos encontrados.
- Evita considerar archivos auxiliares como resultados principales de la compilacion.

## 3. Flujo detallado

1. El usuario solicita compilar un proyecto.
2. Sketch obtiene la ruta del proyecto y el objetivo solicitado.
3. El backend valida la entrada y ejecuta ESP-IDF.
4. El proceso de compilacion devuelve un codigo de salida y mensajes.
5. El backend recopila la informacion y busca los artefactos `.bin`.
6. El resultado se devuelve a Sketch.
7. La interfaz y el modulo Log presentan el resultado segun el contrato de integracion acordado.

## 4. Principios de diseno

- Utilizar ESP-IDF como sistema de compilacion, sin depender de Arduino IDE ni Arduino CLI.
- Mantener separado el backend de la interfaz.
- Validar la ruta del proyecto antes de iniciar la operacion.
- Capturar el codigo de salida y los mensajes del proceso.
- No declarar una compilacion exitosa cuando el proceso termina con error.
- No presentar archivos antiguos como resultados de una compilacion fallida.
- No asumir que todas las placas ESP32 utilizan el mismo objetivo.
- Tratar la carga fisica y la monitorizacion serial como operaciones independientes hasta implementarlas y validarlas.
- No declarar terminada la integracion entre modulos antes de ejecutar pruebas conjuntas.

## 5. Estado de validacion

- Entorno ESP-IDF 6.1: verificado.
- Compilacion del ejemplo `hello_idf`: completada correctamente.
- Identificacion de `hello_idf.bin`, `bootloader.bin` y `partition-table.bin`: verificada para el ejemplo.
- Integracion del backend con la interfaz Sketch: pendiente.
- Comunicacion con Editor/Compilador: pendiente.
- Comunicacion con Log: pendiente.
- Carga fisica en una placa ESP32: pendiente.
- Compatibilidad con otras placas y bibliotecas: pendiente de pruebas especificas.

La compilacion satisfactoria de `hello_idf` demuestra que el entorno y el backend funcionan para ese proyecto de ejemplo. No demuestra por si sola que el modulo Sketch este completamente integrado ni que todas las placas sean compatibles.

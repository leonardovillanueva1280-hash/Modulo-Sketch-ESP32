# Flujo y arquitectura — Modulo Sketch ESP32

## 1. Flujo principal

**Codigo del editor → preparacion o identificacion del proyecto ESP-IDF → seleccion del objetivo de compilacion → compilacion → identificacion de artefactos `.bin` → resultado en Log/Monitorizacion.**

La carga al ESP32 se considera una operacion independiente y solo se dara por implementada cuando exista una prueba satisfactoria con hardware real.

**Nota de compatibilidad:** ESP-IDF utiliza proyectos basados en CMake y no compila directamente un archivo `.ino` como un proyecto ESP-IDF convencional. La integracion con el editor debe definir como se organiza o adapta el codigo antes de compilarlo.

## 2. Componentes

- **Interfaz Sketch:** recibe el codigo o la ruta del proyecto, el objetivo de compilacion y la accion solicitada.
- **Backend ESP-IDF:** ejecuta las operaciones admitidas mediante las herramientas de ESP-IDF y devuelve el codigo de salida, los mensajes y el estado de la operacion.
- **Editor/Compilador:** proporciona el codigo y recibe el resultado conforme al contrato de integracion.
- **Log/Monitorizacion:** muestra o registra los mensajes, advertencias y errores de cada operacion.
- **IDE principal:** coordina la configuracion y la comunicacion entre modulos.
- **Gestion de artefactos:** identifica los archivos generados por una compilacion exitosa y comunica sus ubicaciones.

## 3. Principios de diseño

- Separar el backend de la interfaz.
- Utilizar ESP-IDF como sistema de compilacion, sin depender de Arduino IDE ni Arduino CLI.
- Identificar explicitamente el objetivo de compilacion y validar su compatibilidad con el proyecto.
- Capturar la salida estandar, los errores y el codigo de retorno.
- Identificar la carpeta de compilacion y los artefactos generados.
- No declarar una compilacion exitosa si el proceso termina con error.
- No presentar archivos `.bin` antiguos como resultado de una compilacion fallida.
- No asumir que todas las placas ESP32 utilizan la misma configuracion o generan exactamente los mismos artefactos.
- Mantener la carga fisica y la monitorizacion serial como operaciones independientes hasta implementar y validar su integracion.
- No declarar terminada la integracion entre modulos antes de ejecutar pruebas conjuntas.

## 4. Estado de validacion

- **Entorno ESP-IDF:** se verifico la version 6.1.
- **Proyecto de ejemplo:** compilacion de `hello_idf` completada correctamente.
- **Backend integrado con Sketch:** pendiente de validacion.
- **Comunicacion con Editor/Compilador y Log:** pendiente de pruebas conjuntas.
- **Carga fisica al ESP32:** pendiente.
- **Compatibilidad con varias placas y bibliotecas:** pendiente de validar para cada caso.

La compilacion satisfactoria del proyecto de ejemplo demuestra que el entorno puede compilar ese proyecto, pero no demuestra por si sola que el modulo Sketch este integrado o terminado.

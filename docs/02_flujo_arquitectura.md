# Flujo y arquitectura - Modulo Sketch ESP32

## 1. Flujo principal

**Solicitud de compilacion -> validacion del proyecto ESP-IDF -> configuracion opcional del objetivo -> ejecucion de la compilacion -> identificacion de artefactos -> resultado JSON.**

La integracion con Log/Monitorizacion y los demas modulos debe respetar el contrato de integracion acordado.

La carga al ESP32 es una operacion independiente y solo se considerara implementada cuando exista una prueba satisfactoria con hardware real.

**Nota de compatibilidad:** ESP-IDF utiliza proyectos basados en CMake. No compila directamente un archivo `.ino` como un proyecto ESP-IDF convencional. La integracion con el editor debe definir como se organiza o adapta el codigo antes de compilarlo.

## 2. Componentes

- **Interfaz Sketch:** debe recibir el codigo o la ruta del proyecto, el objetivo de compilacion y la accion solicitada.
- **Backend ESP-IDF:** valida el proyecto, ejecuta las operaciones admitidas y devuelve un resultado JSON normalizado.
- **Editor/Compilador:** debe proporcionar un proyecto compatible con ESP-IDF y recibir el resultado conforme al contrato.
- **Log/Monitorizacion:** debe mostrar o registrar los mensajes, advertencias y errores de cada operacion.
- **IDE principal:** debe coordinar la configuracion y la comunicacion entre modulos.
- **Gestion de artefactos:** identifica los archivos generados por una compilacion exitosa y comunica sus ubicaciones.

Los componentes que todavia no se han conectado deben considerarse pendientes de integracion.

## 3. Principios de diseno

- Separar el backend de la interfaz.
- Utilizar ESP-IDF como sistema de compilacion, sin depender de Arduino IDE ni Arduino CLI.
- Validar la existencia del proyecto y de su archivo `CMakeLists.txt`.
- Identificar explicitamente el objetivo de compilacion.
- Capturar la salida estandar, los errores y el codigo de retorno.
- Identificar la carpeta de compilacion y los artefactos generados.
- No declarar una compilacion exitosa si el proceso termina con error.
- No presentar archivos `.bin` antiguos como resultado de una compilacion fallida.
- No asumir que todas las placas ESP32 utilizan la misma configuracion o generan exactamente los mismos artefactos.
- Mantener la carga fisica y la monitorizacion serial como operaciones independientes hasta implementar y validar su integracion.
- No declarar terminada la integracion entre modulos antes de ejecutar pruebas conjuntas.

## 4. Estado de validacion

- **Entorno ESP-IDF:** version 6.1 verificada.
- **Proyecto de ejemplo:** compilacion de `hello_idf` completada correctamente.
- **Configuracion del objetivo `esp32`:** ejecutada correctamente mediante el backend.
- **Manejo de entradas invalidas:** probada una ruta inexistente y un proyecto sin `CMakeLists.txt`.
- **Identificacion de artefactos:** comprobada en el proyecto de ejemplo.
- **Integracion real con Sketch:** pendiente de validacion.
- **Comunicacion con Editor/Compilador y Log:** pendiente de pruebas conjuntas.
- **Deteccion de puertos y carga fisica:** pendientes.
- **Compatibilidad con otras placas y bibliotecas:** pendiente de validar para cada caso.

La compilacion satisfactoria del proyecto de ejemplo demuestra que el entorno puede compilar ese proyecto mediante el backend. No demuestra por si sola que el modulo Sketch este integrado o terminado.

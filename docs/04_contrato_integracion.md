# Contrato de integracion — Modulo Sketch ESP32

## 1. Objetivo

Definir los datos de entrada y salida del backend ESP-IDF para facilitar su futura integracion con la interfaz Sketch, el Editor/Compilador y el modulo Log.

## 2. Entrada del backend

El backend recibe la ruta de un proyecto ESP-IDF valido.

Parametros disponibles:

- `project_path`: ruta del proyecto que se desea compilar.
- `--target`: objetivo de compilacion opcional, por ejemplo `esp32`.
- `--timeout`: limite de tiempo para cada operacion ejecutada, cuando se proporciona.

El proyecto debe contar con la estructura requerida por ESP-IDF. Un archivo `.ino` aislado no es suficiente para compilar un proyecto ESP-IDF convencional.

## 3. Salida del backend

El backend devuelve un objeto JSON con los datos disponibles de la operacion.

| Campo | Descripcion |
|---|---|
| `success` | Indica si la operacion finalizo correctamente. |
| `returncode` | Codigo de salida del proceso ejecutado. |
| `stdout` | Salida estandar del proceso. |
| `stderr` | Mensajes de error y salida de error del proceso. |
| `command` | Comandos ejecutados por el backend. |
| `framework` | Framework utilizado; debe indicar `ESP-IDF`. |
| `project_path` | Ruta del proyecto procesado. |
| `build_path` | Ruta del directorio de compilacion. |
| `artifacts_dir` | Directorio donde se buscan los artefactos generados. |
| `bin_files` | Lista de archivos `.bin` identificados. |
| `target` | Objetivo solicitado, si se proporciono. |
| `error` | Informacion adicional del error, cuando corresponda. |

La presencia de un campo depende del resultado y de la implementacion vigente. Los consumidores deben manejar campos opcionales y resultados de error sin asumir que siempre existiran archivos `.bin`.

## 4. Responsabilidades de los modulos

### Sketch

- Recibir la accion solicitada por el usuario.
- Proporcionar la ruta del proyecto y el objetivo cuando corresponda.
- Mostrar el resultado devuelto por el backend.
- No declarar una operacion exitosa si el backend informa un error.

### Backend ESP-IDF

- Validar la entrada necesaria.
- Ejecutar las operaciones de ESP-IDF admitidas.
- Capturar los codigos de salida y los mensajes del proceso.
- Identificar los artefactos disponibles.
- Devolver el resultado en el formato acordado.

### Editor/Compilador

- Definir como se organiza el codigo del editor para convertirlo en un proyecto ESP-IDF valido.
- Acordar con Sketch la forma de entregar la ruta del proyecto.
- Validar conjuntamente la compilacion de un proyecto generado o preparado desde el editor.

### Log/Monitorizacion

- Recibir o mostrar los mensajes de compilacion.
- Distinguir resultados exitosos, advertencias y errores.
- Conservar informacion util para diagnosticar fallos.

La comunicacion entre estos modulos debe comprobarse mediante pruebas conjuntas antes de considerarse implementada.

## 5. Flujo de operacion

1. El usuario solicita compilar.
2. Sketch proporciona la ruta del proyecto y, si corresponde, el objetivo.
3. El backend ejecuta la compilacion con ESP-IDF.
4. El backend recopila el resultado del proceso.
5. Se identifican los artefactos disponibles.
6. El resultado se entrega a Sketch y se comunica al modulo Log segun el contrato que acuerde el equipo.

La carga de firmware y la monitorizacion serial se consideran operaciones independientes y pendientes de integracion.

## 6. Manejo de errores

- Una ruta inexistente no debe producir un resultado exitoso.
- Un proyecto sin la estructura requerida debe reportar el problema.
- Una compilacion fallida no debe presentarse como exitosa.
- No deben reportarse archivos antiguos como si fueran resultado de una compilacion fallida.
- Los modulos consumidores deben poder mostrar errores sin cerrar inesperadamente la interfaz.

## 7. Estado de integracion

- Backend con proyecto de ejemplo `hello_idf`: probado.
- Resultado JSON y codigo de retorno: verificados en la prueba realizada.
- Identificacion de archivos `.bin`: verificada para el ejemplo.
- Integracion con la interfaz Sketch: pendiente.
- Comunicacion con Editor/Compilador: pendiente.
- Comunicacion con Log: pendiente.
- Deteccion de puertos y carga fisica: pendientes.

## 8. Acuerdos pendientes del equipo

Antes de conectar los modulos, el equipo debe acordar:

- El formato definitivo de las solicitudes y respuestas.
- La forma en que el editor prepara un proyecto ESP-IDF.
- La ubicacion de los proyectos temporales y de los artefactos.
- La forma de enviar los mensajes al modulo Log.
- El manejo de cancelaciones, tiempos de espera y errores.
- Las pruebas conjuntas y sus criterios de aceptacion.

Este contrato describe el estado actual y la integracion prevista. Los puntos pendientes no deben considerarse implementados hasta contar con pruebas verificables.

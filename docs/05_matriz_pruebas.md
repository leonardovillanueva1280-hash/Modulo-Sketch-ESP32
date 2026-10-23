# Matriz de pruebas

**Estado inicial: pendiente. Actualizar solo después de ejecutar cada prueba.**

| ID | Prueba | Criterio de aceptación | Estado | Evidencia |
|---|---|---|---|---|
| P-01 | `python --version` | Python responde con versión | Pendiente | Captura |
| P-02 | `arduino-cli version` | CLI responde sin error | Pendiente | Captura |
| P-03 | `arduino-cli core list` | Core ESP32 aparece instalado | Pendiente | Captura |
| P-04 | `arduino-cli board listall esp32` | Lista placas disponibles | Pendiente | Salida guardada |
| P-05 | Compilar sketch mínimo | Código de salida 0 | Pendiente | Log |
| P-06 | Identificar `.bin` | Se encuentra archivo en salida de compilación | Pendiente | Listado de archivos |
| P-07 | FQBN incorrecto | Se muestra error y no se declara éxito | Pendiente | Log |
| P-08 | Listar puertos | Se muestran dispositivos detectables | Pendiente | Salida CLI |
| P-09 | Carga física | Carga termina correctamente en placa real | Pendiente | Log y modelo |
| P-10 | Biblioteca | Sketch que la usa compila | Pendiente | Sketch y log |
| P-11 | Integración | Módulos intercambian datos según contrato | Pendiente | Prueba conjunta |
| P-12 | Varias placas | Compilación separada para cada FQBN probado | Pendiente | Matriz de modelos |

La función programada no equivale a una función validada.

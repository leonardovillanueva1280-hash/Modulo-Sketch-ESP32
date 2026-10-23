# Alcance y requisitos

## Propósito
Gestionar operaciones del programa en el IDE orientado a ESP32, siguiendo como referencia el flujo de Arduino IDE.

## Funciones dentro del alcance
- Verificar/compilar un sketch.
- Configurar placa y puerto.
- Cargar el programa al dispositivo.
- Considerar carga mediante programador según compatibilidad.
- Exportar el firmware `.bin`.
- Mostrar/abrir la carpeta del sketch.
- Incluir bibliotecas y añadir archivos.
- Integrarse con Editor/Compilador, Log/Monitorización e IDE principal.

## Requisitos funcionales
- RF-01: recibir la ruta del sketch.
- RF-02: recibir un FQBN seleccionado para la placa.
- RF-03: ejecutar compilación mediante Arduino CLI.
- RF-04: informar éxito/error según el código de salida.
- RF-05: mostrar salida estándar y mensajes de error.
- RF-06: permitir indicar carpeta de salida.
- RF-07: listar puertos cuando la herramienta los detecte.
- RF-08: permitir seleccionar puerto para la carga.
- RF-09: separar compilación, exportación y carga para probarlas individualmente.
- RF-10: registrar acciones y resultados.

## Requisitos no funcionales
- Mostrar mensajes técnicos y legibles.
- No asumir que un FQBN funciona con todas las placas ESP32.
- No declarar éxito si la herramienta devuelve error.
- Mantener registro de pruebas y evidencias.

## Fuera de alcance para afirmar en este hito
No afirmar compatibilidad con todas las placas ESP32 ni carga física exitosa sin pruebas reales.

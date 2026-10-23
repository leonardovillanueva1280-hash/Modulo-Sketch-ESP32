# Flujo y arquitectura

## Flujo principal
**Código `.ino` → selección de placa/FQBN → compilación → artefactos/`.bin` → carga al ESP32 → resultado en Log/Monitorización.**

## Componentes
- **Interfaz Sketch:** recoge sketch, placa, puerto y acción.
- **Backend Arduino CLI:** ejecuta comandos y devuelve código de salida, salida y error.
- **Editor/Compilador:** aporta el código y recibe el resultado de compilación, según contrato.
- **Log/Monitorización:** muestra o registra mensajes y errores.
- **IDE principal:** coordina la configuración y acceso al módulo.

## Principios
- Separar backend e interfaz.
- Pasar el FQBN explícitamente.
- Capturar salida, errores y código de retorno.
- Guardar artefactos en carpeta identificable.
- No asumir que todas las placas generan un `.bin` con el mismo nombre o conjunto de archivos.
- No marcar integración como terminada antes de las pruebas conjuntas.

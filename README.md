# Avance de Leonardo — Módulo Sketch / Programa ESP32

Base de documentación y backend inicial para el área Investigación / Análisis e Integración, y para el trabajo compartido con Xavi en bibliotecas, compilación y exportación de `.bin`.

**Ojo:** esto es una base de avance, aun no se afirma que haya compilado ni que se haya probado con hardware. Registra solo pruebas ejecutadas realmente.

## Archivos
- `docs/01_alcance_requisitos.md`
- `docs/02_flujo_arquitectura.md`
- `docs/03_dependencias_placas.md`
- `docs/04_contrato_integracion.md`
- `docs/05_matriz_pruebas.md`
- `docs/06_bitacora.md`
- `src/arduino_backend.py`

## Requisitos
Windows, Python 3 y el core ESP32 instalado. El backend no instala esas dependencias.

## Uso
```powershell
python src\arduino_backend.py list-boards
python src\arduino_backend.py list-ports
python src\arduino_backend.py compile "C:\ruta\MiSketch" --fqbn esp32:esp32:esp32 --output build
```
El FQBN `esp32:esp32:esp32` es solo un ejemplo inicial para una placa ESP32 genérica; no representa todos los modelos. Consulta `arduino-cli board listall esp32` y selecciona el FQBN que corresponda a la placa concreta.

## Hito del 23/10/2026
El cronograma  dice que el desarrollo principal, archivos, bibliotecas y `.bin` deben estar **encaminados**. Este paquete organiza avances y pendientes; no sustituye las pruebas reales ni demuestra que la compilación funcione en el equipo.

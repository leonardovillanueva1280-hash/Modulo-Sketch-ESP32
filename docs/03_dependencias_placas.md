# Dependencias y selección de placas

## Dependencias
- Python 3.
- Arduino CLI.
- Core `esp32` de Espressif instalado en Arduino CLI.
- Bibliotecas que requiera cada sketch.
- Drivers USB/serial correspondientes, cuando aplique.

## Comprobaciones en Windows
```powershell
python --version
arduino-cli version
arduino-cli core list
arduino-cli board list
arduino-cli board listall esp32
```

## Placas
La familia ESP32 incluye distintas series y placas. No se debe asumir que un único FQBN sirve para todas. Elegirlo según el modelo y las opciones que muestre el core instalado.

Ejemplo no universal: `esp32:esp32:esp32`

## Registro de bibliotecas
Por cada biblioteca registrar nombre, versión si se conoce, función, forma de instalación, compatibilidad confirmada/pendiente y resultado de compilación de un ejemplo mínimo. No marcarla como probada sin compilar un sketch que la incluya.

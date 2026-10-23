# Contrato de integración — borrador para acordar

Esta propuesta debe revisarse con Xavi y con responsables de Editor/Compilador, Log/Monitorización e IDE principal.

## Entradas para compilar
- `sketch_path`: carpeta del sketch.
- `fqbn`: identificador de placa.
- `build_path`: carpeta de salida opcional.

## Resultado normalizado sugerido
- `success`: éxito según código de salida.
- `returncode`: código de salida.
- `stdout` y `stderr`: mensajes de la herramienta.
- `command`: comando ejecutado.
- `artifacts_dir`: carpeta de artefactos.
- `bin_files`: `.bin` encontrados después de una compilación exitosa.

## Eventos sugeridos para el log
`compile_started`, `compile_succeeded`, `compile_failed`, `upload_started`, `upload_succeeded`, `upload_failed`.

Cada evento debería incluir fecha/hora, operación, mensaje y resultado.

## Acuerdos pendientes
- [ ] Cómo recibe Sketch la ruta del sketch desde Editor.
- [ ] Cómo se comparte el FQBN seleccionado.
- [ ] Formato del resultado de compilación.
- [ ] Cómo se envían los mensajes al Log.
- [ ] Cómo comunica el IDE principal placa y puerto.
- [ ] Convención para guardar/exportar `.bin`.

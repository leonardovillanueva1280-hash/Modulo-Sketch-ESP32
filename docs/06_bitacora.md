\### 22/10/2026 — Prueba de compilación para ESP32



\*\*Responsable:\*\* Leonardo Villanueva.



\*\*Objetivo:\*\* Verificar la compilación de un programa de prueba para ESP32 y la generación de archivos binarios mediante Arduino CLI.



\*\*Procedimiento realizado:\*\*

\- Se preparó un sketch de prueba llamado `PruebaESP32.ino`.

\- Se configuró Arduino CLI con el paquete de soporte ESP32.

\- Se compiló el sketch para la configuración de placa `esp32:esp32:esp32`.

\- Se especificó una carpeta de salida para conservar los archivos generados.



\*\*Resultado observado:\*\* Se generaron archivos binarios, incluidos `PruebaESP32.ino.bin`, `PruebaESP32.ino.merged.bin` y `PruebaESP32.ino.partitions.bin`, además de archivos de compilación `.elf` y `.map`.



\*\*Evidencia:\*\* `evidence/compilacion\_esp32\_2026-10-22.png`.



\*\*Alcance y limitaciones:\*\* Se comprobó la generación de archivos de compilación para la configuración seleccionada. No se realizó una carga en una placa física ni se validó el funcionamiento del programa en hardware. Esta prueba constituye un avance técnico del módulo Sketch y no representa la finalización de su integración.



\*\*Pendiente:\*\* Integrar el proceso de compilación en el módulo propio, continuar con las pruebas previstas y coordinar la integración con los demás equipos.


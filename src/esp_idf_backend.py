"""Backend de compilacion ESP-IDF para el modulo Sketch."""

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def crear_resultado(
    success=False,
    returncode=None,
    stdout="",
    stderr="",
    command=None,
    proyecto=None,
    build=None,
    bin_files=None,
    error=None,
    target=None,
):
    """Devuelve un resultado con una estructura consistente."""
    resultado = {
        "success": success,
        "returncode": returncode,
        "stdout": stdout,
        "stderr": stderr,
        "command": command or [],
        "framework": "ESP-IDF",
        "project_path": str(proyecto) if proyecto else None,
        "build_path": str(build) if build else None,
        "artifacts_dir": str(build) if build else None,
        "bin_files": bin_files or [],
        "target": target,
    }

    if error:
        resultado["error"] = error

    return resultado


def compilar_proyecto(ruta_proyecto, timeout=600, target=None):
    """Compila un proyecto ESP-IDF y devuelve un resultado normalizado."""
    proyecto = Path(ruta_proyecto).expanduser().resolve()
    build = proyecto / "build"

    if not proyecto.is_dir():
        return crear_resultado(
            error=f"No existe la carpeta del proyecto: {proyecto}",
            proyecto=proyecto,
            build=build,
            target=target,
        )

    if not (proyecto / "CMakeLists.txt").is_file():
        return crear_resultado(
            error="Falta CMakeLists.txt en la raiz del proyecto.",
            proyecto=proyecto,
            build=build,
            target=target,
        )

    idf_py = shutil.which("idf.py")

    if not idf_py:
        return crear_resultado(
            error=(
                "No se encontro idf.py. Abre una terminal "
                "ESP-IDF configurada e intenta de nuevo."
            ),
            proyecto=proyecto,
            build=build,
            target=target,
        )

    if timeout <= 0:
        return crear_resultado(
            error="El tiempo maximo debe ser mayor que cero.",
            proyecto=proyecto,
            build=build,
            target=target,
        )

    comandos = []

    try:
        if target:
            comando_target = [idf_py, "set-target", target]
            comandos.append(comando_target)

            configuracion = subprocess.run(
                comando_target,
                cwd=str(proyecto),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                check=False,
            )

            if configuracion.returncode != 0:
                return crear_resultado(
                    returncode=configuracion.returncode,
                    stdout=configuracion.stdout,
                    stderr=configuracion.stderr,
                    command=comandos,
                    proyecto=proyecto,
                    build=build,
                    target=target,
                    error="No se pudo configurar el objetivo ESP-IDF.",
                )

        comando_build = [idf_py, "build"]
        comandos.append(comando_build)

        proceso = subprocess.run(
            comando_build,
            cwd=str(proyecto),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            check=False,
        )

        compilacion_ok = proceso.returncode == 0

        # Solo informar artefactos si esta compilacion fue exitosa.
        bin_files = []
        if compilacion_ok and build.is_dir():
                   bin_files = []
        if compilacion_ok and build.is_dir():
            bin_files = sorted(
                str(archivo.resolve())
                for archivo in build.rglob("*.bin")
                if archivo.is_file()
                and "CMakeFiles" not in archivo.parts
            )

        return crear_resultado(
            success=compilacion_ok,
            returncode=proceso.returncode,
            stdout=proceso.stdout,
            stderr=proceso.stderr,
            command=comandos,
            proyecto=proyecto,
            build=build,
            bin_files=bin_files,
            target=target,
            error=None if compilacion_ok else "La compilacion fallo.",
        )

    except subprocess.TimeoutExpired:
        return crear_resultado(
            command=comandos,
            proyecto=proyecto,
            build=build,
            target=target,
            error=f"Tiempo maximo excedido ({timeout} segundos).",
        )

    except OSError as exc:
        return crear_resultado(
            command=comandos,
            proyecto=proyecto,
            build=build,
            target=target,
            error=f"No se pudo ejecutar ESP-IDF: {exc}",
        )


def main():
    parser = argparse.ArgumentParser(
        description="Backend ESP-IDF para ESP32, sin Arduino CLI."
    )
    parser.add_argument(
        "project",
        help="Ruta de la carpeta raiz de un proyecto ESP-IDF.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="Tiempo maximo por operacion, en segundos.",
    )
    parser.add_argument(
        "--target",
        help="Objetivo ESP-IDF, por ejemplo esp32 o esp32s3.",
    )

    args = parser.parse_args()

    resultado = compilar_proyecto(
        args.project,
        timeout=args.timeout,
        target=args.target,
    )

    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0 if resultado["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

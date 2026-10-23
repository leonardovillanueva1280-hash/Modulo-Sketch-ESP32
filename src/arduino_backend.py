"""Backend inicial para Arduino CLI. Requiere instalación externa de Arduino CLI y core ESP32."""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def run_cli(args: list[str]) -> dict:
    exe = shutil.which("arduino-cli")
    if not exe:
        return {"success": False, "returncode": None, "stdout": "",
                "stderr": "No se encontró arduino-cli en PATH. Instálalo y reinicia la terminal.",
                "command": ["arduino-cli", *args]}
    command = [exe, *args]
    try:
        p = subprocess.run(command, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", check=False)
        return {"success": p.returncode == 0, "returncode": p.returncode,
                "stdout": p.stdout, "stderr": p.stderr, "command": command}
    except OSError as exc:
        return {"success": False, "returncode": None, "stdout": "",
                "stderr": str(exc), "command": command}


def emit(result: dict) -> int:
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["success"] else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Backend inicial Arduino CLI para Sketch IDE")
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("list-boards", help="Lista placas ESP32 disponibles en el core instalado")
    sub.add_parser("list-ports", help="Lista puertos/dispositivos detectados")
    cp = sub.add_parser("compile", help="Compila un sketch Arduino")
    cp.add_argument("sketch", type=Path)
    cp.add_argument("--fqbn", required=True, help="FQBN correspondiente a la placa")
    cp.add_argument("--output", type=Path, default=Path("build"))
    args = parser.parse_args()

    if args.action == "list-boards":
        return emit(run_cli(["board", "listall", "esp32"]))
    if args.action == "list-ports":
        return emit(run_cli(["board", "list", "--format", "json"]))
    if args.action == "compile":
        if not args.sketch.is_dir():
            return emit({"success": False, "returncode": None, "stdout": "",
                         "stderr": f"No existe la carpeta del sketch: {args.sketch}",
                         "command": []})
        args.output.mkdir(parents=True, exist_ok=True)
        result = run_cli(["compile", "--fqbn", args.fqbn,
                          "--output-dir", str(args.output.resolve()),
                          str(args.sketch.resolve())])
        result["fqbn"] = args.fqbn
        result["sketch_path"] = str(args.sketch.resolve())
        result["artifacts_dir"] = str(args.output.resolve())
        if result["success"]:
            result["bin_files"] = [str(p.resolve()) for p in args.output.rglob("*.bin")]
            if not result["bin_files"]:
                result["note"] = "Compilación exitosa, pero no se localizó .bin en la carpeta indicada; revisar artefactos del core."
        return emit(result)
    return 2


if __name__ == "__main__":
    sys.exit(main())

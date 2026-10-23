"""Backend experimental ESP-IDF; no usa Arduino IDE ni Arduino CLI."""
import argparse
import json
import shutil
import subprocess
from pathlib import Path

def compilar_proyecto(ruta_proyecto, timeout=600):
    proyecto = Path(ruta_proyecto).expanduser().resolve()
    if not proyecto.is_dir():
        return {"success": False, "error": f"No existe la carpeta: {proyecto}"}
    if not (proyecto / "CMakeLists.txt").is_file():
        return {"success": False, "error": "Falta CMakeLists.txt en la raíz del proyecto."}
    idf_py = shutil.which("idf.py")
    if not idf_py:
        return {"success": False, "error": "No se encontró idf.py. Abre una terminal ESP-IDF configurada."}
    try:
        p = subprocess.run([idf_py, "build"], cwd=str(proyecto),
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=timeout, check=False)
        build = proyecto / "build"
        bins = sorted(str(x.resolve()) for x in build.rglob("*.bin")) if build.exists() else []
        return {"success": p.returncode == 0, "returncode": p.returncode,
                "stdout": p.stdout, "stderr": p.stderr, "framework": "ESP-IDF",
                "project_path": str(proyecto), "build_path": str(build.resolve()),
                "bin_files": bins}
    except subprocess.TimeoutExpired:
        return {"success": False, "error": f"Tiempo máximo excedido ({timeout} s)."}
    except OSError as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backend ESP-IDF para ESP32, sin Arduino CLI")
    parser.add_argument("project", help="Carpeta raíz de un proyecto ESP-IDF")
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()
    result = compilar_proyecto(args.project, args.timeout)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result.get("success") else 1)

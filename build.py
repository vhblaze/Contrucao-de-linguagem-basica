import sys
from pathlib import Path


def main():
    projeto = Path(__file__).resolve().parent
    entrada_cli = projeto / "cli.py"
    pasta_build = projeto / "build"
    pasta_dist = projeto / "dist"

    try:
        import PyInstaller.__main__ as pyinstaller
    except ImportError:
        print(
            "PyInstaller nao esta instalado. Execute: python -m pip install pyinstaller",
            file=sys.stderr,
        )
        return 1

    argumentos = [
        str(entrada_cli),
        "--onefile",
        "--name",
        "leadscript",
        "--clean",
        "--noconfirm",
        "--distpath",
        str(pasta_dist),
        "--workpath",
        str(pasta_build),
        "--specpath",
        str(pasta_build),
        "--paths",
        str(projeto),
        "--hidden-import",
        "asyncio",
    ]

    print("Compilando runner LeadScript com PyInstaller...")
    print("PyInstaller " + " ".join(argumentos))
    pyinstaller.run(argumentos)

    print("\nBuild finalizado.")
    print("Executavel gerado em:")
    print(f"  {projeto / 'dist' / _nome_executavel()}")
    return 0


def _nome_executavel():
    return "leadscript.exe" if sys.platform.startswith("win") else "leadscript"


if __name__ == "__main__":
    raise SystemExit(main())

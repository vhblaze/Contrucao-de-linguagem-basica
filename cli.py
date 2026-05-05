import argparse
import asyncio
import os
import sys

from errors import LeadScriptError
from main import executar_arquivo


def criar_parser():
    parser = argparse.ArgumentParser(
        prog="leadscript",
        description="Runner oficial da linguagem LeadScript.",
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    rodar = subparsers.add_parser(
        "rodar",
        help="Executa um arquivo .las.",
    )
    rodar.add_argument(
        "arquivo",
        help="Caminho absoluto ou relativo para o script .las.",
    )
    rodar.add_argument(
        "--pausar",
        action="store_true",
        help="Mantem a janela aberta ao final da execucao.",
    )

    return parser


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    pausar_ao_final = False

    # Permite arrastar um .las diretamente sobre leadscript.exe no Windows.
    if len(argv) == 1 and not argv[0].startswith("-"):
        argv = ["rodar", argv[0]]
        pausar_ao_final = _deve_pausar_por_drag_and_drop()

    parser = criar_parser()
    args = parser.parse_args(argv)

    if args.comando == "rodar":
        try:
            asyncio.run(executar_arquivo(args.arquivo))
            return _finalizar(0, pausar_ao_final or args.pausar)
        except LeadScriptError as erro:
            print(erro.format(), file=sys.stderr)
            return _finalizar(1, pausar_ao_final or args.pausar)

    parser.print_help()
    return 1


def _deve_pausar_por_drag_and_drop():
    return bool(getattr(sys, "frozen", False)) and os.name == "nt" and sys.stdout.isatty()


def _finalizar(codigo_saida, pausar):
    if pausar:
        input("\nPressione Enter para sair...")
    return codigo_saida


if __name__ == "__main__":
    raise SystemExit(main())

import argparse
import asyncio
import sys
from pathlib import Path

from errors import LeadScriptError, RuntimeErrorCustom
from interpreter import Interpreter
from lexico import AnalisadorLexico
from parser_1 import Parser


def resolver_caminho_arquivo(caminho):
    arquivo = Path(caminho).expanduser()
    if not arquivo.is_absolute():
        arquivo = Path.cwd() / arquivo
    return arquivo.resolve(strict=False)


async def executar_codigo_async(codigo, filename="<memoria>"):
    try:
        lexer = AnalisadorLexico(codigo)
        tokens = lexer.analisar()

        parser = Parser(tokens)
        ast = parser.parse()

        interpreter = Interpreter()
        return await interpreter.visit(ast)
    except LeadScriptError as erro:
        raise erro.with_context(filename=filename, source=codigo) from erro


def executar_codigo(codigo, filename="<memoria>"):
    return asyncio.run(executar_codigo_async(codigo, filename=filename))


async def executar_arquivo(caminho):
    arquivo = resolver_caminho_arquivo(caminho)

    if arquivo.suffix.lower() != ".las":
        raise RuntimeErrorCustom(
            "Arquivos LeadScript devem usar a extensao .las.",
            filename=str(arquivo),
        )

    try:
        codigo = arquivo.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeErrorCustom(f"Arquivo '{arquivo}' nao encontrado.") from exc

    return await executar_codigo_async(codigo, filename=arquivo.name)


def modo_interativo():
    while True:
        print("\n=== LeadScript ===")
        print("1 - Executar arquivo .las")
        print("2 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            caminho = input("Digite o caminho do arquivo: ").strip()
            try:
                asyncio.run(executar_arquivo(caminho))
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            print("Encerrando...")
            break

        else:
            print("Opcao invalida.")


def criar_parser():
    parser = argparse.ArgumentParser(
        prog="leadscript",
        description="Runner oficial da linguagem LeadScript.",
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    subparsers.add_parser(
        "interativo",
        help="Modo interativo para executar scripts .las.",
    )

    rodar = subparsers.add_parser(
        "rodar",
        help="Executa um arquivo .las.",
    )
    rodar.add_argument(
        "arquivo",
        help="Caminho absoluto ou relativo para o script .las.",
    )

    return parser


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)

    # Compatibilidade: python main.py arquivo.las
    if (
        len(argv) == 1
        and not argv[0].startswith("-")
        and argv[0] not in ("interativo", "rodar")
    ):
        argv = ["rodar", argv[0]]

    parser = criar_parser()
    args = parser.parse_args(argv)

    if args.comando == "interativo":
        modo_interativo()
        return 0

    if args.comando == "rodar":
        try:
            asyncio.run(executar_arquivo(args.arquivo))
            return 0
        except LeadScriptError as erro:
            print(erro.format(), file=sys.stderr)
            return 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
from lexico import AnalisadorLexico
from parser import Parser
from interpreter import Interpreter
import sys


def executar_codigo(codigo):
    try:
        # =========================
        # 1. LEXER
        # =========================
        lexer = AnalisadorLexico(codigo)
        tokens = lexer.analisar()

        # Debug (opcional)
        # print("\nTOKENS:")
        # for t in tokens:
        #     print(t)

        # =========================
        # 2. PARSER
        # =========================
        parser = Parser(tokens)
        ast = parser.parse()

        # Debug (opcional)
        # print("\nAST:")
        # print(ast)

        # =========================
        # 3. INTERPRETER
        # =========================
        interpreter = Interpreter()
        interpreter.visit(ast)

    except Exception as e:
        print(f"Erro: {e}")


# =========================
# EXECUÇÃO VIA TERMINAL
# =========================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py arquivo.nl")
    else:
        arquivo = sys.argv[1]

        try:
            with open(arquivo, "r") as f:
                codigo = f.read()
                executar_codigo(codigo)
        except FileNotFoundError:
            print("Arquivo não encontrado!")
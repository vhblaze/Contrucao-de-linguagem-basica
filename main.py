from lexico import AnalisadorLexico
from parser import Parser
from interpreter import Interpreter
import sys

def executar_codigo(codigo):
    try:

        lexer = AnalisadorLexico(codigo)
        tokens = lexer.analisar()

        parser = Parser(tokens)
        ast = parser.parse()

        interpreter = Interpreter()
        interpreter.visit(ast)

    except Exception as e:
        print(f"Erro: {e}")

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
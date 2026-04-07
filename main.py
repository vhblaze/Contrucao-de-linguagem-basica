from lexico import AnalisadorLexico
from parser_1 import Parser
from interpreter import Interpreter
from errors import LexicalError, SyntaxErrorCustom, RuntimeErrorCustom
import sys

def executar_codigo(codigo):
    try:
        lexer = AnalisadorLexico(codigo)      
        tokens = lexer.analisar()
        tokens = lexer.tokens

        parser = Parser(tokens)
        ast = parser.parse()

        interpreter = Interpreter()
        interpreter.visit(ast)

    
    except LexicalError as e:
        print(f"Erro Lexico: {e}")
    except SyntaxErrorCustom as e:
        print(f"Erro de Sintaxe: {e}")
    except RuntimeErrorCustom as e:
        print(f"Erro de Execução: {e}")


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
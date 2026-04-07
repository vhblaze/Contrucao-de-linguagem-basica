from enum import Enum
from errors import LexicalError


# =========================
# TIPOS DE TOKEN (ENUM)
# =========================
class TipoToken(Enum):
    CATCHMON = "CATCHMON"
    GIVEMON = "GIVEMON"
    IFMON = "IFMON"
    ELSEMON = "ELSEMON"
    ENTAOMON = "ENTAOMON"
    DEXOUT = "DEXOUT"

    IDENTIFICADOR = "IDENTIFICADOR"
    NUMERO = "NUMERO"
    WHILEMON = "WHILEMON"
    ATRIBUICAO = "="
    IGUALDADE = "=="
    DIFERENTE = "!="
    MAIOR = ">"
    MENOR = "<"
    MAIOR_IGUAL = ">="
    MENOR_IGUAL = "<="
    SOMA = "+"
    SUB = "-"
    MULT = "*"
    DIV = "/"
    MOD = "%"     
    AND = "&&"      
    OR = "||"      
    NOT = "!"          

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    PONTO_VIRGULA = ";"
    LBARRA = "["
    RBARRA = "]"
    EOF = "EOF"
    VIRGULA = ","

class Token:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token({self.tipo.name}, {repr(self.valor)})"

class AnalisadorLexico:
    def __init__(self, codigo_fonte):
        self.codigo = codigo_fonte
        self.posicao = 0
        self.tokens = []

        self.palavras_chave = {
            "catchmon": TipoToken.CATCHMON,
            "givemon": TipoToken.GIVEMON,
            "ifmon": TipoToken.IFMON,
            "elsemon": TipoToken.ELSEMON,
            "entaomon": TipoToken.ENTAOMON,
            "whilemon": TipoToken.WHILEMON,
            "dexout": TipoToken.DEXOUT,
            "&&": TipoToken.AND,
            "||": TipoToken.OR,
            "!": TipoToken.NOT,
            "(": TipoToken.LPAREN,
            ")": TipoToken.RPAREN,
            "{": TipoToken.LBRACE,
            "}": TipoToken.RBRACE,
            ";": TipoToken.PONTO_VIRGULA,
            "[": TipoToken.LBARRA,
            "]": TipoToken.RBARRA
            
        }

    def _caractere_atual(self):
        if self.posicao >= len(self.codigo):
            return None
        return self.codigo[self.posicao]

    def _avancar(self):
        self.posicao += 1

    def _proximo(self):
        if self.posicao + 1 >= len(self.codigo):
            return None
        return self.codigo[self.posicao + 1]

    def analisar(self):
        while self._caractere_atual() is not None:
            char = self._caractere_atual()

            if char.isspace():
                self._avancar()
                continue

            if char == "~" and self._proximo() == "~":
                self._avancar()
                self._avancar()
                while self._caractere_atual() not in [None, "\n"]:
                    self._avancar()
                continue

            if char.isdigit():
                numero = ""
                while self._caractere_atual() and self._caractere_atual().isdigit():
                    numero += self._caractere_atual()
                    self._avancar()

                self.tokens.append(Token(TipoToken.NUMERO, int(numero)))
                continue

            if char.isalpha() or char == "_":
                ident = ""
                while self._caractere_atual() and (
                    self._caractere_atual().isalnum() or self._caractere_atual() == "_"
                ):
                    ident += self._caractere_atual()
                    self._avancar()

                tipo = self.palavras_chave.get(ident, TipoToken.IDENTIFICADOR)
                self.tokens.append(Token(tipo, ident))
                continue

            if char == "=" and self._proximo() == "=":
                self.tokens.append(Token(TipoToken.IGUALDADE, "=="))
                self._avancar(); self._avancar()
                continue

            if char == "!" and self._proximo() == "=":
                self.tokens.append(Token(TipoToken.DIFERENTE, "!="))
                self._avancar(); self._avancar()
                continue

            if char == ">" and self._proximo() == "=":
                self.tokens.append(Token(TipoToken.MAIOR_IGUAL, ">="))
                self._avancar(); self._avancar()
                continue

            if char == "<" and self._proximo() == "=":
                self.tokens.append(Token(TipoToken.MENOR_IGUAL, "<="))
                self._avancar(); self._avancar()
                continue

            if char == "&" and self._proximo() == "&":
                self.tokens.append(Token(TipoToken.AND, "&&"))
                self._avancar(); self._avancar()
                continue

            if char == "|" and self._proximo() == "|":
                self.tokens.append(Token(TipoToken.OR, "||"))
                self._avancar(); self._avancar()
                continue

            if char == "=":
                self.tokens.append(Token(TipoToken.ATRIBUICAO, "="))
            elif char == ">":
                self.tokens.append(Token(TipoToken.MAIOR, ">"))
            elif char == "<":
                self.tokens.append(Token(TipoToken.MENOR, "<"))
            elif char == "+":
                self.tokens.append(Token(TipoToken.SOMA, "+"))
            elif char == "-":
                self.tokens.append(Token(TipoToken.SUB, "-"))
            elif char == "*":
                self.tokens.append(Token(TipoToken.MULT, "*"))
            elif char == "/":
                self.tokens.append(Token(TipoToken.DIV, "/"))
            elif char == "%":
                self.tokens.append(Token(TipoToken.MOD, "%"))
            elif char == "!":
                self.tokens.append(Token(TipoToken.NOT, "!")) 
            elif char == "(":
                self.tokens.append(Token(TipoToken.LPAREN, "("))
            elif char == ")":
                self.tokens.append(Token(TipoToken.RPAREN, ")"))
            elif char == "{":
                self.tokens.append(Token(TipoToken.LBRACE, "{"))
            elif char == "}":
                self.tokens.append(Token(TipoToken.RBRACE, "}"))
            elif char == ";":
                self.tokens.append(Token(TipoToken.PONTO_VIRGULA, ";"))
            elif char == ",":
                self.tokens.append(Token(TipoToken.VIRGULA, ","))
            elif char == "[":
                self.tokens.append(Token(TipoToken.LBARRA, "["))
            elif char == "]":
                self.tokens.append(Token(TipoToken.RBARRA, "]"))
            else:
                raise LexicalError(f"Caractere inválido: '{char}'")

            self._avancar()

        self.tokens.append(Token(TipoToken.EOF))
        return self.tokens
from ast_nodes import *
from lexico import TipoToken

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # =========================
    # AUXILIARES
    # =========================
    def _current(self):
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]

    def _advance(self):
        self.pos += 1

    def _expect(self, tipo):
        token = self._current()
        if token.tipo == tipo:
            self._advance()
            return token
        raise SyntaxError(f"Esperado {tipo}, encontrado {token}")

    # =========================
    # ENTRY POINT
    # =========================
    def parse(self):
        statements = []

        while self._current().tipo != TipoToken.EOF:
            statements.append(self._parse_statement())

        return Program(statements)

    # =========================
    # STATEMENTS
    # =========================
    def _parse_statement(self):
        token = self._current().tipo

        if token == TipoToken.CATCHMON:
            return self._parse_var_decl()

        elif token == TipoToken.IDENTIFICADOR:
            return self._parse_assignment()

        elif token == TipoToken.IFMON:
            return self._parse_if()

        elif token == TipoToken.DEXOUT:
            return self._parse_output()

        else:
            raise SyntaxError(f"Comando inesperado: {self._current()}")

    def _parse_var_decl(self):
        self._expect(TipoToken.CATCHMON)
        name = self._expect(TipoToken.IDENTIFICADOR).valor

        self._expect(TipoToken.ATRIBUICAO)
        value = self._parse_expression()

        self._expect(TipoToken.PONTO_VIRGULA)

        return VarDecl(name, value)

    def _parse_assignment(self):
        name = self._expect(TipoToken.IDENTIFICADOR).valor

        self._expect(TipoToken.ATRIBUICAO)
        value = self._parse_expression()

        self._expect(TipoToken.PONTO_VIRGULA)

        return Assignment(name, value)

    def _parse_if(self):
        self._expect(TipoToken.IFMON)
        self._expect(TipoToken.LPAREN)

        condition = self._parse_expression()

        self._expect(TipoToken.RPAREN)

        then_block = self._parse_block()

        else_block = None
        if self._current().tipo == TipoToken.ELSEMON:
            self._advance()
            else_block = self._parse_block()

        return If(condition, then_block, else_block)

    def _parse_output(self):
        self._expect(TipoToken.DEXOUT)
        value = self._parse_expression()
        self._expect(TipoToken.PONTO_VIRGULA)

        return Output(value)

    def _parse_block(self):
        self._expect(TipoToken.LBRACE)

        statements = []
        while self._current().tipo != TipoToken.RBRACE:
            statements.append(self._parse_statement())

        self._expect(TipoToken.RBRACE)

        return Block(statements)

    # =========================
    # EXPRESSÕES (IGUAL AO SLIDE)
    # =========================

    # menor precedência
    def _parse_expression(self):
        node = self._parse_term()

        while self._current().tipo in (TipoToken.SOMA, TipoToken.SUB):
            op = self._current()
            self._advance()
            right = self._parse_term()
            node = BinaryOp(node, op, right)

        return node

    # precedência média
    def _parse_term(self):
        node = self._parse_factor()

        while self._current().tipo in (TipoToken.MULT, TipoToken.DIV):
            op = self._current()
            self._advance()
            right = self._parse_factor()
            node = BinaryOp(node, op, right)

        return node

    # maior precedência
    def _parse_factor(self):
        token = self._current()

        if token.tipo == TipoToken.NUMERO:
            self._advance()
            return Number(token.valor)

        elif token.tipo == TipoToken.IDENTIFICADOR:
            self._advance()
            return Identifier(token.valor)

        elif token.tipo == TipoToken.LPAREN:
            self._advance()
            node = self._parse_expression()
            self._expect(TipoToken.RPAREN)
            return node

        else:
            raise SyntaxError(f"Token inesperado em fator: {token}")
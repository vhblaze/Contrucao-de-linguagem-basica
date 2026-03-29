from platform import node
from turtle import left, right

from lexico import TipoToken
from ast_nodes import *

class Interpreter:
    def __init__(self):
        self.env = {}

    def visit(self, node):

        if isinstance(node, BlockNode):
            for stmt in node.statements:
                self.visit(stmt)

        elif isinstance(node, NumberNode):
            return node.value

        elif isinstance(node, VarNode):
            if node.name not in self.env:
                raise Exception(f"Variável '{node.name}' não definida")
            return self.env[node.name]

        elif isinstance(node, BinOpNode):
            left = self.visit(node.left)
            right = self.visit(node.right)
            op = node.op.tipo

            if op == TipoToken.SOMA:
                return left + right
            elif op == TipoToken.SUB:
                return left - right
            elif op == TipoToken.MULT:
                return left * right
            elif op == TipoToken.DIV:
                return left / right
            
            elif op == TipoToken.MAIOR:
                return left > right
            elif op == TipoToken.MENOR:
                return left < right
            elif op == TipoToken.MAIOR_IGUAL:
                return left >= right
            elif op == TipoToken.MENOR_IGUAL:
                return left <= right
            elif op == TipoToken.IGUALDADE:
                return left == right
            elif op == TipoToken.DIFERENTE:
                return left != right
            elif op == TipoToken.MOD:
                return left % right
            elif op == TipoToken.AND:
                return left and right
            elif op == TipoToken.OR:
                return left or right
            elif isinstance(node, UnaryOpNode):
                value = self.visit(node.expr)
            elif node.op.tipo == TipoToken.NOT:
                return not value
            else:
                raise Exception(f"Operador não suportado: {op}")
            
        elif isinstance(node, VarDeclNode):
            value = self.visit(node.value)
            self.env[node.name] = value

        elif isinstance(node, AssignNode):
            if node.name not in self.env:
                raise Exception(f"Variável '{node.name}' não definida")
            value = self.visit(node.value)
            self.env[node.name] = value

        elif isinstance(node, OutputNode):
            value = self.visit(node.expr)
            print(value)

        elif isinstance(node, IfNode):
            condition = self.visit(node.condition)

            if condition:
                self.visit(node.then_block)
            elif node.else_block:
                self.visit(node.else_block)

        else:
            raise Exception(f"Nó desconhecido: {node}")
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
            return self.env.get(node.name, 0)

        elif isinstance(node, BinOpNode):
            left = self.visit(node.left)
            right = self.visit(node.right)

            if node.op.tipo == TipoToken.SOMA:
                return left + right
            elif node.op.tipo == TipoToken.SUB:
                return left - right
            elif node.op.tipo == TipoToken.MULT:
                return left * right
            elif node.op.tipo == TipoToken.DIV:
                return left / right

        elif isinstance(node, VarDeclNode):
            self.env[node.name] = self.visit(node.value)

        elif isinstance(node, AssignNode):
            self.env[node.name] = self.visit(node.value)

        elif isinstance(node, OutputNode):
            print(self.visit(node.expr))

        elif isinstance(node, IfNode):
            if self.visit(node.condition):
                self.visit(node.then_block)
            elif node.else_block:
                self.visit(node.else_block)
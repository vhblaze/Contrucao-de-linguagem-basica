from operator import index
from platform import node
from turtle import left, right
from errors import RuntimeErrorCustom
from lexico import TipoToken
from ast_nodes import *

class Interpreter:
    def __init__(self):
        self.env = {}
        self.contador = 0
    
    def visit(self, node):

        if isinstance(node, BlockNode):
            for stmt in node.statements:
                self.visit(stmt)

        elif isinstance(node, NumberNode):
            return node.value

        elif isinstance(node, VarNode):
            if node.name not in self.env:
                raise RuntimeErrorCustom(f"Variável '{node.name}' não definida")
            return self.env[node.name]
        
        elif isinstance(node, CallNode):

            if node.name == "contador":
                self.contador += 1
                return self.contador

            else:
                raise RuntimeErrorCustom(f"Função '{node.name}' não definida")
        
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
                raise RuntimeErrorCustom(f"Operador não suportado: {op}")
            
        elif isinstance(node, VarDeclNode):
            value = self.visit(node.value)
            self.env[node.name] = value
        elif isinstance(node, WhileNode):
            while self.visit(node.condition):
                self.visit(node.block)
        
        elif isinstance(node, IndexNode):
            lista = self.visit(node.list_node)
            index = self.visit(node.index)

            try:
                return lista[index]
            except Exception:
                raise RuntimeErrorCustom("Erro ao acessar índice da lista")   
    
        elif isinstance(node, AssignNode):
            if node.name not in self.env:
                raise RuntimeErrorCustom(f"Variável '{node.name}' não definida")
            value = self.visit(node.value)
            self.env[node.name] = value

        elif isinstance(node, OutputNode):
            value = self.visit(node.expr)
            print(value)
        elif isinstance(node, ListNode):
            return [self.visit(element) for element in node.elements]
         
        elif isinstance(node, IfNode):
            condition = self.visit(node.condition)

            if condition:
                self.visit(node.then_block)
            elif node.else_block:
                self.visit(node.else_block)
        elif isinstance(node, UnaryOpNode):
            value = self.visit(node.expr)

            if node.op.tipo == TipoToken.NOT:
                return not value
        else:
            raise RuntimeErrorCustom(f"Nó desconhecido: {node}")
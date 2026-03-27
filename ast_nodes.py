class NumberNode:
    def __init__(self, value):
        self.value = value


class VarNode:
    def __init__(self, name):
        self.name = name


class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class VarDeclNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class AssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class OutputNode:
    def __init__(self, expr):
        self.expr = expr


class IfNode:
    def __init__(self, condition, then_block, else_block):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block


class BlockNode:
    def __init__(self, statements):
        self.statements = statements
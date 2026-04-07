# 🔥 Linguagem Blaze - README

Este documento descreve todas as evoluções e implementações realizadas na linguagem ao longo do desenvolvimento.

---

# 📌 1. Estrutura Inicial

A linguagem foi construída com:

* Lexer (`lexico.py`)
* Errors (`errors.py`)
* Parser (`parser_1.py`)
* AST (`ast_nodes.py`)
* Interpreter (`interpreter.py`)
* Execução (`main.py`)

---

# 🧱 2. Variáveis e Operações

## Exemplo:

```blaze
catchmon x = 10;
catchmon y = 5;
dexout x + y;
```

Suporte a:

* Soma, subtração, multiplicação, divisão
* Comparações (`>`, `<`, `==`, etc)

---

# 🧠 3. Estruturas Condicionais

## Sintaxe inicial:

```blaze
ifmon (x > 5) {
    dexout x;
} elsemon {
    dexout 0;
}
```

## Evolução com `entao`:

```blaze
ifmon (x > 5) entao {
    dexout x;
} elsemon {
    dexout 0;
}
```

### Alterações:

* Novo token `ENTAO`
* Parser atualizado:

```python
self._expect(TipoToken.ENTAO)
```

---

# 📦 4. Listas

## Criação:

```blaze
catchmon x = [10, 20, 30];
```

## AST:

```python
class ListNode:
    def __init__(self, elements):
        self.elements = elements
```

## Interpreter:

```python
elif isinstance(node, ListNode):
    return [self.visit(e) for e in node.elements]
```

---

# 🔢 5. Acesso por Índice

## Exemplo:

```blaze
dexout x[1];
```

## AST:

```python
class IndexNode:
    def __init__(self, list_node, index):
        self.list_node = list_node
        self.index = index
```

## Parser:

```python
while self._current().tipo == TipoToken.LBARRA:
    self._advance()
    index = self._parse_expression()
    self._expect(TipoToken.RBARRA)
    node = IndexNode(node, index)
```

## Interpreter:

```python
elif isinstance(node, IndexNode):
    lista = self.visit(node.list_node)
    index = self.visit(node.index)

    if not isinstance(lista, list):
        raise RuntimeErrorCustom("Não é uma lista")

    if not isinstance(index, int):
        raise RuntimeErrorCustom("Índice inválido")

    if index < 0 or index >= len(lista):
        raise RuntimeErrorCustom("Índice fora do limite")

    return lista[index]
```

---

# ⚠️ 6. Tratamento de Erros

## Tipos criados:

```python
class LexicalError(Exception): pass
class SyntaxErrorCustom(Exception): pass
class RuntimeErrorCustom(Exception): pass
```

## Uso no main:

```python
try:
    ...
except LexicalError as e:
    print(e)
except SyntaxErrorCustom as e:
    print(e)
except RuntimeErrorCustom as e:
    print(e)
```

---

# 🔁 7. Função Contador (estado persistente)

## Objetivo:

```blaze
dexout contador();
dexout contador();
dexout contador();
```

## Saída:

```
1
2
3
```

---

## AST:

```python
class CallNode:
    def __init__(self, name, args):
        self.name = name
        self.args = args
```

---

## Parser:

```python
if self._current().tipo == TipoToken.LPAREN:
    self._advance()
    args = []
    if self._current().tipo != TipoToken.RPAREN:
        args.append(self._parse_expression())
    self._expect(TipoToken.RPAREN)
    return CallNode(token.valor, args)
```

---

## Interpreter:

```python
self.contador = 0

elif isinstance(node, CallNode):
    if node.name == "contador":
        self.contador += 1
        return self.contador
```

---

# 🧪 8. Execução via arquivo

## main.py:

```python
python main.py arquivo.blaze
```

---

# 🚀 9. Estado Atual da Linguagem

## Suporta:

* Variáveis
* Operações matemáticas
* Condicionais (`ifmon`)
* Listas
* Indexação
* Funções nativas (`contador()`)
* Tratamento de erros

---

# 🔥 Próximos passos

* Funções completas (`func`, `return`)
* Loops (`whilemon`, `for`)
* Escopo de variáveis
* Tipagem

---

# 💬 Conclusão

A linguagem evoluiu de um interpretador básico para um sistema com:

* AST estruturada
* Execução dinâmica
* Funções com estado
* Validação de erros

Isso já representa a base de uma linguagem de programação real 🚀
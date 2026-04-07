# 🔥 Linguagem Blaze - README

Este documento descreve todas as evoluções e implementações realizadas na linguagem ao longo do desenvolvimento.

DISCENTE(s): Pedro Ubirajara Santos de Faria - 601015364
Vitor Hugo Neves do Vale Camargos - 601016508


Cada questão está demarcada com os comentários:


#===========================
#Aqui está a questão X, opção Y
#==========================

Na questão 1 escolhemos a opção B  (lista).
O código pode ser conferido na íntegra no arquivo ast_nodes.py 
Linha 33 até 35
O código pode ser conferido na íntegra no arquivo parser_1.py 
Linha 123 até 135
O código pode ser conferido na íntegra no arquivo lexico.py 
Linha 40, 75, 189 até 41, 76, 192
O código pode ser conferido na íntegra no arquivo interpreter.py 
Linha 82 até 89
O arquivo de teste dessa função é teste_lista.blaze
O teste é realizado através do comando no terminal python main.py teste_lista.blaze

Na questão 2 escolhemos a opção A  (novo formato de condicional).
O código pode ser conferido na íntegra no arquivo parser_1.py 
Linha 95 até 110
O código pode ser conferido na íntegra no arquivo interpreter.py 
Linha 103 até 109
O código pode ser conferido na íntegra no arquivo lexico_1.py 
Linha 11, 62  até 13, 64
O código pode ser conferido na íntegra no arquivo ast_nodes.py 
Linha 57 até 61
O arquivo de teste dessa função é teste_if_else.blaze.
O teste é realizado através do comando no terminal python main.py teste_if_else.blaze

Na questão 3 escolhemos a opção A  (função contador).
O código pode ser conferido na íntegra no arquivo  interpreter.py
Linha 11 até 31
O arquivo de teste dessa função é teste_contador.blaze.
O teste é realizado através do comando no terminal python main.py teste_contador.blaze


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
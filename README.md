# 🔥 PythonMon Language

PythonMon é uma mini-linguagem de programação temática inspirada no universo Pokémon, desenvolvida como projeto acadêmico para a disciplina de Compiladores.

---

## 🚀 Como executar

### Pré-requisitos

* Python 3 instalado
* Clonar o repositório:

```bash
git clone https://github.com/vhblaze/Contrucao-de-linguagem-basica.git
cd Contrucao-de-linguagem-basica
```

### ▶️ Executar programa

```bash
python main.py exemplo.blaze
```

---

## 📁 Estrutura do projeto

```
.
├── lexico.py          # Analisador léxico
├── parser.py          # Analisador sintático
├── ast_nodes.py       # Estrutura da AST
├── interpreter.py     # Execução da linguagem
├── main.py            # Arquivo principal
├── teste_erro.blaze
├── teste_if_else.blaze
└── teste_logico.blaze
```

---

## 🧠 Sintaxe da linguagem

### 🔹 Declaração de variável

```
catchmon x = 10;
```

### 🔹 Atribuição

```
x = x + 5;
```

### 🔹 Saída de dados

```
dexout x;
```

### 🔹 Condicional

```
ifmon (x > 10) {
    dexout x;
} elsemon {
    dexout 0;
}
```

---

## ⚙️ Operadores suportados

### Aritméticos

```
+  -  *  /
```

### Relacionais

```
==  !=  >  <  >=  <=
```

---

## 🧪 Exemplo completo

```
catchmon saldo = 1000;
catchmon saque = 300;

saldo = saldo - saque;

ifmon (saldo >= 0) {
    dexout saldo;
} elsemon {
    dexout 0;
}
```

---

## 📜 Gramática (EBNF)

```
program       ::= statement*

statement     ::= declaration
                | assignment
                | if_statement
                | output

declaration   ::= "catchmon" IDENT "=" expression ";"
assignment    ::= IDENT "=" expression ";"

if_statement  ::= "ifmon" "(" expression ")" block ("elsemon" block)?

block         ::= "{" statement* "}"

output        ::= "dexout" expression ";"

expression    ::= comparison

comparison    ::= arithmetic ((">" | "<" | ">=" | "<=" | "==" | "!=") arithmetic)*

arithmetic    ::= term (("+" | "-") term)*

term          ::= factor (("*" | "/") factor)*

factor        ::= NUMBER
                | IDENT
                | "(" expression ")"
```

---

## ⚖️ Precedência e associatividade

Da maior para a menor:

1. Parênteses `()`
2. Multiplicação e divisão `* /`
3. Soma e subtração `+ -`
4. Operadores relacionais `> < >= <= == !=`

**Associatividade:** esquerda para direita

---

## 🧱 Arquitetura

```
Código (.blaze)
   ↓
Lexer (tokens)
   ↓
Parser (AST)
   ↓
Interpreter (execução)
```

---

## ⚠️ Tratamento de erros

* Tokens inválidos geram erro
* Variáveis não definidas geram exceção
* Erros de sintaxe interrompem a execução

### ❌ Exemplo de erro

```
catchmon x = ;
```

Saída esperada:

```
Erro: esperado expressão após '='
```

---

## 🎯 Objetivo acadêmico

* Construção de linguagem de programação
* Análise léxica
* Parsing (análise sintática)
* Construção de AST
* Interpretação de código

---

## 👨‍💻 Autores

Pedro Ubirajara Santos de Faria
Vitor Hugo Neves do Vale Camargos

Projeto acadêmico – Compiladores

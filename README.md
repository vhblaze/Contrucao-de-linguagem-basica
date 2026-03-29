# 🔥 PythonMon

PythonMon é uma mini-linguagem de programação temática inspirada no universo Pokémon, desenvolvida como projeto acadêmico para a disciplina de Compiladores.

---

## 🚀 Como executar

### Pré-requisitos

* Python 3 instalado

### Comando para rodar

```bash
python main.py (nomearquivo.blaze)
```

---

## 📁 Estrutura do projeto

```
.
├── lexico.py
├── parser.py
├── ast_nodes.py
├── interpreter.py
├── main.py
└── exemplo.blaze
```

---

## 🧠 Sintaxe da linguagem

### 🔹 Variáveis

```
catchmon x = 10;
```

### 🔹 Atribuição

```
x = x + 5;
```

### 🔹 Saída

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
+  -  *  /  %
```

### Relacionais

```
==  !=  >  <  >=  <=
```

### Lógicos

```
&&  ||  !
```

---

## 🧪 Exemplo completo

```
catchmon saldo = 1000;
catchmon saque = 300;

saldo = saldo - saque;

ifmon (saldo >= 0 && !(saldo == 0)) {
    dexout saldo;
} elsemon {
    dexout 0;
}
```

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
* Erros de sintaxe interrompem execução

---

## 🎯 Objetivo acadêmico

* Construção de linguagem
* Análise léxica
* Parsing
* AST
* Interpretação

---

## 👨‍💻 Autores

Pedro Ubirajara Santos de Faria
Vitor Hugo Neves Do Vale Camargos 

Projeto acadêmico – Compiladores

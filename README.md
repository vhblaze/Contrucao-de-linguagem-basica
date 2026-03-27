# Mini Linguagem de Programação

## 📌 Sobre o Projeto

Este projeto consiste no desenvolvimento de uma mini-linguagem original, incluindo analisador léxico, parser, AST e execução. A linguagem possui sintaxe própria e foi criada com foco em aprendizado de compiladores.

## ⚙️ Funcionalidades

* Declaração e atribuição de variáveis
* Expressões aritméticas (+, -, *, /, %)
* Operadores relacionais (==, !=, <, <=, >, >=)
* Operadores lógicos
* Estrutura condicional (if/else personalizada)
* Saída de dados
* Tratamento de erros com posição

## 🧱 Estrutura do Projeto

```
/VT-Compiladores
  ├── lexer
  ├── parser
  ├── ast
  └── runtime
```

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone <seu-repo>
```

2. Acesse a pasta:

```bash
cd <seu-repo>
```

3. Execute o programa:

```bash
python main.py exemplo.nl
```

## 📄 Exemplo de Código

```
var x = 10;
if (x > 5) {
  output x;
} else {
  output 0;
}
```

## 👥 Equipe

* Vitor Hugo Neves Do Vale Camargos
* Pedro Ubirajara Santos de Faria

## 📎 Observações

Projeto desenvolvido para a disciplina de CONSTRUÇÃO DE INTERPRETADORES E COMPILADORES.
Professor: Jair Neto

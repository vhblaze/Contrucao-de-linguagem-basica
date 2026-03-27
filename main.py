from lexico import AnalisadorLexico

codigo = """
catchmon pikachu = 50;
catchmon charizard = 100;

~~ isso é um comentário

ifmon (pikachu < charizard) {
    dexout pikachu;
} elsemon {
    dexout charizard;
}
"""

lexer = AnalisadorLexico(codigo)
tokens = lexer.analisar()

for token in tokens:
    print(token)
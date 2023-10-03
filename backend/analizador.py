# Analisador lexico para linguagem de expressoes de primeiro grau

# Crétitos autor original
# Andrei de Araujo Formiga, 2014-07-25

# Modificado por:
# Alan Marinho - Github: @alanmarinho 03-10-2023

import re

# variaveis globais
codigo = ""
posicao = 0
tamanho = 0

# constantes para valores de operadores
SOMA = "SOMA"
SUB = "SUBITRAÇÃO"
MULT = "MULTIPLICAÇÃO"
DIV = "DIVISÃO"

# constantes para tipo de token
TOK_NUM = "NÚMERO"
TOK_OP = "OPERADOR"
TOK_IGUALDADE = "IGUALDADE"
TOK_VAL = "VARIÁVEL"

# Operadores validos
operadores = "+-*/"


# Estrutura de um token
class Token:
    def __init__(self, token, tipo, valor):
        self.token = token
        self.tipo = tipo
        self.valor = valor


# le um caractere do codigo e retorna o caractere ou -1 se o fim do codigo foi alcancado
# incrementa a variavel posicao
def le_caractere():
    global codigo, posicao, tamanho
    c = ""

    if posicao < tamanho:
        c = codigo[posicao]
        posicao += 1
    else:
        posicao += 1
    return c


# determina se um caractere eh um operador, e retorna o tipo se for, se nao retorna -1
def define_operador(operador):
    switch = {"+": SOMA, "-": SUB, "*": MULT, "/": DIV}

    return switch.get(operador, "NENHUM")


# funcao que faz a analise lexica, retornando o proximo token
def proximo_token():
    global posicao
    c = le_caractere()
    valor = ""

    if posicao > tamanho:
        return None

    while c.isspace():
        c = le_caractere()

    if c.isdigit():
        while c.isdigit():
            valor += c
            c = le_caractere()
        posicao -= 1

        return Token(valor, TOK_NUM, int(valor))
    elif c in operadores:
        return Token(c, TOK_OP, define_operador(c))
    elif c == "=":
        return Token(c, TOK_IGUALDADE, "IGUALDADE")
    elif re.search(r"[a-zA-Z]", c):
        while re.search(r"[a-zA-Z0-9]", c):
            valor += c
            c = le_caractere()
          
        return Token(valor, TOK_VAL, valor)
    else:
        return None


# inicializa a analise lexica do codigo em uma string (preeche as variaveis globais)
def inicializa_analise(entrada):
    global codigo, posicao, tamanho
    codigo = entrada
    tamanho = len(entrada)
    posicao = 0


# executa o nalizador lexico
def analisador_lexico(entrada):
    inicializa_analise(entrada)
    tokens = []
    while True:
        tok = proximo_token()
        if tok is None:
            break
        tokens.append(tok)

    tokens_JSON = []
    for token in tokens:
        tokens_JSON.append({
            "token": token.token,
            "tipo": token.tipo,
            "valor": token.valor
        })
    
    return tokens_JSON









# entrada = '1 + a1a87a67a6 69= 0'
# tokens = analisador_lexico(entrada)
# print("Tokens: ", tokens)
# for i in tokens:
#     print(i.token, i.tipo, i.valor)
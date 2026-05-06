# AULA COMPLETA: NUMEROS EM PYTHON
"""
Vamos aprender:
1 - Tipos numéricos
2 - Conversão de tipos
3 - Hierarquia numérica
4 - Operações matemáticas
5 - Coerção de ipos 
6 - Verificação d etipos
7 - Entrada de dados
"""
# ===========================
# PASSO 01 - TIPOS NUMÉRICOS
# ===========================
# int -> números inteiros 
# float -> números com casas decimais 
# complex -> números complexos (usado em matemática/engenharia)

print("====TIPOS ====")

# EXEMPLO 01 - NUMERO INTEIRO

# criamos uma variável chamada numero_inteiro
numero_inteiro = 10

# Mostramos o valor 
print ("Valor:", numero_inteiro)

# Type() mostra qual é o tipo da variável
print("Tipo:", type(numero_inteiro))

print("--------------------------------")

# EXEMPLO 02 - NUMERO DECIMAL

# Float é um número com ponto decimal
numero_decimal = 3.14

print ("Valor:", numero_decimal)
print ("Tipo:", type(numero_decimal))

print("-----------------------------")

# EXEMPLO 03 - NUMEROS COMPLEXOS
# Um número complexo possui duas partes:
# Parte real (Numero normal)
# Parte Imaginária (multiplicada por j)

# Estrutura Geral:
# numero = a = bj

# a = parte real
# b = parte imaginária
# j = unidade imaginária

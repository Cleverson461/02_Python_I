game_name = 'Fifa 23'
game_description = """
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
"""

# string[inicio:fim] - indice começa na posição 0 | indice final -1

# 1 - busque toda string a partir da primeira posição
print(game_name[0:])

# 2 - busque toda string até a última posição
print(game_name[:7])

# 3 - busque toda string da terceira até a última posição
print(game_name[2:])

"""
string[inicio:fim:passo] - indice começa na posição 0 | indice final -1 passo - determina o incremento. Por padrão esse número é o 1 
"""

# 4 - busque toda a string de 2 em 2 caracteres
print(game_name[::2])

# 5 - busque toda a string nos indices impares
print(game_name[1::2])

# 6 - Inverter uma string de trás para frente
print(game_name[::-1])
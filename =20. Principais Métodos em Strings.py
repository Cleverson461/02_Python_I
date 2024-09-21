game_name = 'Fifa 23'
game_description = """
Fifa 23 é um jogo de futebol,
desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online
"""

print(game_name.upper()) # Retornar string em maiúsculo
print(game_name.lower()) # Retornar string em minúsculo
print(game_name.capitalize()) # Apenaas a primeira letra em maiúsculo
print(game_name.title()) # Apenas a primeira letra em maiúsculo
print(game_name.center(11, '-')) # Retorna a string centralizada com caractere de preenchimento
print(game_name.find('i')) # Retorna a posíção de um determinado caractere
print(game_description.count('f')) # conta caracteres
print(game_description.count('a')) # conta caracteres
print(game_name.replace('Fifa', 'Pes')) # Altera um elemento por outro
print(game_description.split(','))
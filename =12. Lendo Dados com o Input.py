# Utilizando o Input
""" 
Comentário de multi linha

JogoTeca
"""

name = input('Digite o nome do jogo: ')
year_launch = int(input('Digite o ano de lançamento do jogo: '))
game_price = float(input('Digite o preço do jogo: '))
plan_included = input('Está incluso no serviço mensal? ')

print(f'Nome do jogo: {name}')
print(f'O ano do jogo é {year_launch}')
print(f'O preço do jogo é {game_price}')
print(f'Ele está incluso no serviço mensal? {plan_included}')

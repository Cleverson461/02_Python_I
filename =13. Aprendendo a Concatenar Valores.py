name = input('Digite o nome do jogo: ')
year_launch = int(input('Digite o ano de lançamento do jogo: '))
game_price = float(input('Digite o preço do jogo: '))
plan_included = input('Está incluso no serviço mensal? ')

print('### Dados do Jogo ###')
print(10 * '=')

# Alternativa 1
""" print('Nome do Jogo: ', name)
print('Ano do Jogo: ', year_launch)
print('Preço do Jogo: ', game_price)
print('Está incluso no plano? ', plan_included) """

# Alternativa 2
""" print('Nome do Jogo:', name, '\n Ano de lançamento:', year_launch, '\n Preço do Jogo:', game_price, '\n Esrá incluso no serviço?', plan_included) """

# Alternativa 3
print(f'Nome do Jogo: {name}')
print(f'Ano do Jogo: {year_launch}')
print(f'Preço do Jogo: {game_price}')
print(f'Está incluído no plano? {plan_included}')
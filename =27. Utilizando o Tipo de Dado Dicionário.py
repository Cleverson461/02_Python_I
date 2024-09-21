game_fifa = {
    'name': 'Fifa 23',
    'yearLaunch': 2022,
    'game_price': 90.50,
    'classification': 8.5,
    'genre': ['esporte', 'familia']
}

print(game_fifa)
print(len(game_fifa))
print(type(game_fifa))

# 1 - Recuperar um elemento dicionario
print('======= 1 ========')
print(game_fifa['genre'])
print(game_fifa.get('classification'))
print()

# 2 - Buscar apenas as chaves do dicionario
print('======= 2 ========')
print(game_fifa.keys())
print()

# 3 - Buscar apenas os valores do dicionario
print('======== 3 ========')
print(game_fifa.values())
print()

# 4 - Buscar itens do dicionario com chave e valor
print('======= 4 ========')
print(game_fifa.items())
print()

# 5 - Adicionar itens no dicionario
print('======= 5 ========')
game_fifa['players'] = 2
print(game_fifa)
print()

# 6 - Atualizar itens do dicionario
print('======= 6 ========')
game_fifa.update({'players': 1})
print(game_fifa)
print()

# 7 - Remover item no dicionario
print('======= 7 ========')
game_fifa.pop('players')
print(game_fifa)
print()
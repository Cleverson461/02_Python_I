game_tuple = ('Fifa23', 'Red Dead 2', 'Star Wars','Mario Odyssey', 'The Legend of Zelda', )

print(game_tuple)
print(type(game_tuple))

# name = ('Rogrigo',)
# print(type(name))

# - Não posibilita adicionar valores na tupla
# - Não posibilita remover valores na tupla
# - Não posibilita ordenar valores na tupla

# 1 - Buscar os odis primeiros itens da tupla
print(game_tuple[:2])

# 2 - Buscar o último item da tupla
print(game_tuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(game_tuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(game_tuple[2:])

# 5 - Recuperar um item da tupla pelo índice
print(game_tuple.index('Red Dead 2'))
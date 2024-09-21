game_list = ['Resident Evil 4', 'Star Wars Jedi Survivor', 'The Legend of Zelda', 'Red Dead 2', 'Mario Odyssey', 'Luigis Mansion 3']

# 1 - Tamanho da lista
print(len(game_list))

# 2 - Recuperar um item da lista pelo índice
print(game_list.index('Mario Odyssey'))

# 3 - Adicionar item ao final da lista
game_list.append('Gta V')
print(game_list)

# 4 - Ordenar a lista 
game_list.sort()
print(game_list)

# 5 - Copiar os itens de uma lista para outra
game_reset = game_list.copy()
game_reset.remove('Star Wars Jedi Survivor')
print(game_reset)

# 6 - Remove todos os itens da lista
game_list.clear()
print(game_list)
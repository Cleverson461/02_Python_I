game_list = ['Fifa', 'God of War', 'Red Dead 2', 'Uncharted', 90.50]

# 1 - Iterando valores de uma lista
for game in game_list:
    print(game) # O laço de repetição for percorre a lista de jogos e imprime cada um deles.
print(20 * '-')
    
# 2 - Quando a condição for atendida, o loop será encerrado
for game in game_list:
    if game == 'Red Dead 2':
        break
    print(game)
print(20 * '-')

# - 3 Quando a condiçào for atendida, o loop vai para a proxima iteração
for game in game_list:
    if game == 'Red Dead 2':
        continue
    print(game)
print(20 * '-')
    
# 4 - Avaliação do Jogo
game_name = input('Digite o nome do jogo: ')
game_rating = int(input('Digite quantas avaliações deseja fazer no jogo: '))

sum = 0
for i in range(game_rating):
    note = float(input(f'Digite a {i+1}ª nota: '))
    sum += note

print(f'A média de avaliação do jogo {game_name} é {sum / game_rating}')
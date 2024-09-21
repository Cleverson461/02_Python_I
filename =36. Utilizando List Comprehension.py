# 1 - Liste valores de 0 a 10 que sejam menor do que 4
for i in range(11):
    if i < 4:
        print(i)

list_numbers = [i for i in range(11) if i < 4]
print(list_numbers)

game_list = ['Mario Odyssey', 'Dk Country', 'Luigis Mansion', 'Kirby']

# 2 - Jogos que possuam a letra a
new_list = [x for x in game_list if 'a' in x]
print(new_list)

# 3 - Jogos que eu zerei
games_finished = [x for x in game_list if x != 'Kirby']
print(games_finished)
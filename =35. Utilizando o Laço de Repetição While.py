game_name = input("Digite o nome do jogo: ")
qtde_rating = 0
total_rating = 0
rating = 0
average = 0

while rating != -1:
    rating = float(input('Informe a nota do jogo: '))
    if(rating != -1):
        total_rating += rating # total_rating = total_rating + rating
        qtde_rating += 1 # qtde_rating = qtde_rating + 1
        average = total_rating / qtde_rating

print(f'Média das avaliações do jogo {game_name} é {average:.2f}')
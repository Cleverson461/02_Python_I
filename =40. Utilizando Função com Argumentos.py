# 1 - Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome
def full_name(fname, lname):
    print(f'Nome completo: {fname} {lname}')
    
full_name("João", "Silva")

# 2 - Crie uma função que some dois numeros via parametros
def sum(a, b):
    return a + b

print(sum(10, 20))

# 3 - Argurmentos default numa função
def address(country='Brsil'):
    print(f'Eu moro no {country}')


address('Brasil')
address('Portugal')
address('EUA')

# 4 - Avaliação do jogo
def rating_game(qtde_rating):
    game_name = input('Digite o nome do jogo: ')
    sum = 0
    for i in range(qtde_rating):
        note = float(input('Digite a nota para o jogo: '))
        sum += note
    print(f'A média de avaliação para o jogo {game_name} é {sum/qtde_rating}')
rating = int(input('Digite quantas avalioçoes deseja fazer no jogo '))

rating_game(rating)
rating_game(rating)
rating_game(rating)
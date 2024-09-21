def wellcome():
    print('Hello World!')
    
wellcome()

# 2 - Função para somar dois números
def sum():
    # print(5 + 4)
    return 5 + 2
 
print(sum())

# 3 - Função para cadastrar um jogo
def create_game():
    print('Cadastrando um jogo')
    name = input('Digite o nome do jogo: ')
    year_launch = int(input('Digite o ano de lançamento: '))
    game_price = float(input('Digite o preço do jogo: '))
    note_rating = float(input('Digite a nota de avaliação do jogo: '))
    
    print(f'{name} - R${game_price:.2f} - {year_launch} - {note_rating}')

create_game()

name = input('Digite o nome do jogo? ')
year_launch = int(input('Digite o ano de lançamento do jogo? '))
classification = float(input('Digite a nota de classificação do jogo? '))

if classification > 8.0 and year_launch > 2015:
    print(f'O jogo {name} é bom. Recomendamos jogá-lo.')
else:
    print(f'O jogo {name} ainda não atingiu uma boa nota. Não recomendamos jogá-lo.')
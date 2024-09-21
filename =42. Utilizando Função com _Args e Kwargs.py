""" 
    *args -> Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função.
     - Os argumentos sào passados como um tupla
     
    **kwargs -> Além dos valores podemos passar também as respectivas chaves para cada argumento. 
     - Os argumentos são passados como um dicionário.
"""

# 1 - Soma de numeros
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f'Soma é: {sum_total}')
    
sum(7)
sum(7, 9)
sum(7, 9, 10, 11)
sum(7, 10, 9, 8, 7, 6)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f'{key} - {value}')


print('===== Dados do Curso =====')
presentation(nome='Python', category='Backend', level='Iniciante', carga_horaria=40, preco=299.99, )
presentation(nome='Visão Computacional com Python', category='IA', level='Avançado', carga_horaria=40, preco=299.99, )
presentation(nome='Dashboards com Dash', category='Data Science', level='Intermediário', carga_horaria=40, preco=299.99, )
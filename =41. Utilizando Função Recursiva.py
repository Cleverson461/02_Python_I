""" 
    Fatorial de um número:
    3! = 3 * 2 * 1 = 6
    5! = 5 * 4 * 3 * 2 * 1 = 120
"""

# 1 - Fatorial de um número
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))
    
number = int(input('Digite o número para o fatorial: '))
print(f'O fatorial de {number} é {factorial(number)}')

# 2 - Soma total de um número
""" 
    1 = 1 + 0
    5 = 5 + 4 + 3 + 2 + 1 = 15
    3 = 3 + 2 + 1 = 6
"""
def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))
    
num = int(input('Digite um número para soma: '))
print(f'A soma total de {num} é: {total_sum(num)}')
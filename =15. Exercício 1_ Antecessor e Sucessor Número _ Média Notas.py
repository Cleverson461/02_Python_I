""" 
    Exercicio 1:
    # Antecessor e Sucessor de um número:
    -> Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizado operadores de atribuição.
    
    # Média de 4 notas;
    -> Escreva um programa em Python que leia quatro números e calcule a média entre esse números
"""
# exercicio 1
numero = int(input('Digite um numero: '))

print(f'O numero antecessor de {numero} é {numero - 1}')
print(f'O numero sucessor de {numero} é {numero + 1}')

# exercicio 2

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))
num4 = float(input('Digite o quarto numero: '))

media = (num1 + num2 + num3 + num4) / 4

print(f'A media dos numeros {num1}, {num2}, {num3} e {num4} é {media}')
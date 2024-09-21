""" 
Exercicio 4:
* Contagem Regressiva:
-> Faça um programa para escrever a contagem repressiva do lançamento de um foquete.
O Programa deve imprimir 10, 9, 8, ..., 1, 0 e disparar um 'beep'

* Tabuada:
-> Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário.
"""
# for foquete in range(10,0,-1):
#     print(foquete)

# import winsound
# x = 10
# while x >= 0:
#     print(x)
#     x -= 1 # x = x - 1
# winsound.Beep(2500, 500)
    

number = int(input('Tabuada de: '))
begin = int(input('De: '))
end = int(input('Até: '))

x = begin

while x <= end:
    print(f'Tabuada de {number} X {x} = {number * x}')
    x += 1

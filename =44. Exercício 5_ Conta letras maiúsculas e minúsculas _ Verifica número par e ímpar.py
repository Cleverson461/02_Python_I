""" 
## Conta letras maiúsculas e minúsculas
    Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

## Lista números pares e ímpares de uma lista
    Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.

"""

def conta_letras(string):
    maiusculas = 0
    minusculas = 0
    for letra in string:
        if letra.isupper():
            maiusculas += 1
        elif letra.islower():
            minusculas += 1
    print(f'Texto original: {string}')
    print(f'Letras maiúsculas: {maiusculas}')
    print(f'Letras minúsculas: {minusculas}')

conta_letras('A Melhor Forma De Prever o Futuro é Cria-lo.')
conta_letras('Python é uma linguagem de programação')

print( )
print(25 * '-')
print( )

def lista_pares_impares(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

print(lista_pares_impares([1, 2, 4, 6, 5, 7, 11, 20, 13]))
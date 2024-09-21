# 1 - Função de potencia de numero
power = lambda num: num ** 2

# 2 - Função para verificar se é par
pair = lambda x: x % 2 == 0

# 3 - Função que divide um número por outro
div_num = lambda a, b: a / b

# 4 - Função que inverte um string
reverse = lambda s: s[::-1]


# Exemplo de uso das funções
print(power(5))
print(power(9))

print( )
print(10 * '-')
print( )

print(pair(30))

print( )
print(10 * '-')
print( )

print(div_num(10, 2))
print(div_num(6, 2))

print( )
print(10 * '-')
print( )

print(reverse('Python'))
print(reverse('Curso de Python'))
print(reverse('Javascript'))
""" 
Exercício 2
## Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

Ex:
fifa 23 → **fi#a 23**

restart→ resta#t

## Substituindo caractere repetido

Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:

abc xyz → **xyc abz** """

# Substituindo caractere repetido
name = input('Digite o nome do jogo: ')
char = name[0].lower()
new_name = name.replace(char, '$')
new_name = char + new_name[1:]

print(new_name)


# Troca de caracteres
st1 = 'abc'
st2 = 'xyz'

new_str1 = st2[:2] + st1[2:]
new_str2 = st1[:2] + st1[2:]
print(new_str1)
print(new_str2)
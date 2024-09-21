num1 = float(input('Digite o número 1:'))
num2 = float(input('Digite o número 2:'))
operation = input('Digite a operação a realizar (+, -, *, /): ')

if operation == '+':
    print(f'A soma de {num1} + {num2} é igual a {num1 + num2:.2f}')
elif operation == '-':
    print(f'A subtração de {num1} - {num2} é igual a {num1 - num2:.2f}')
elif operation == '*': 
    print(f'A multiplicação de {num1} * {num2} é igual a {num1 * num2:.2f}')
elif operation == '/':
    print(f'A divisão de {num1} / {num2} é igual a {num1 / num2:.2f}')
else:
    print('Operação inválida')
    result = 0
    print(result)
# O programa pede dois números e uma operação, e executa a operação escolhida.
# Se a operação for inválida, ele imprime uma mensagem de erro.

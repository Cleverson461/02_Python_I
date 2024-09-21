""" 
    Exercicio 3:
    
    * Cálculo da Distância:
    -> Escreva um programa que pergunte a distancia que um passageiro deseja percorrer em km.
    Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200 km e R$0,35 para viagens mais longas.
    
    * Aumento salario funcionario:
    -> Escreva um programa que pergunte o salario do funcionario e calcule o valor do aumento.
    Para salarios superiores a R$ 1.2500,00 calcule um aumento de 10%. 
    Para os inferiores ou iguais, de 15%.
"""

# Calculo da Distância:
distancia_km = float(input("Digite a distancia em km: "))

if distancia_km <= 200:
    valor_passagem = distancia_km * 0.50
    print(f"O valor da passagem é: R${valor_passagem:.2f}")
else:
    valor_passagem = distancia_km * 0.35
    print(f"O valor da passagem é: R${valor_passagem:.2f}")

# =======================================
print(20 * '=')

# Aumenrto de Salário do Funcionário:
salario_funcionario = float(input("Digite o salario do funcionario: "))

if salario_funcionario > 1250.00:
    aumento = salario_funcionario * 0.10
    salario_funcionario = salario_funcionario + aumento
    print(f"O salario do funcionario com aumento é: R${salario_funcionario:.2f}, o aumento será de {aumento:.2f}")
elif salario_funcionario <= 1250.00:
    aumento = salario_funcionario * 0.15
    salario_funcionario = salario_funcionario + aumento
    print(f"O salario do funcionario com aumento é: R${salario_funcionario:.2f}, o aumento será de {aumento:.2f}")
    
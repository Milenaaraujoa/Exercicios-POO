# 1. Crie um programa que receba o salário de um empregado e o percentual de 
# aumento, calcule e mostre o valor do aumento e o novo salário. 

salario = float(input("Digite o valor do seu salário:  "))
percentual = float(input("Digite o percentual de aumento: "))


aumento = salario * percentual /100

novo_salario = salario + aumento 

print(f'O valor do aumento é de {aumento} e seu novo salário é de R${novo_salario}')




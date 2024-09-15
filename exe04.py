# 4. Crie um programa que calcule o valor total a ser pago em uma conta de restaurante, 
# considerando o valor da refeição e uma taxa de serviço. 

refeicao = float(input("Digite o valor da refeição: "))

taxa_servico = float(input("Digite o da taxa de serviço: ")) 

taxa = refeicao * taxa_servico / 100

total = refeicao + taxa

print(f'O valor total a ser pago é de {total}')


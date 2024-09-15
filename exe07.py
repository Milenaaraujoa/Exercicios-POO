# Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. 
# Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 
# 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário 
# total. 


salario_fixo = float(input("Digite seu salário fixo: "))
vendas = float(input("Digite o valor das vendas efetuadas: "))

if vendas <= 1500:
    comissao = 0.03 * vendas

    
else:
    comissao = 0.03 * 1500 + 0.05 *(vendas - 1500)


salario_total = salario_fixo + comissao

print(f'O salário total é de {salario_total}')
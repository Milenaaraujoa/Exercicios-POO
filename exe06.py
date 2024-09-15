# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que 
# trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular 
# com um acréscimo de 50%. Escreva um algoritmo/programa que leia o número de 
# horas trabalhadas em um mês, o salário por hora e escreva o salário total do 
# funcionário, que deverá ser acrescido das horas extras, e caso tenham sido 
# trabalhadas. 
# (Considere que o mês possua 4 semanas exatas).

horas_normais = 160

horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
salario_hora = float(input("Digite o salário que ganha por hora: "))


if horas_trabalhadas > horas_normais:
    
    hora_extra = horas_trabalhadas - horas_normais
    salario_base = salario_hora  * horas_normais
    salario_extra = hora_extra * (salario_hora *1.5)
    salario_total = salario_extra + salario_base

else:
    salario_total = salario_hora * horas_normais
    
    
print(f'Seu salário total é de R${salario_total}')
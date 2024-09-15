# 30. Escrever um algoritmo/programa que leia um valor digitado pelo usuário e mostre 
# a tabuada deste número de 1 até 10. 


n = int(input("Digite um valor: "))

for i in range(1, 11):
    print(f'{n} * {i} = {n * i}')
    
# 16. Crie um programa que leia uma sequência de números inteiros e exiba apenas os 
# números pares. 

num_par = 0
sequencia = []
while True:  
    n = int(input("Digite um número inteiro ou zero para sair: "))

    if n == 0: 
        break

    if n % 2 == 0:
        sequencia.append(n)


print(f'Números pares: {sequencia}')



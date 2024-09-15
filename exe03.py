# 3. Faça um programa que leia um caractere e indique se é uma vogal ou consoante.

caractere = input("Digite uma caractere: ")

if caractere in 'aeiou':
    print("É vogal")
    
else:
    print('É consoante')
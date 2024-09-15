# 26. Escrever um algoritmo/programa que lê 10 valores e mostra a média dos valores 
# lidos. 

contagem = 0

for i in range(3):
    n = int(input("Digite 10 valores: "))
    contagem +=n; 
    
media = contagem / 3

print(f"A média é de {media}")
# 24. Escrever um algoritmo/programa que lê 20 valores e mostra quantos destes valores 
# são maiores ou iguais a 5. 


contagem = 0

for i in range (20):
    n = int(input("Digite um número: "))
    
    if n >= 5:
        contagem += 1
        
print(f'Quantidades de números maiores ou iguais a 5: {contagem}')
    
    
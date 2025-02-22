# URI.1173 - Preenchimento de Vetor I
# Python
# Praticando listas

# criar um vetor N com 10 posições
vetor = [0] * 10

# a primeira posição do vetor vai ser o valor do input
valor = int(input())
vetor[0] = valor

# para as outras posição, preenche de acordo com a formula abaixo
for i in range (1, 10):
    vetor[i] = vetor[i - 1] * 2 
    
# print 
for i in range (10): 
    print(f"N[{i}] = {vetor[i]}")

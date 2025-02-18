#URI.1066 - Pares, Ímpares, Positivos e Negativos

conta_par = 0
conta_impar = 0
conta_positivo = 0
conta_negativo = 0

for i in range(5):
    number = float(input())
    if (number % 2 == 0):
        conta_par = conta_par+1
    else: 
        conta_impar = conta_impar+1
    if number>0:
        conta_positivo = conta_positivo+1
    elif number<0: 
        conta_negativo = conta_negativo+1
        
print(f"{conta_par} valor(es) par(es)")
print(f"{conta_impar} valor(es) impar(es)")
print(f"{conta_positivo} valor(es) positivo(s)")
print(f"{conta_negativo} valor(es) negativo(s)")

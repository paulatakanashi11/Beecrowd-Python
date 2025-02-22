# URI.1174 - Seleçao em Vetor I

# declarando o vetor
A = []

# ler os 100 numeros 
for i in range(100):
    valor = float(input())
    A.append(valor)

# ler o numero e ver se é <= 10
for i in range(100):
    if A[i] <= 10:
        print(f"A[{i}] = {A[i]:.1f}")

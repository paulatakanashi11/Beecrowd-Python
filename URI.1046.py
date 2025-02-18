#URI 1046 - Tempo de jogo 

#inicio, fim = map(int(input().split()))
inicio, fim = map(int, input().split())


if inicio == fim:
    print("O JOGO DUROU 24 HORA (S)")
elif inicio > fim:
    print(f"O JOGO DUROU {(24 - inicio) + fim} HORA (S)")
else: 
    print(f"O JOGO DUROU {fim - inicio} HORA (S)")



"""
Errado: 
inicio, fim = map(int(input().split()))
Isso causa erro de sintaxe porque você está tentando passar a lista retornada por split() diretamente para int() dentro de map(), o que não é válido.

Correto: 
inicio, fim = map(int, input().split())
Isso usa map() corretamente para aplicar int() a cada elemento da lista gerada por split(), resultando em dois números inteiros atribuídos às variáveis inicio e fim.
"""

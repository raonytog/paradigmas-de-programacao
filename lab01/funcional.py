def head(lista):
    if lista == []: return []
    if lista == '': return ''
    return lista[0]
    
def tail(lista):
    if lista == []: return []
    if lista == '': return ''
    return lista[1:]
    
def init(lista):
    if lista == []: return []
    if lista == '': return ''
    return lista[:-1]
    
def last(lista):
    if lista == []: return []
    if lista == '': return ''
    return lista[-1]

# 1) Ler um número n e imprimer todos os números pares de 1 até n.
def pares_aux(n, i):
    if n < i: return []
    if i%2 == 0: return [i] + pares_aux(n, i+1)
    else: return pares_aux(n, i+1)

def pares(n):
    return pares_aux(n, 1)

# 2) Ler uma string e contar quantas vogais ela contém.
def qtd_vogais(string):
    if string == '': return 0
    if head(string) in "aeiou": return 1+qtd_vogais(tail(string))
    else: return qtd_vogais(tail(string))

# 3) Ler 5 números, armazenar em uma lista e ordenar usando apenas estruturas de repetição (sem sort() ou funções prontas). Utilize o algoritmo de ordenação que você preferir


# 4) Ler um número inteiro e calcular a soma de seus dígitos

# 5) Ler um número n e imprimir sua tabuada de 1 a 10.

# 6) Ler 10 números e mostrar o maior e o menor sem usar max() nem min().

# 7) Ler um número n e fazer uma contagem regressiva até 0, mostrando "FIM!" ao terminar

# 8) Ler uma temperatura em Celsius e converter para Fahrenheit e Kelvin

# 9) Ler uma matriz 3x3 de números inteiros e imprimir sua transposta.
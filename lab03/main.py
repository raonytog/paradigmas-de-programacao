
# 1 Escreva uma função ‘head’ que retorna o primeiro elemento de uma lista
def head(list):
    if list == [] or list == '': return []
    else: return list[0]

# 2 Escreva uma função ‘tail’ que retorna toda a lista, exceto o primeiro elemento
def tail(list):
    if list == [] or list == '': return []
    else: return list[1:]
    

# 3 Escreva uma função ‘init’ que retorna toda a lista, exceto o último elemento
def init(list):
    if list == [] or list == '': return []
    else: return list[:-1]

# 4 Escreva uma função ‘last’ que retorna o último elemento de uma lista
def last(list):
    if list == [] or list == '': return head(list)
    else: return last( tail(list) )

# 5 A sequência de Fibonacci é dada pela seguinte série: 0 1 1 2 3 5 8 13 ... Em termos matemáticos, a sequência de Fibonacci pode ser definida através da seguinte relação de recorrência
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    return fib(n-1) + fib(n-2)

# 6 Faça uma função que concatena duas listas de forma recursiva. Utilize as funções head/tail para acessar os elementos. O comportamento deve ser o mesmo do operador + (listas). O operador + até pode ser usado, mas um dos operandos deve conter no máximo 1 elemento.
def concat(l1, l2):
    if l2 == [] or l2 == '': return l1
    elif isinstance(l1, str): return concat (l1 + head(l2), tail(l2))
    else: return concat (l1 + [head(l2)], tail(l2))

# 7 Escreva uma função que verifique se um elemento pertence a uma lista. Não usar o operador “in”;
def pertence(x, list):
    if list == [] or list == '': return False
    elif x == head(list): return True
    else: return pertence(x, tail(list))
    
# 8 Escreva uma função para realizar a união de duas listas. A função é similar à feita na Q6, mas elementos repetidos não são permitidos.
def concat_unique(l1, l2):
    if l2 == [] or l2 == '': return l1
    elif not pertence(head(l2), l1): return concat_unique(l1+head(l2), tail(l2))
    else: return concat_unique(l1, tail(l2))

# 9 Defina uma função que dada uma lista de inteiros e um número n, retorne o total de elementos de valor superior a n.
def has_bigger_than(n, list):
    if list == [] or list == '': return 0
    elif head(list) > n: return 1 + has_bigger_than(n, tail(list))
    else: return 0 + has_bigger_than(n, tail(list))

# 10 Defina uma função que dada uma lista de inteiros e um número n, retorne outra lista contendo apenas de elementos de valor superior a n. Use a função feita na Q6.
def get_biggers_than(n, list):
    if list == [] or list == '': return []
    elif head(list) > n: return concat([head(list)], get_biggers_than(n, tail(list)))
    else: return get_biggers_than(n, tail(list))

# 11 Escreva uma função que inverte o conteúdo de uma lista. Use apenas as funções da Q1 (head) e a da Q6 (concat):
def invert(list):
    if list == [] or list == '': return []
    return concat( invert(tail(list)), [head(list)] )

# 12  Escreva uma função que receba uma palavra e gere seu palíndromo
def palindromizer(list):
    return concat( list, invert(list) )

# 13 Escreva uma função que retorne o tamanho (a quantidade de elementos) de uma lista. Não usar a função len para isso
def size(list):
    if list == [] or list == '': return 0
    else: return 1 + size(tail(list))
    
    
# 14 Escreva a função ehPrimo para verificar se um número dado é primo.
def prime_aux(n, i, c):
    if i > n: return 0
    elif n % i == 0: return 1 + prime_aux(n, i+1, c+1)
    else: return prime_aux(n, i+1, c)
    
def is_prime(n):
    if n <= 1: return False
    return prime_aux(n, 1, 0) == 2

# 15 Defina a função strip que dadas duas listas, retira da segunda todos os elementos que ocorrem na primeira, em qualquer quantidade.
### MEDIA
def strip(elementos, l2):
    if l2 == [] or l2 == '': return l2
    elif pertence( head(l2), elementos): return strip(elementos, tail(l2) )
    else: return [head(l2)] + strip( elementos, tail(l2))
    
# 16 Defina   a   função   consoantList   que   retorna   verdadeiro   se   somente   se   todas   as consoantes da segunda lista, incluindo repetições, ocorrem na primeira lista, na mesma ordem.
# NAO FIZ
def consoant_list(consoantes, l2):
    if consoantes == [] or consoantes == '': return True
    
    elif pertence(head(consoantes), l2): 
        return consoant_list(tail(consoantes), strip([head(consoantes)], l2))
    else: return consoant_list(consoantes, tail(l2))
    
# print(consoant_list(list('sdd'), list('saudade')))

# 17 Defina a função matches que recebe uma lista de palavras e uma sequência de  consoantes e retorna uma lista de possíveis palavras representadas pelas consoantes. Use a função da Q14. Exemplos:
# NAO FIZ
dic = ["arara","arreio","haskell","vaca","vacuo","velho","vermelho","vicio"]
def match():
    print()
    
# 18 Faça uma função que, dado um número, retorna o menor número primo que é maior que o número. Ex: proximoPrimo(2) → 3
def next_prime(n):
    if is_prime(n+1): return n+1
    else: return next_prime(n+1)
    
# 19 Faça a função primes, que retorna a lista de fatores primos de um número que ela recebe. Ex: primes(8)→ [2,2,2]
def fatoracao_aux(n, i):
    if i > n: return []
    elif n%i == 0: return [i] + fatoracao_aux(n/i, i)
    else: return fatoracao_aux(n, next_prime(i))
    
def fatoracao(n):
    return fatoracao_aux(n, 2)

# 20 Defina a função primeFactors que fatora um número inteiro em uma lista de pares (fator,frequência). Exemplos:
def fatores_fatoracao_aux(n, i, contador):
    if i > n: return [(i, contador)]
    elif n%i == 0: return fatores_fatoracao_aux(n/i, i, contador+1)
    else: 
        if contador != 0: return [(i, contador)] + fatores_fatoracao_aux(n, next_prime(i), contador=0)
        else: return fatores_fatoracao_aux(n, next_prime(i), contador=0)
    
def fatores_fatoracao(n):
    return fatores_fatoracao_aux(n, 2, contador=0)

# Defina a função splitToken que recebe um valor e uma lista e retorna uma lista de listas utilizando o valor dado como marcador.
def split_token(token, l1):
    if not pertence(token, l1): return []
    
    elif head(l1) == token:
    else: return [head[l1]]
    
print( split_token(2, [1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 2, 10]) )
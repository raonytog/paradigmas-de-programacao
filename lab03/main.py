
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
# NAO FEITO
def is_prime(n):
    if n == 0 or n == 1: return False
    
print( is_prime(2) )

# 15 Defina a função strip que dadas duas listas, retira da segunda todos os elementos que ocorrem na primeira, em qualquer quantidade.
# NAO FEITO
def strip(l1, l2):
    if l2 == [] or l2 == '': return []
    if pertence( head(l1), l2): return strip( tail(l1), tail(l2) )
    else: return head(l2)
    
print( strip([1, 2], [3, 2, 4] ))

# 16 Defina   a   função   consoantList   que   retorna   verdadeiro   se   somente   se   todas   as consoantes da segunda lista, incluindo repetições, ocorrem na primeira lista, na mesma ordem.
def consoant_list(l1, l2):
    if l2 == [] or l2 == '': return []
import functools
import operator


# ANY - retorna true s.s.s. há algum elemento true (ou equiv.) na lista;
def any_reduce(a, b):
    return a or b

def any(list):
    return functools.reduce(any_reduce, list) == True

# ALL - retorna true s.s.s. todos os elementos da lista são true (ou equiv.);
def  all_reduce(a, b):
    return a and b

def all(list):
    return functools.reduce(all_reduce, list) == True

# LEN - retorna tamanho de uma lista;
def len_reduce(a, b):
    return operator.add(a, 1)

def len(list):
    return functools.reduce(len_reduce, list)

# SUM - soma da lista
def sum_reduce(a, b):
    return operator.add(a, b)

def sum(list):
    return functools.reduce(sum_reduce, list)

# ZIP -  recebe dois iteráveis e retorna uma lista com os elementos de ambos;
# OBS: essa é a descricao q ele botou no slide, mas a funcao zip no python retorna uma lista de tuplas
# por exemplo: list(zip([1, 2], [3, 4])) retorna [(1, 3), (2, 4)]
def acopla(a, b):
    return (a, b)

def my_zip(l1, l2):
    return list(map(acopla, l1, l2))

# REVERSED - retorna a lista em ordem inversa.
def inverte(l1):
    return []

def my_reversed(lista):
    return list(map(inverte, lista, []))


# ENUMERATE - retorna uma tupla com índice e elemento de uma lista
def enumera(a, idx):
    return (idx, a)
    
def my_enumerate(lista):
    return list( map(enumera, lista, range(0, len(lista)+1)) )

# MAX - retorna o valor máximo da lista
def max_reduce(a, b):
    if a > b: return a
    else: return b
    
def max(lista):
    return functools.reduce(max_reduce, lista)

# MIN - retorna o valor mínimo da lista
def min_reduce(a, b):
    if a < b: return a
    else: return b
    
def min(lista):
    return functools.reduce(min_reduce, lista)


# SORTED - retorna se a lista esta ordenada
def sorted_reduce(a, b):
    if a < b: return True
    else: return False
    
def sorted(list):
    return functools.reduce(sorted_reduce, list)

print( sorted([0, 1, 2, 1]) )
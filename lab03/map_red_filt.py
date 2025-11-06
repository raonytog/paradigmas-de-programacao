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

# 1 Escreva uma função ‘head’ que retorna o primeiro elemento de uma lista
def head(lista):
    return functools.reduce(lambda acc, ret: acc, lista)

# 2 Escreva uma função ‘tail’ que retorna toda a lista, exceto o primeiro elemento
def tail(lista):
    if lista == [] or lista == '': return []
    else: return lista[1:]

# 3 Escreva uma função ‘init’ que retorna toda a lista, exceto o último elemento
def init(lista):
    if lista == [] or lista == '': return []
    else: return lista[:-1]

# 4 Escreva uma função ‘last’ que retorna o último elemento de uma lista
def last(lista):
    return functools.reduce(lambda a, b: b, lista)
    
# 5 A sequência de Fibonacci é dada pela seguinte série: 0 1 1 2 3 5 8 13 ... Em termos matemáticos, a sequência de Fibonacci pode ser definida através da seguinte relação de recorrência
def conta(acc, n):
  return acc[1], acc[0]+acc[1]

def fib(n):
    return functools.reduce(conta, range(0, n), (0, 1))[1]

# 6 Faça uma função que concatena duas listas de forma recursiva. Utilize as funções head/tail para acessar os elementos. O comportamento deve ser o mesmo do operador + (listas). O operador + até pode ser usado, mas um dos operandos deve conter no máximo 1 elemento.
def concat(l1, l2):
  return functools.reduce(lambda acc, el: acc + [el], l2, l1)

# 7 Escreva uma função que verifique se um elemento pertence a uma lista. Não usar o operador “in”;
def pertence(lista, x):
  return functools.reduce(lambda acc, el: acc or el==x, lista, False)
    
# 8 Escreva uma função para realizar a união de duas listas. A função é similar à feita na Q6, mas elementos repetidos não são permitidos.

# 9 Defina uma função que dada uma lista de inteiros e um número n, retorne o total de elementos de valor superior a n.

# 10 Defina uma função que dada uma lista de inteiros e um número n, retorne outra lista contendo apenas de elementos de valor superior a n. Use a função feita na Q6.

# 11 Escreva uma função que inverte o conteúdo de uma lista. Use apenas as funções da Q1 (head) e a da Q6 (concat):

# 12  Escreva uma função que receba uma palavra e gere seu palíndromo

# 13 Escreva uma função que retorne o tamanho (a quantidade de elementos) de uma lista. Não usar a função len para isso
    
# 14 Escreva a função ehPrimo para verificar se um número dado é primo.

# 15 Defina a função strip que dadas duas listas, retira da segunda todos os elementos que ocorrem na primeira, em qualquer quantidade.
    
# 16 Defina   a   função   consoantList   que   retorna   verdadeiro   se   somente   se   todas   as consoantes da segunda lista, incluindo repetições, ocorrem na primeira lista, na mesma ordem.
# isto é, oq ta na primeira lista, aparece na mesma ordem na segunda lista]

# 17 Defina a função matches que recebe uma lista de palavras e uma sequência de  consoantes e retorna uma lista de possíveis palavras representadas pelas consoantes. Use a função da Q14. Exemplos:
dic = ["arara","arreio","haskell","vaca","vacuo","velho","vermelho","vicio"]
    
# 18 Faça uma função que, dado um número, retorna o menor número primo que é maior que o número. Ex: proximoPrimo(2) → 3
    
# 19 Faça a função primes, que retorna a lista de fatores primos de um número que ela recebe. Ex: primes(8)→ [2,2,2]

# 20 Defina a função primeFactors que fatora um número inteiro em uma lista de pares (fator,frequência). Exemplos:

# 21 Defina a função splitToken que recebe um valor e uma lista e retorna uma lista de listas utilizando o valor dado como marcador.

# 22 Defina a função joinToken que recebe um valor e uma lista de listas e retorna a concatenação das sublistas usando o primeiro parâmetro como separador

# 23 Defina a função splitHalf que divide uma lista em duas, de tamanho iguais (ou com  diferença de apenas um elemento no caso de uma lista de tamanho ímpar).

# 24 Uma tripla (x,y,z) de números inteiros positivos é chamada pitagórica se x2+y2 = z2. Usando list comprehension, defina uma função pyths que mapeia um inteiro n a uma lista de todas as triplas pitagóricas componentes no intervalo [1..n]. Por exemplo

#25 Um número inteiro positivo é perfeito se ele igual à soma de todos os seus fatores, excluindo o próprio número. Usando list comprehension, defina uma função perfects que retorna a lista de todos os números perfeitos de zero até um dado limite. Por exemplo: perfects (500) -> [6,28,496]

# 26  produto escalar de dois vetores v e w de tamanho n é dado pela soma dos produtos dos elementos correspondentes. Usando list comprehension, defina uma função que retorna o produto escalar de dois vetores representados por listas

# 27 O problema das n rainhas consiste em posicionar em um tabuleiro de xadrez n×n, n rainhas de modo que cada rainha não ataque as demais. Uma rainha pode atacar qualquer outra que esteja na mesma linha, coluna, ou nas mesmas diagonais. Considere que a representação da solução será feita por meio de uma lista de pares (Linha, Coluna), de coordenadas das rainhas. Defina a função ataca que dada uma posição e uma lista de posições diz se a primeira posição ataca qualquer uma das posições da lista.

# 28 Implemente a função isPalindrome que verifica se uma string é palindroma ou não.


# 29 Implemente a função compress que elimina duplicadas consecutivas em uma lista.

    
#30 Implemente a função pack que empacota os elementos duplicados consecutivos em sublistas

    
# 31 Implemente a função encode que especifica o método de compressão de dados baseado no tamanho da sequência repetida. Neste método os elementos duplicados consecutivos são codificados como duplas (N,E), onde N é o número de duplicadas do elemento E. Ex: encode "aaaabccaadeeee" -> [(4,’a’),(1,’b’),(2,’c’),(2,’a’),(1,’d’),(4,’e’)]


# 32 Implemente a função decode a qual, dada uma lista codificada como no exercício anterior, gera a lista original.
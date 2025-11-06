import functools
import operator

# 1 Escreva uma função ‘head’ que retorna o primeiro elemento de uma lista
def head(lista):
    if lista == []: return []
    if lista == '': return ''
    return lista[0]

# 2 Escreva uma função ‘tail’ que retorna toda a lista, exceto o primeiro elemento
def tail(lista):
    if lista == []: return []
    if lista == '': return ''
    return lista[1:]

# 3 Escreva uma função ‘init’ que retorna toda a lista, exceto o último elemento
def init(lista):
    if lista == []: return []
    if lista == '': return ''

# 4 Escreva uma função ‘last’ que retorna o último elemento de uma lista
def last(lista):
    if lista == []: return []
    if lista == '': return ''
    return lista[-1]

# ANY - retorna true s.s.s. há algum elemento true (ou equiv.) na lista;
def any(lista):
    if lista == [] or lista == '': return False
    
    if head(lista) == True: return True
    else: return any( tail(lista) )

# ALL - retorna true s.s.s. todos os elementos da lista são true (ou equiv.);
def all(lista):
    if lista == [] or lista == '': return True
    
    if head(lista) == True: return True and all( tail(lista) )
    else: return False

# LEN - retorna tamanho de uma lista;
def len(lista):
    if lista == [] or lista == '': return 0
    return 1+len( tail(lista) )

# SUM - soma da lista
def sum(lista):
    if lista == [] or lista == '': return 0
    return head(lista) + sum( tail(lista) )

# ZIP -  recebe dois iteráveis e retorna uma lista com os elementos de ambos;
# OBS: essa é a descricao q ele botou no slide, mas a funcao zip no python retorna uma lista de tuplas
# por exemplo: list(zip([1, 2], [3, 4])) retorna [(1, 3), (2, 4)]
def my_zip(v, w):
    if v == [] or w == []: return []
    return [(head(v), head(w))] + my_zip(tail(v), tail(w))

# REVERSED - retorna a lista em ordem inversa.
def my_reversed(lista):
    if lista == []: return []
    if lista == '': return ''
    
    if isinstance(lista, list): return my_reversed( tail(lista) ) + [head(lista)]
    elif isinstance(lista, str): return my_reversed( tail(lista) ) + head(lista)

# ENUMERATE - retorna uma tupla com índice e elemento de uma lista
def my_enumerate(lista):
    def enumerate_aux(lista, i):
        if lista == []: return []
        if lista == '': return ''
        
        return [(i, head(lista))] + enumerate_aux(tail(lista), i+1)
    
    return enumerate_aux(lista, 0)    

# MAX - retorna o valor máximo da lista
def max(lista):
    def max_aux(lista, val):
        if lista == [] or lista == '': return val
        
        if head(lista) > val: return max_aux(tail(lista), head(lista))
        else: return max_aux(tail(lista), val)
    return max_aux(lista, head(lista))


# MIN - retorna o valor mínimo da lista
def min(lista):
    def min_aux(lista, val):
        if lista == [] or lista == '': return val
        
        if head(lista) < val: return min_aux(tail(lista), head(lista))
        else: return min_aux(tail(lista), val)
    return min_aux(lista, head(lista))

# SORTED - retorna se a lista esta ordenada
def sorted(lista):
    if lista == []: return True
    
    if head(tail(lista)) != []:
        if head(lista) < head( tail(lista) ): return True and sorted(tail(lista))
        else: return False
    else: return True
        
# 5 A sequência de Fibonacci é dada pela seguinte série: 0 1 1 2 3 5 8 13 ... Em termos matemáticos, a sequência de Fibonacci pode ser definida através da seguinte relação de recorrência
def fib(n):
    if n < 0: return -1
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1)+fib(n-2)

# 6 Faça uma função que concatena duas listas de forma recursiva. Utilize as funções head/tail para acessar os elementos. O comportamento deve ser o mesmo do operador + (listas). O operador + até pode ser usado, mas um dos operandos deve conter no máximo 1 elemento.
def concat(l1, l2):
    if l2 == [] or l2 == '': return l1
    
    if isinstance(l1, list): return l1 + [head(l2)] + concat([], tail(l2))
    if isinstance(l1, str): return l1 + head(l2) + concat('', tail(l2))
        
# 7 Escreva uma função que verifique se um elemento pertence a uma lista. Não usar o operador “in”;
def pertence(lista, x):
    if lista == []: return False
    if lista == '': return False
    
    if head(lista) == x: return True
    else: return pertence(tail(lista), x)
        
# 8 Escreva uma função para realizar a união de duas listas. A função é similar à feita na Q6, mas elementos repetidos não são permitidos.
def concat_no_repeat(l1, l2):
    if l2 == [] or l2 == '': return l1
        
    if not pertence(l1, head(l2)): return concat_no_repeat(l1 + [head(l2)], tail(l2))
    else: return concat_no_repeat(l1, tail(l2))
    
# 9 Defina uma função que dada uma lista de inteiros e um número n, retorne o total de elementos de valor superior a n.
def has_bigger_than(lista, n):
    if lista == []: return 0
    
    if head(lista) > n: return 1 + has_bigger_than( tail(lista), n)
    else: return has_bigger_than( tail(lista), n)
    
# 10 Defina uma função que dada uma lista de inteiros e um número n, retorne outra lista contendo apenas de elementos de valor superior a n. Use a função feita na Q6.
def get_bigger_than(lista, n):
    if lista == []: return []
    
    if head(lista) > n:
        return concat([head(lista)], get_bigger_than(tail(lista), n))
    else:
        return get_bigger_than(tail(lista), n)
    
# 11 Escreva uma função que inverte o conteúdo de uma lista. Use apenas as funções da Q1 (head) e a da Q6 (concat):
def invert(lista):
    if lista == []: return []
    if lista == '': return ''
    
    if isinstance(lista, list): return concat(invert(tail(lista)), [head(lista)] )
    if isinstance(lista, str): return concat(invert(tail(lista)), head(lista) )
    
# 12  Escreva uma função que receba uma palavra e gere seu palíndromo
def palindromo(palavra):
    if palavra == '': return ''
    return concat(palavra, invert(palavra))

# 13 Escreva uma função que retorne o tamanho (a quantidade de elementos) de uma lista. Não usar a função len para isso
def size(lista):
    if lista == []: return 0
    return 1 + size(tail(lista))
    
# 14 Escreva a função ehPrimo para verificar se um número dado é primo.
def is_prime(n):
    def is_prime_aux(n, i):
        if i > n: return 0
        if n%i==0: return 1 + is_prime_aux(n, i+1)
        else: return is_prime_aux(n, i+1)
    return is_prime_aux(n, 1) == 2    

# 15 Defina a função strip que dadas duas listas, retira da segunda todos os elementos que ocorrem na primeira, em qualquer quantidade.
def strip(elementos, lista):
    if lista == []: return lista
    if pertence(elementos, head(lista)): return strip(elementos, tail(lista))
    else: return [head(lista)] + strip(elementos, tail(lista))
    
# 16 Defina   a   função   consoantList   que   retorna   verdadeiro   se   somente   se   todas   as consoantes da segunda lista, incluindo repetições, ocorrem na primeira lista, na mesma ordem.
# isto é, oq ta na primeira lista, aparece na mesma ordem na segunda lista]
def rmv_first_aparicao(lista, x):
        if not pertence(lista, x): 
            if lista == []: return []
            if lista == '': return ''
            
        if head(lista) == x: return tail(lista)
        else: 
            if isinstance(lista, str): return head(lista) + rmv_first_aparicao(tail(lista), x)
            if isinstance(lista, list): return [head(lista)] + rmv_first_aparicao(tail(lista), x)
            
def consoant_list(consoantes, lista):
    if consoantes == [] or consoantes == '': return True
            
    if not pertence(lista, head(consoantes)): return False
    else: return True and consoant_list(tail(consoantes), rmv_first_aparicao(lista, head(consoantes)))

# 17 Defina a função matches que recebe uma lista de palavras e uma sequência de  consoantes e retorna uma lista de possíveis palavras representadas pelas consoantes. Use a função da Q14. Exemplos:
dic = ["arara","arreio","haskell","vaca","vacuo","velho","vermelho","vicio"]
def match(lista, consoantes):
    if lista == []: return []
    if consoant_list(consoantes, head(lista)): return [head(lista)] + match(tail(lista), consoantes)
    else: return match(tail(lista), consoantes)
    
# 18 Faça uma função que, dado um número, retorna o menor número primo que é maior que o número. Ex: proximoPrimo(2) → 3
def nxtPrime(n):
    if is_prime(n+1): return n+1
    else: return nxtPrime(n+1)
    
# 19 Faça a função primes, que retorna a lista de fatores primos de um número que ela recebe. Ex: primes(8)→ [2,2,2]


def fatores(n):
    def fatores_aux(n, i):
        if i > n: return []
        if n%i == 0: return [i] + fatores_aux(n/i, i)
        else: return fatores_aux(n, nxtPrime(i))
    
    return fatores_aux(n, 2)

# 20 Defina a função primeFactors que fatora um número inteiro em uma lista de pares (fator,frequência). Exemplos:
def fatores_freq(n):
    def fatores_freq_aux(n, i, f):
        if i>n: return [(i, f)]
        if n%i==0: return fatores_freq_aux(n/i, i, f+1)
        else: 
            if f >0: return concat([(i, f)], fatores_freq_aux(n, nxtPrime(i), 0))
            else: return fatores_freq_aux(n, nxtPrime(i), 0)
        
    return fatores_freq_aux(n, 2, 0)

# 21 Defina a função splitToken que recebe um valor e uma lista e retorna uma lista de listas utilizando o valor dado como marcador.
# splitToken(2, [1, 1, 2, 1, 1, 1, 2, 1]) -> [[1,1], [1,1,1],[1]]
def split_token(token, lista):
    
    def split_token_aux(token, lista, output):
        if lista == []: return [output]
        if head(lista) == token: return [output] + split_token_aux(token, tail(lista), [])
        else: return split_token_aux(token, tail(lista), output+[head(lista)])
        
    return split_token_aux(token, lista, [])

# 22 Defina a função joinToken que recebe um valor e uma lista de listas e retorna a concatenação das sublistas usando o primeiro parâmetro como separador
def join_token(token, listas):
    if listas == []: return []
     
    if size(tail(listas)) == 0: return head(listas)
    else: return head(listas)+[token]+join_token(token, tail(listas))
    

# 23 Defina a função splitHalf que divide uma lista em duas, de tamanho iguais (ou com  diferença de apenas um elemento no caso de uma lista de tamanho ímpar).
def split_half(lista):
    
    def split_half_aux(original, left, max, atual):
        if atual == max//2: return [left, original]
        return split_half_aux(tail(original), left+[head(original)], max, atual+1)
    
    return split_half_aux(lista, [], size(lista), 0)


# 24 Uma tripla (x,y,z) de números inteiros positivos é chamada pitagórica se x2+y2 = z2. Usando list comprehension, defina uma função pyths que mapeia um inteiro n a uma lista de todas as triplas pitagóricas componentes no intervalo [1..n]. Por exemplo
def pyths(n):
    return [(x,y,z) 
            for x in range(1, n+1)
            for y in range(1, n+1)
            for z in range(1, n+1)
            if x**2+y**2 == z**2]
    

#25 Um número inteiro positivo é perfeito se ele igual à soma de todos os seus fatores, excluindo o próprio número. Usando list comprehension, defina uma função perfects que retorna a lista de todos os números perfeitos de zero até um dado limite. Por exemplo: perfects (500) -> [6,28,496]
def perfects(n):
    return [x for x in range(1, n+1)
            if sum([y for y in range(1, x) if x%y==0]) == x]
    
# 26  produto escalar de dois vetores v e w de tamanho n é dado pela soma dos produtos dos elementos correspondentes. Usando list comprehension, defina uma função que retorna o produto escalar de dois vetores representados por listas
def prod_escalar(v, w):
    return sum([x1*x2 for x1, x2 in zip(v, w)])

# 27 O problema das n rainhas consiste em posicionar em um tabuleiro de xadrez n×n, n rainhas de modo que cada rainha não ataque as demais. Uma rainha pode atacar qualquer outra que esteja na mesma linha, coluna, ou nas mesmas diagonais. Considere que a representação da solução será feita por meio de uma lista de pares (Linha, Coluna), de coordenadas das rainhas. Defina a função ataca que dada uma posição e uma lista de posições diz se a primeira posição ataca qualquer uma das posições da lista.
def ataca(atual, posicoes):
    if posicoes == []: return False
    
    # linha
    if head(posicoes)[0] == head(atual): return True
    
    # coluna
    elif head(posicoes)[1] == tail(atual): return True
    
    # diagonal
    elif abs(atual[0] - head(posicoes)[0]) == abs(atual[1] - head(posicoes)[1]): return True
    
    else: return ataca(atual, tail(posicoes))
    
# 28 Implemente a função isPalindrome que verifica se uma string é palindroma ou não.
def is_palindrome(palavra):
    return palavra == invert(palavra)

# 29 Implemente a função compress que elimina duplicadas consecutivas em uma lista.
def compress(lista):
    if lista == []: return []
    
    if head(lista) == head(tail(lista)): return compress(tail(lista))
    else: return [head(lista)] + compress(tail(lista))
    
#30 Implemente a função pack que empacota os elementos duplicados consecutivos em sublistas
def pack(lista):    
    def pack_aux(lista, output):
        if lista == []: return []
        
        if head(lista) == head(tail(lista)): return pack_aux(tail(lista), output+[head(lista)])
        else: return [output] + pack_aux(tail(lista), [])
        
    return pack_aux(lista, [])
    
# 31 Implemente a função encode que especifica o método de compressão de dados baseado no tamanho da sequência repetida. Neste método os elementos duplicados consecutivos são codificados como duplas (N,E), onde N é o número de duplicadas do elemento E. Ex: encode "aaaabccaadeeee" -> [(4,’a’),(1,’b’),(2,’c’),(2,’a’),(1,’d’),(4,’e’)]
def encode(lista):
    def encode_aux(lista, c):
        if lista == [] or lista == '': return []
        if head(lista) == head( tail(lista) ): return encode_aux(tail(lista), c+1)
        else: return [(c, head(lista))] + encode_aux(tail(lista), 1)
        
    return encode_aux(lista, 1)
    
# 32 Implemente a função decode a qual, dada uma lista codificada como no exercício anterior, gera a lista original.
def decode(lista):
    if lista == [] or lista == '': return ''
    return head(lista)[1]*head(lista)[0] + decode(tail(lista))
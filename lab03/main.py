# 1
def head(list):
    if list == []: return []
    else: return list[0]

# 2
def tail(list):
    if list == []: return []
    else: return list[1:]

# 3
def init(list):
    if list == []: return []
    else: return list[:-1]

# 4 
def last(list):
    if tail(list) == []: return head(list)
    else: return last( tail(list) )

# 5 
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    return fib(n-1) + fib(n-2)

# 6
def concat(l1, l2):
    if l2 == [] or l2 == '': return l1
    else: return concat (l1 + head(l2), tail(l2))

# 7 
def pertence(x, list):
    if list == [] or list == '': return False
    elif x == head(list): return True
    else: return pertence(x, tail(list))
    
# 8
def concat_unique(l1, l2):
    if l2 == [] or l2 == '': return l1
    elif not pertence(head(l2), l1): return concat_unique(l1+head(l2), tail(l2))
    else: return concat_unique(l1, tail(l2))

# 9
def has_bigger_than(n, list):
    if list == [] or list == '': return 0
    elif head(list) > n: return 1 + has_bigger_than(n, tail(list))
    else: return 0 + has_bigger_than(n, tail(list))
    
# 10 ERRADO AQUI
def get_biggers_than(n, list):
    if list == [] or list == '': return []
    elif head(list) > n: return concat([head(list)], get_biggers_than(n, tail(list)))
    
print( get_biggers_than(3, [1, 2, 0, 4, 5]))
    
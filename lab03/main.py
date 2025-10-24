def head(list):
    if list == []: return []
    else: return list[0]

def tail(list):
    return list[1:]

def init(list):
    return list[:-1]

def last(list):
    if tail(list) == []: return head(list)
    else: return last( tail(list) )
    
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    return fib(n-1) + fib(n-2)

def concat(l1, l2):
    return l1 + head(l2) + concat()

print( concat("ola ", " auau") )
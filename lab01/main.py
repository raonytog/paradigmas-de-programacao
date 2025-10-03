import random


def atv01():
    num = int(input())
    for i in range(num+1):
        if i%2 == 0: 
            print(i)

def atv02():
    palavra = input()

    count = 0
    for l in palavra:
        if l in "aeiou":
            count += 1

    print(count)

def atv03():
    n = list()
    for i in range(5):
        n.append( int(input()) )

    aux = 0
    for i in range(0, 5):
        for j in range (i+1, 5):
            if n[i] > n[j]:
                aux = n[j]
                n[j] = n[i]
                n[i] = aux

    print(n)

def atv04():
    num = int(input())

    sum = 0
    while num > 0:
        sum += num%10
        num = num//10
    
    print(sum)

def atv05():
    num = int(input())
    for i in range(10):
        print(f"{i+1:>2}x{num} = {num*(i+1)}")

def atv06():
    n = []
    for i in range(10):
        n.append(int(input()))

    min = n[0]
    max = n[0]

    for i in range(10):
        if n[i]<min:
            min = n[i]
        if n[i]>max:
            max = n[i]
    print(min)
    print(max)

def atv07():
    num = int(input())
    for i in range(num, 0,-1):
        print(i)

    print("FIM!")

def atv08():
    c = float(input())
    k = c + 273
    f = 1.8*c +32

    print(k, f)

def atv09():
    m = []
    for i in range(3):
        m.append(input().split(" "))
    
    for i in range(3):
        for j in range(i+1,3):
            aux = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = aux

    print(m)

def atv10():
    a = int(input())
    b = int(input())

    for i in range(a, b+1):
        count = 0
        for j in range(1, i+1):
            if i%j==0:
                count+=1
        
        if count == 2:
            print(f"{i} é primo")

def atv11():
    n = int(input())

    cem = n//100
    n = n%100

    cinquenta = n//50
    n = n%50
    
    vinte = n//20
    n = n%20
    
    dez = n//10
    n = n%10
    
    cinco = n//5
    n = n%5
    
    dois = n//2
    n = n%2

    print(f"100 {cem}\n50 {cinquenta}\n20 {vinte}\n10 {dez}\n5 {cinco}\n2 {dois}")

def atv12():
    num = int(input())

    val = 1
    for i in range(num, 0, -1):
        val *= i

    print(val)

def atv13():
    palavra = input()
    palindromo = palavra[::-1]

    if palavra == palindromo: print("é palindromo")
    else: print("não é palindromo")

def atv14():
    n = int(input())
    m = []
    for i in range(n):
        l = []
        for j in range(n):
            if i == j:
                l.append(1)
            else: 
                l.append(0)
        m.append(l)

    print(m)

def atv15():
    nota_parcial = 0
    sum = 0
    for _ in range(3):
        nota = float(input())
        peso = float(input())
        sum += peso
        nota_parcial += nota*(peso)

    nota_parcial /= sum
    print(nota_parcial)

def atv16():
    val = random.randint(1, 100)

    while True:
        tentativa = int(input())

        if tentativa > val: print("menor")
        elif tentativa < val: print("maior")
        else:
            print("eba")
            break

def atv17():
    f = lambda x: x**2
    a = 0
    b = 4
    n = 4
    
    h = (b - a) / n
    
    area = f(a)
    for i in range(1, n):
        x = a + i*h
        if i % 2 == 0: area += 2 * f(x)
        else: area += 4 * f(x)
    area += f(b)

    area *= h / 3
    print(area)
    
def atv18():
    palavra = input('Digite uma palavra e a mantenha em segredo: ')
    gabarito = list(palavra)
    print("\n"*20)

    descobertas = ["_" for _ in palavra]
    
    vidas = len(palavra)
    for _ in range(vidas):
        print(descobertas)
        tentativa = input('Digite uma letra: ')
        
        if tentativa in palavra:
            for i, l in enumerate(palavra):
                if l == tentativa:
                    descobertas[i] = tentativa
        else:
            print("Letra não contida na palavra!")
                    
        if gabarito == descobertas:
            print("Parabéns!")
            break
    
def atv19():
    # deu preguica
    M = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5]]
    

def main():
    atv19()

if __name__== '__main__':
    main()

'''
MAP
'''
#? EJEMPLO GUILLE

values = [4,81,144]

def raiz_cuadrada(a):
    return a**(1/2)

a = map(raiz_cuadrada,values)

print(raiz_cuadrada())
print(list(map(raiz_cuadrada,values)))
print(list(map(lambda a: a**2, values)))

#? EJEMPLO VITO

x = [2,4,24]
y = [3,7,30]

def pow(a):
    return a ** 2

def mapeo(function, given_list):
    result = []
    for value in given_list:
        result.append(pow(value))
    return result

print(mapeo(pow ,x))
print(list(map(pow,x)))
print(list(map(lambda a: a**2,x)))
print(list(map(lambda a,b: a*b,x,y)))

#? Ejemplo ZIP con lambda

x = [2, 4, 24]
y = [3, 7 , 30]

print(list(zip(x,y)))

print(list(map(lambda par: par[0] * par[1], zip(x,y))))

#? Ejemplo Filter con lambda

y = [3, 7, 30, 20, 7, 2]

pares = list(filter(lambda n: n % 2 == 0, y))

print(pares)

from functools import reduce

def veredict(number):
    a = number % 2 == 0
    if a:
        return number

print(list(map(lambda number: number %2 == 0, y)))
print(list(filter(lambda number: number %2 == 0, y)))

letters = ["p", "a", "b", "l", "o"]
x = [2,4,24]

print(reduce(lambda a, b: a+b, x))
print(reduce(lambda a, b: a+b, letters))


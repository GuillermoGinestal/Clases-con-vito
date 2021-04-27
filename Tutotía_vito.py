#  #? Lambda

# a = [1,2,3,4]

# def cuadrados(given_list):          #! Siempre debe de recibir un argumento como minimo
#     result = []
#     for num in given_list:
#         result.append(num**2)
#     return result

# funcion = lambda num: num **2
# resultado = funcion(3)
# print(resultado)


# # matematica = {"suma": lambda a,b: num a + b, "cuadrado": lambda num: num **2, "cubo": lambda num: num**3}

# resultado = matematica["cubo"](5)
# print(resultado)

# #? MAP              

# a = [1,2,3,4]

# def cuadrado(num):          
#     return num ** 2

# resultado = list(map(cuadrado, a))
# print(resultado)

# resultado_lambda = list(map(lambda num: num **2, a))

# # resultado_lambda_sin_pow = list(map(lambda num1, num2, num3: ))

# #? FILTER

# # resultado_filtrado = list(filter(lambda num: num % 2 == , a))


a = [1203,1233,64,3430,44,32130,1230,4,3,2,34,6,9,4645,45,3]

b = list(filter(lambda num: num >= 100, a))

print(b)


names = ["Pablo", "Guillermo", "Ciriaco", "Evander"]

def with_g(given_list):
    result = []
    for name in given_list:
        if name.startswith('G'):
            result.append(name)
    return result

resultado = list(filter(lambda name: name.startswith('G'), names))

print(resultado)
    
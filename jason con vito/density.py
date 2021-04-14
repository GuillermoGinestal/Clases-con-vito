import json
import os.path

pwd = os.path.dirname(os.path.realpath(__file__))
o = open(f"{pwd}/data.json")


data = json.load(o)
data = data["data"]
# print(data[1])
o.close()

# Ejercicio 1: Obtender la densidad media de los municipios de Madrid

def densidad_media(data):
    
    longitud = len(data)
    count = 0
    for densidad in data:
        count += densidad['densidad_por_km2']
    
    return count / longitud

# print(densidad_media(data))

# Ejercicio 2: Obtener municipio por codigo ine // Extra: utilizando función filter

def obtener_municipio(data):
	codigo_ine = input('introduce un codigo: ')
	for codigo in data:
		if codigo['municipio_codigo_ine'] == codigo_ine:
			return codigo
		
	
# print(obtener_municipio(data))

# Ejercicio 3: Obtener el municipio más grande

def municipio_grande(data):

    maximo = 0
    indice = 0
    indice_del_maximo = 0

    for municipio in data:
        if municipio['superficie_km2'] > maximo:
            indice_del_maximo = indice
            maximo = municipio['superficie_km2']
        indice += 1
    return data[indice_del_maximo]
        

# print(municipio_grande(data))



# Ejercicio 4: Obtener los 10 municipios con mayor densidad poblacional


def top10_densidad(data):
    lista_densidad = []
    lista_top10densidad = []
    for elemento in data:
        lista_densidad.append(elemento["densidad_por_km2"])
    
    print(len(lista_densidad))
    count = 0
    while count != 10:
        for v in range(0, 10):
            x = max(lista_densidad)
            lista_top10densidad.append(x)
            lista_densidad.pop(lista_densidad.index(x))
            count += 1
    return lista_top10densidad
    
print(top10_densidad(data))

# Ejercicio Bonus: Crea una función que reciba como parametro el dataset y devuelva tres listas con la siguiente condición:
# la lista 1 tendrá todos los valores de densidad que empiecen por 1
# la lista 2 tendrá todos los valores de densidad que empiecen por 2 ej: lista_1 = ["134324", "1354211", "349.34"]
# OOP

def valores_1(data):
    lista_densidad = []
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    for elemento in data:
        lista_densidad.append(elemento["densidad_por_km2"])

    for elemento in lista_densidad:
        if str(elemento).startswith('1'):
            lista1.append(elemento)
        elif str(elemento).startswith('2'):
            lista2.append(elemento)
        elif str(elemento).startswith('3'):
            lista3.append(elemento)
        elif str(elemento).startswith('4'):
            lista4.append(elemento)
    # return lista1, lista2, lista3

    porcentaje1 = len(lista1)*100/len(lista_densidad)
    porcentaje2 = len(lista2)*100/len(lista_densidad)
    porcentaje3 = len(lista3)*100/len(lista_densidad)
    porcentaje4 = len(lista4)*100/len(lista_densidad)
    return f"Lista 1: {len(lista1)}, porcentaje: {porcentaje1}\nLista 2: {len(lista2)}, porcentaje: {porcentaje2}\nLista 3: {len(lista3)}, porcentaje: {porcentaje3}\nLista 4: {len(lista4)}, porcentaje: {porcentaje4}"

print(valores_1(data))


# Ejercicio 5: Crear una clase de tipo municipality/municipio
# Debe tener tantas propiedas como claves en el diccionario


class Municipio:
    def __init__ (self, municipio_nombre, densidad_por_km2, superficie_km2):
        self.municipio_nombre = municipio_nombre
        self.densidad_por_km2 = densidad_por_km2
        self.superficie_km2 = superficie_km2

    def __str__ (self):
        return f"\nNombre: {self.municipio_nombre}\nDensidad: {self.densidad_por_km2:.3f}\nSuperficie: {self.superficie_km2:.3f} "


# Ejercicio 7: Crear una función que acepte un solo parámetro (municipio) 
# y que devuleva un objecto con las propiedades (nombre, densidad, superfice)


def municipio(nombre_municipio):
    list_municipio = []
    
    for mun in data:
        if mun['municipio_nombre'] == nombre_municipio:
            list_municipio.append(mun)
            nombre, densidad, superficie = list_municipio[0]['municipio_nombre'], list_municipio[0]['densidad_por_km2'], list_municipio[0]['superficie_km2']
            objeto_municipio = Municipio(nombre, densidad, superficie)
            return objeto_municipio
    return 'Este municipio no existe'

print(municipio('Villalbilla'))


# Ejercicio 9: Crear una función que acepte como parámetro toda la lista de diccionarios y devuelva una lista de objetos


class Municipio_2:

    def __init__ (self, municipio_codigo, densidad_por_km2, municipio_codigo_ine, nuts4_nombre, municipio_nombre, nuts4_codigo, superficie_km2):
        
        self.municipio_codigo = municipio_codigo
        self.densidad_por_km2 = densidad_por_km2
        self.municipio_codigo_ine = municipio_codigo_ine
        self.nuts4_nombre = nuts4_nombre
        self.municipio_nombre = municipio_nombre
        self.nuts4_codigo = nuts4_codigo
        self.superficie_km2 = superficie_km2

    # def __str__ (self):
    #     return f"\nCódigo del Municipio: {self.municipio_codigo}\nDensidad por km2: {self.densidad_por_km2:.3f}\nCódigo INE: {self.municipio_codigo_ine}\nNombre del nuts4: {self.nuts4_nombre}\nNombre del Municipio: {self.municipio_nombre}\nCódigo del nuts4: {self.nuts4_codigo}\nSuperficie del Municipio: {self.superficie_km2}  "

def obj_municipio(data):

    lista_municipio = []

    for diccionario in data:
        obj = Municipio_2(diccionario['municipio_codigo'],
                        diccionario['densidad_por_km2'],
                        diccionario['municipio_codigo_ine'],
                        diccionario['nuts4_nombre'],
                        diccionario['municipio_nombre'],
                        diccionario['nuts4_codigo'],
                        diccionario['superficie_km2'])
        lista_municipio.append(obj)
    return lista_municipio

# print(obj_municipio(data))

# Ejercicio 10: Considerando que en cada objeto tenemos la superficie y densidad ambas por km2,
#  crear un MÉTODO (una función dentro del objeto) que devuelva la densidad total del municipio dado

def total_densidad(municipio_nombre):
    for num in data:
        if num['municipio_nombre'] == municipio_nombre:
            densidad = num['densidad_por_km2'] 
            superficie_total = num['superficie_km2']
            densidad_total = densidad * superficie_total
            return f'La densidad total es {densidad_total}'


print(total_densidad('Villalbilla'))


# Ejercicio 11: Ya que tenemos una lista con todos los objetos, 
# con su método "get_total_density()" obtener la densidad total de la comunidad de Madrid

def densidad_madrid(data):

    lista_densidades = []
    lista_superficies = []

    for mun in data:
        lista_densidades.append(mun['densidad_por_km2'])
        lista_superficies.append(mun['superficie_km2'])
    densidad_total_madrid = sum(lista_densidades) * sum(lista_superficies)
    return f'La densidad total de Madrid es {densidad_total_madrid:.2f}'

print(densidad_madrid(data))





# Ejercicio 12: Crea un contador de modo que cada vez que se cree una nueva instancia, 
# el mencionado contador aumente en 1





# Ejercicio 13: Crea un classmethod llamado from_str que crea una instancia de la siguiente cadena --> "test-3.54-23.86"







# Ejercicio 14: Estable una tasa de crecimiento anual del 2%








# Ejercicio 15: Define un método que aplique el crecimiento anual sobre un objeto
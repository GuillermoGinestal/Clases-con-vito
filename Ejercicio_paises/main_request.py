
import requests as req
import csv
import json

# C:/Users/cice/AppData/Local/Programs/Python/Python39/python.exe -m pip install requests 



def buscar_pais():

    nombre_pais = input('Introduce nombre del pais: ')

    response = req.get(f'https://restcountries.eu/rest/v2/name/{nombre_pais}').json()

    print(response)
    print(f"Name:{response[0]['name']}\nCapital: {response[0]['capital']}\nRegión: {response[0]['region']}\nPopulation: {response[0]['population']}\nArea: {response[0]['area']}\nIdioma: {response[0]['languages'][0]['nativeName']}")

    busqueda_pais = (response[0]['name'],response[0]['capital'],response[0]['region'],response[0]['area'],response[0]['languages'][0]['nativeName'],response[0]['flag'])
    print(busqueda_pais)

    with open('csv_paises.csv', 'a', newline = "" ) as paises:
        csv_writer = csv.writer(paises)
        csv_writer.writerow([response[0]['name'],response[0]['capital'],response[0]['region'],response[0]['area'],response[0]['languages'][0]['nativeName'],response[0]['flag']]) 
    
    response3 = req.get(response[0]['flag'])
    nombre_PAIS = f"{str(nombre_pais)}.svg"
    with open(f"./Unidad 12 csv con vito/imagenes/{nombre_PAIS}", "wb") as img:     #Hay que poner el formato del archivo y convertirlo en binario(wb)
        img.write(response3.content)


def buscar_continente():

    continente = input('Buscar por continente: ')

    response2 = req.get(f'https://restcountries.eu/rest/v2/region/{continente}').json()
    nombre_continente = continente
    with open(f'{nombre_continente}.json', "w") as jsonfile:
            json.dump({'data': response2}, jsonfile)    


def get_population(nombre_continente):
    
    lista_population = []
    with open(f'{nombre_continente}.json') as jsonfile:
        data = json.load(jsonfile)
        data = data['data']

        for population in data:
            lista_population.append(population['population'])

    return sum(lista_population)

# print(get_population())

def historial_busqueda(pais_poblacion):

    with open('csv_paises.csv', "r") as paises:

        csv_reader = csv.reader(paises)
        for pais in csv_reader:
            if pais_poblacion == pais[0]:
                # print(pais[0], pais[3])
                return pais[0], pais[3]

class Pais():
    poblacion_total = 0
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population
        Pais.poblacion_total += self.population

def obj_pais():
    response_4 = req.get(f'https://restcountries.eu/rest/v2/all').json()
    
    lista_obj_paises = []

    for diccionario in response_4:
        obj = Pais(diccionario['name'],
                diccionario['capital'],
                diccionario['population'])
        lista_obj_paises.append(obj)

    return  Pais.poblacion_total

# print(*obj_pais())    # La función asterisco te imprime sin tupla!



def menu():
    """
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
    print ("Bienvenido al menú, selecciona una opción ")
    print ("1 Busca un país")
    print ("2 Busca un continente")
    print ("3 Busca la population de un continente")
    print ("4 historial de búsqueda")
    print ("5 Recibir la población total del mundo")
    print ("6 Salir del programa")


    while True:
        
        # solicituamos una opción al usuario
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu =="1":
            buscar_pais()

        elif opcionMenu =="2":
            buscar_continente()

        elif opcionMenu =="3":
            continente = input('¿De que continente quieres obtener la población? ')
            print('La población total es: ', get_population(continente))
        
        elif opcionMenu == "4":
            busqueda_pais_poblacion = input('¿De que país quieres obtener el nombre y la población?')
            print('El nombre y la población son: ', historial_busqueda(busqueda_pais_poblacion))
        
        elif opcionMenu == "5":
            print(f'La población total es: ', obj_pais())

        elif opcionMenu == "6":
            print("Usted ha salido del programa")
            break
        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

menu()





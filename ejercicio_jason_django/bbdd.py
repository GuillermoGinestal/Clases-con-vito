import requests as req
import json
import os
import utm

# utm.to_latlon(x,y,30,"N")

def get_data_desfibriladores():

    response = req.get(f"https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json").json()

    carpeta = os.path.dirname(os.path.realpath(__file__))
    # print(os.path.realpath(__file__))
    with open(f"{carpeta}\desfibriladores.json", "w", encoding="utf8") as desfibrilador_file:           #Encoding y ensure:ascii nos permite crear el json sin fallos de escritura
        json.dump(response, desfibrilador_file, ensure_ascii=False, indent = 4)
get_data_desfibriladores()

#CONOCER TU DATASET

# Cuántos DEAS hay en total
# Considerando solo los DEAS de los códigos postales dentro de la M-30, cuántos hay?
# Cuántos se encuentran en entidades públicas y cuántos en privadas?

def get_deas():
    with open('desfibriladores.json', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
        data = data['data']
        return data
data = get_deas()
print('Total de Deas:',len(data))


def get_titulo(datos, titulo):

    lista_publico = []
    lista_privado = []
    contador = 0

    for dea in datos:
        contador += 1 if dea["tipo_titularidad"] == titulo else 0
        lista_publico.append(dea)
    return contador
    

print('Públicas: ',get_titulo(data,'Pública'))
print('Privadas: ',get_titulo(data,'Privada'))

# def get_data(datos, titulo):

#     return len(list(filter(lambda dea: dea['tipo_titularidad'] == titulo ,datos)))

# test_a = get_data(data, 'Pública')

# print(test_a)
    


def get_cp_m_30(datos):

    cp_m30=("28029", "28036", "28046", "28039", "28016", "28020", "28002", "28003", "28015", "28010", "28006", "28028", 
    "28008", "28004", "28001", "280013", "28014", "28009", "28007", "28012", "28005", "28045" )

    contador = 0

    for dea in datos:
        contador += 1 if dea["direccion_codigo_postal"] in cp_m30 else 0
    return contador

print('Número de códigos postales en la m-30: ',get_cp_m_30(data))

# def get_cp_30(datos):

#     cp_m30=("28029", "28036", "28046", "28039", "28016", "28020", "28002", "28003", "28015", "28010", "28006", "28028", 
#     "28008", "28004", "28001", "280013", "28014", "28009", "28007", "28012", "28005", "28045" )

#     resultado = len(list(filter(lambda dea: dea['direccion_codigo_postal'] in cp_m30, datos)))
#     return resultado

def menu():
    print(' -------------------------------')
    print("DEA\n")
    print("1. Crear usuario")
    print("Salir")
menu()

user = input("Elija una opción: ")

while user.lower() != "salir":
    # Opción que me crea un usuario con contraseña y si es necesairo nuwvo usuario

    if user == "1":                      
        name = input("Nombre: ")
        password = input("Contraseña: ")
        new_user = {"name": name, "password" : password}
        
        def get_users():
            with open("users.json","w") as file:
                users = json.load(file)
                return users
        users = get_users()
        users['data'].append(new_user)
        with open ("users.json", "w") as file:
            json.dump(users, file)
        menu()
        user = input(": ")
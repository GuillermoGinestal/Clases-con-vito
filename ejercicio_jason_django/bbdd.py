import requests as req
import json
import functools
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

def cambiar_latitud(dataset):
    result = {"data": []}
    for i,dea in enumerate(dataset):
        print(i)
        try:
            latitud = utm.to_latitud(int(dea["direccion_coordenada_x"]), int(dea["direccion_coordenada_y"]), 30, "N")
        except:
            continue
        dea["direccion_coordenada_x"] = latitud[0]
        dea["direccion_coordenada_y"] = latitud[1]
        result["data"].append(dea)
    with open("deas_latitud.json", "w", encoding="utf8") as file:
        json.dump(result,file,ensure_ascii=False)

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
    print("MENÚ DEA\n")
    print("1. Crear usuario")
    print("2. Acceder")
    print("3. Salir")
menu()

user = input("\nElija una opción: ")

while user.lower() != "salir":
    # Opción que me crea un usuario con contraseña y si es necesairo nuevo usuario

    if user == "1":                      
        name = input("Nombre: ")
        password = input("Contraseña: ")
        new_user = {"name": name, "password" : password}
        
        def get_users():
            with open("users.json", "r") as file:
                users = json.load(file)
                return users
        users = get_users()
        users['data'].append(new_user)
        with open ("users.json", "w") as file:
            json.dump(users, file)
        menu()
        user = input(": ")

    elif user == "2":
        def sub_menu():
            print("-----------------")
            print("1. Buscar DEA por código")
            print("2. Buscar DEA por distancia")
            print("3. Buscar DEA por radio")
            print("4. Volver al paso anterior")
            print("-----------------")
        
        def by_code(code):
            aplicar_filtro = filter(lambda dea: dea["codigo_dea"] == code, data)
            dea = next(aplicar_filtro, "No encontrado")
            print(dea)
            sub_menu()
            user = input("Elija una opción: ")
        
        name = input("Nombre: ")
        password = input("Contraseña: ")

        with open("users.json") as file:
            users = json.load(file)["data"]
            validacion = map(lambda user: True if user['name'] == name and user['password'] == password else False, users)
            if next (validacion):
                sub_menu()
                user = input("Elija opción: ")

                # Opción que nos busca el DEA por código

                if user == "1":
                    code = input("Introduzca un código: ")
                    by_code(code)
                    sub_menu()
                    user = input("Elija opción: ")
                
                #Opción que nos busca el DEA por latitud
                elif user == "2":
                    user_x = int(input("Introduzca coordenada X: "))
                    user_y = int(input("Introduzca coordenada Y: "))
                    user_latitud=utm.to_latlong(user_x,user_y,30,"N")
                    
                    user = User(user_x, user_y)
                    dea, H = user.get_nearest_dea(data)
                    latitud = utm.to_latlong(int(dea["direccion_coordenada_x"]), int(dea["direccion_coordenada_y"]), 30, "N")
                    def get_meters(user_latitud, dea_latitud):
                        return distance.distance(user_latitud, dea_latlong).m
                    distance_meters = get_meters(userlatitud,latitud)
                    print(dea)
                    print(f"https://www.google.com/maps/search/?api=1&query={latitud[0]},{latitud[1]}")
                    print(f"https://www.google.com/maps/dir/{userlatitud[0]},+{userlatitud[1]}/{latitud[0]},{latitud[1]}")
                    print("Usted está a ",distance_meters," metros", "Hipotenusa: ", H)
                    user = input("Elija opción: ")
                
                elif user == "3":
                    user_x = input("Introduzca una coordenada X: ")
                    user_y = input("Introduzca una coordenada Y: ")
                    user_latitud = utm.to_latlong(user_x,user_y,30,"N")
                    
                    user = User(user_x, user_y)
                    deas_lista = user.get_nearest_by_radio(data, 100)
                    print(f"Se han encontrado {len(deas_lista)} D.E.A.s:")
                    all_points = f"https://www.google.com/maps/dir/{user_latitud[0]},+{user_latitud[1]}/"
                    for dea in deas_list:
                        dea_latitud = utm.to_latlon(int(dea["direccion_coordenada_x"]), int(dea["direccion_coordenada_y"]), 30, "N")
                        all_points+=f"{dea_latitud[0]},{dea_latitud[1]}/"
                    print(all_points)
                    sub_menu()
                    user = input("Elija opción: ")

            else:
                print("Usuario o contraseña incorrectos")
                menu()
                user = input("Elija opción: ")
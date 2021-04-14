import requests as req
import json
import os


def get_data_covid():

    response = req.get(f"https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json").json()

    carpeta = os.path.dirname(os.path.realpath(__file__))
    # print(os.path.realpath(__file__))
    with open(f"{carpeta}\covid.json", "w") as covid_file:
        json.dump(response, covid_file)
    
def cargar_data_covid():

    pwd = os.path.dirname(os.path.realpath(__file__))
    o = open(f"{pwd}/covid.json")
    data = json.load(o)
    data = data["data"]
    o.close()
    return data

def total_municipios(data):

    # result = set([mun["municipio_distrito"]for mun in data])
    
    result = set()

    for mun in data:
        
        result.add(mun["municipio_distrito"])
    
    return result
    

def get_tia(data):

    count = 0
    result = 0

    for mun in data:
        try:
            result += mun["casos_confirmados_totales"]
            count += 1
        except KeyError:
            result += 0
            count += 1
    return result, count

def main():

    covid_data = cargar_data_covid()
    
    print(f'Total de diccionarios: ', len(covid_data))
    # print(total_municipios(covid_data))
    print(f'El total de municipios es: ', len(total_municipios(covid_data)))
    print(f'El TIA inicial es: ', get_tia(covid_data[-200:-1]))
    print(f'El TIA final es: ', get_tia(covid_data[0:199]))

main()    


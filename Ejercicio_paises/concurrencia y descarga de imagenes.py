import requests as req
import time
import threading        # (module = threading) != Thread
# import concurrent.futures

# # start = time.perf_counter() # 0


# # def req_country(seconds):
# #     print(req.get("https://restcountries.eu/rest/v2/name/spain").json())

# # t1 = threading.Thread(target = req_country, args = [1])
# # t2 = threading.Thread(target = req_country, args = [1])

# # t1.start()
# # t2.start()
# # t1.join() 
# # t2.join()  # ESPERA A QUE T1 Y T2 HAYAN FINALIZADO!


# # finish = time.perf_counter() #(7 ---> 9) + 1

# # print(f'Delta time --> {finish-start}')


# def get_spain(pais):
#     response = req.get(f"https://restcountries.eu/rest/v2/namë{country}")
#     return response


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(get_country) # == threading.Thread(target= funcion que queremos ejecutar, args = ["spain"] introducimos los valores que necsitamos)
#     print("Loading...")
#     print(future.result())

#? DESCARGA DE IMAGENES

response = req.get("https://1.bp.blogspot.com/-DDJN8nchqxk/XYBjYHJLTWI/AAAAAAAAEUo/MpcZgT8ZXr8-y_zbXkmvymUFhDd8xyuvwCLcBGAsYHQ/s640/baboon.jpg")

with open("babuino.jpg", "wb") as img:     #Hay que poner el formato del archivo y convertirlo en binario(wb)
    img.write(response.content)
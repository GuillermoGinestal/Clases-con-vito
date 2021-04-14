
#?CSV

# path = './MPP - Máster Programación Python - Oficial Python Institute/Unidad 12/M-509'

#! APERTURA - ABRIR FICHERO / CERRADO DE FICHEROS

# fichero = open( path+'/fichero.csv', 'w')

# fichero.close()


#! LECTURA - READER

# import csv

# fichero = open( path+'/fichero.csv', 'r')

# lectura = csv.reader(fichero) 
# for fila in lectura:
#     print(fila)

# fichero.close()

#! LECTURA - READLINE

# fichero = open( path+'/fichero.csv', 'r')

# print( fichero.readline() )

# fichero.close()

#! LECTURA - READLINES

# fichero = open( path+'/fichero.csv', 'r')

# print( fichero.readlines() )

# fichero.close()

#! ESCRITURA - WRITE

# fichero = open( path+'/fichero.csv', 'a')

# fichero.write('\n')
# fichero.write('HOLA QUE TAL')

# fichero.close()

#! ESCRITURA - WRITELINES

# fichero = open( path+'/fichero.csv', 'w')

# lista = ['benjamin\n', 'evander\n', 'ciriaco\n']
# fichero.write('\n')
# fichero.writelines(lista)

# fichero.close()


#? EJERCICIO
#? escriba y lea un archivo CSV 
#? con el formato siguiente:

# import csv


# path = './MPP - Máster Programación Python - Oficial Python Institute/Unidad 12/M-509'

# ESCRITURA
# fichero = open( path+'/fichero.csv', 'a')
# fichero.write(f'Patricia,Herresanchez,15-09-71,223233444T,iglesia2,patricia@gmail.com,jfjfur123∑,True,40000,partido')
# fichero.close()


#* fichero.csv ( recuerde separado por comas ',' y sin espacios )
#* nombre,apellido,fecha_de_nacimiento,dni,direccion,email,clave,activo,salario,horario
#? Patricia,Herresanchez,15-09-71,223233444T,iglesia2,patricia@gmail.com,jfjfur123∑,True,40000,partido


# LECTURA
# fichero = open( path+'/fichero.csv', 'r')
# lectura = csv.reader(fichero) 
# for fila in lectura:
#     print(fila)
# fichero.close()

#* fichero.csv ( recuerde separado por comas ',' y sin espacios )
#* nombre,apellido,fecha_de_nacimiento,dni,direccion,email,clave,activo,salario,horario
#? ['Patricia', 'Herresanchez', '15-09-71', '223233444T', 'iglesia2', 'patricia@gmail.com', 'jfjfur123∑', 'True', '40000', 'partido']

#! Prueba facil de csv

import csv

class Fruta:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    
    def __str__(self):
        return f'{self.nombre}:{self.cantidad}'

lista_frutas = []

fichero = open('C:/Users/cice/Desktop/practica csv/prueba.csv', 'r')

lectura = csv.reader(fichero)

for fila in lectura:
    
    frut =  Fruta(fila[0], fila[1])
    lista_frutas.append(frut)
    print(frut)

fichero.close()


lista_frutas.append(Fruta('Ciriaquito', '123'))
lista_frutas.append(Fruta('evandercito', '5'))
lista_frutas.append(Fruta('Limoncito', '6'))

fichero = open('C:/Users/cice/Desktop/practica csv/prueba2.csv', 'w')

primera_linea = True
for fruta in lista_frutas:
    cadena = ''
    
    if primera_linea == True:
        caderna = f'{fruta.nombre}:{fruta.cantidad}'
        primera_linea = False
    else:
        cadena = f'\n{fruta.nombre}:{fruta.cantidad}'
    
    fichero.write(cadena)

fichero.close()
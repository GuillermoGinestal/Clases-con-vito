
#? CSV

 #! APERTURA - ABRIR FICHERO


#fichero = open('fichero.csv', 'w')

#fichero.close()

#! LECTURA - READLINE

import csv

fichero = open('fichero.csv', 'r')

lectura = csv.reader(fichero)

for fila in lectura:
    print(fila)


fichero.close()



#! ESCRITURA  



#! ESCRITURA 



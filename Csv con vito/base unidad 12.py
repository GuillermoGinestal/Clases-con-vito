 #! APERTURA - ABRIR FICHERO


# fichero = open('fichero.txt', 'r')

# print(fichero.read())

# texto = fichero.read()
# for t in texto:
#     print(t)
# fichero.close()
#! LECTURA - READLINE

# fichero = open('fichero.txt', 'r')

# print(fichero.readlines())          #Te devuelve una lista con saltos de línea
# print(fichero.readline())           #Te devuelve la línea que asignes
#  fichero.close()

#! ESCRITURA - READLINE    

# fichero = open('fichero.txt', 'w')
#                                         #Te permite escribir en el fichero, y reemplazar lo que ya tienes escrito
# fichero.write('\n')
# fichero.write('tweeter')

# fichero.close()

#! ESCRITURA - WRITELINES

# fichero = open('fichero.txt', 'a')

# Lista = ['\nGuillermo', '\nPablo', '\nCiriaco']         #Con la a añades lo introducido al fichero

# fichero.write('\n')
# fichero.writelines(Lista)

# fichero.close()







# Program A1. PSP0, Problem 1
# Programmer: José Eduardo Hernández Rodríguez

# TODO: Requerimientos: ALmacenar en un archivo y leer de un archivo una serie 
# TODO: n números reales. El programa debe aceptar enteros o números reales
# TODO: como entradas pero debe almacenarlos como números reales. Las funciones
# TODO: de usuario que ofrece este programa son las siguientes:
# * 1) El usuario introduce el nombre del archivo
# * 2) El usuario introduce el número de datos a almacenar
# * 3) Para modo lectura, el programa muestra en la pantalla los números
# *    del archivo, uno por línea
# * 4) Para escritura, el usuario introduce la cantidad de números a ser grabada, 
# *    seguido por la entrada de todos los números, uno a la vez

# Function to create a csv file with a personalized name

def createFile():
    fileName = input("Enter the name of the file: ")
    fileName = fileName + ".csv"
    file = open(fileName , "w")
    file.close()


if __name__ == "__main__":
    createFile()
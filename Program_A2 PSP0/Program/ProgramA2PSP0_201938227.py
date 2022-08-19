# Program A1. PSP0, Problem 1
# Programmer: José Eduardo Hernández Rodríguez

# TODO: Requerimientos: ALmacenar en un archivo y leer de un archivo una serie 
# TODO: n números reales. El programa debe aceptar enteros o números reales
# TODO: como entradas pero debe almacenarlos como números reales. Las funciones
# TODO: de usuario que ofrece este programa son las siguientes:

# * 1) El usuario introduce el nombre del archivo
# Function to create a txt file with a personalized name and save in the directory "Program"

dir = "Program/"
def createFile():
    # We get the name of the file
    fileName = input("Enter the name of the file: ")
    # We create the file
    file = open( dir + fileName + ".txt", "w")
    # We close the file
    file.close()

# * 2) El usuario introduce el número de datos a almacenar
# Function to select the mood: read or write
def selectMood():
    mood = input("Enter the mood: ")
    if mood == "read":
        readFile()
    elif mood == "write":
        writeFile()
    else:
        print("Invalid mood")

# * 3) Para modo lectura, el programa muestra en la pantalla los números del archivo, uno por línea
# Function to read the file
def readFile():
    # We get the name of the file
    fileName = "prueba.txt"
    file = open(dir+fileName , "r")
    for line in file:
        print(line)
    file.close()

# * 4) Para escritura, el usuario introduce la cantidad de números a ser grabada, 
# *    seguido por la entrada de todos los números, uno a la vez

# Function to write in the file
def writeFile():
    # We get the name of the file
    fileName = "prueba.txt"
    file = open(dir+fileName , "w")
    # We get the number of data to save
    numData = int(input("Enter the number of data to save: "))
    # We get the data
    for i in range(numData):
        data = float(input("Enter the data: "))
        file.write(str(data) + "\n")
    file.close()




if __name__ == "__main__":
    createFile()
    selectMood()
    selectMood()
    selectMood()

# Program A2, PSP0
# Programmer: José Eduardo Hernández Rodríguez

# TODO: Requerimientos: Almacenar en un archivo y leer de un archivo una serie 
# TODO: n números reales. El programa debe aceptar números reales
# TODO: como entradas pero debe almacenarlos como números reales. Las funciones
# TODO: de usuario que ifrece este programa son las siguientes

import os

class File:
    def __init__(self):
        self.fileName = None
    # Function to create a txt file with a personalizated name and save in the directory "Program"

    # * 1 ) El usuario introduce el nombre del archivo
    def createFile(self,fileName):
        # We create the file 
        file = open( "txt/" + fileName +  ".txt", "w" )
        # We close the file
        file.close()
    
    # Function to select the mood: read or write
    # * 2) El usuario introduce el número de datos a almacenar
    def selectMood(self):
        mood = input("Enter the mood (r: read, w: write): ")
        if mood == "r":
            file.readFile()
        elif mood == "w":
            file.writeFile()
        else:
            print("Invalid mood")
    
    # Function to read the file
    # * 3) Para modo lectura, el programa muestra en la pantalla los números del archivo, uno por línea
    def readFile(self):
        # We get the name of the file
        file = open("txt/" + self.fileName , "r")
        for line in file:
            print(line)
        file.close()

    # * 4) Para escritura, el usuario introduce la cantidad de números a 
    # * ser grabada, seguido por la entrada de todos los números, uno a la vez

    # Function to write in the file
    def writeFile(self):
        # We get the name of the file
        file = open("txt/" + self.fileName, "w")
        # We get the number of data to save
        numData = int(input("Enter the number of data to save: "))
        # We get the data
        for i in range(numData):
            data = float(input("Enter the data: "))
            file.write(str(data) + "\n")
        file.close()

if __name__ == "__main__":
    op = 1
    while (op != 0):
        print("1. New file")
        print("2. Select a file")
        print("3. Select mood")
        print("0. Exit")
        op = int(input("Select a option: "))
        if op == 1:
            file = File()
            # We get the name of the file
            fileName = input("Enter the name of the file: ")
            file.createFile(fileName)
        elif op == 2:
            files = os.listdir("txt")
            print("\n")
            for i in range(len(files)):
                print(f"[{i}]: "+files[i])
            print("\n")
            file_to_open = int(input("Select a file: "))
        elif op == 3:
            file = File()
            file.fileName = str(files[file_to_open])
            print(str(file.fileName))
            file.selectMood()
# Program A3. PSP0
# Programmer: José Eduardo Hernández Rodríguez

# TODO: Requerimientos: Almacenar en un archivo y leer de un archivo una serie 
# TODO: n números reales. El programa debe aceptar números reales
# TODO: como entradas pero debe almacenarlos como números reales. Las funciones
# TODO: de usuario que ifrece este programa son las siguientes

# TODO: Con los datos almacenados, calcular la desviación estandar de la muestra
# TODO: de n numeros, se usa una lista ligada para almacenar los n numeros 

import os

# Definition of the class "Node"
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definition of the class "LinkedList"
class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert(self, data):
        # if not exist any node in the list we create the first node with the data value
        if self.head is None: 
            self.head = Node(data)
        else:
            # We create a temporal node to not lose the head of the list
            temp = self.head
            # We go to the last node
            while temp.next:
                temp = temp.next
            # We create a new node with the data value
            temp.next = Node(data)

    def mean(self):
        # We create a temporal node to not lose the head of the list
        temp = self.head
        # We initialize the sum of the numbers
        sum = 0
        # We initialize the number of elements in the list
        n = 0
        # We sum the data of the nodes until the last node
        while temp:
            sum += temp.data
            n += 1
            temp = temp.next
        # We calculate the mean
        mean = sum / n
        return mean
    
    def print_list(self):
        # We create a temporal node to not lose the head of the list
        temp = self.head
        # We print the data of the nodes until the last node
        while temp:
            print(temp.data)
            temp = temp.next
    
def stdv(list):
    # We calculate the standard deviation of the list
    # We create a temporal node to not lose the head of the list
    temp = list.head
    # We initialize the sum and the counter
    sum = 0
    counter = 0
    # We calculate the mean
    mean = list.mean()

    # We sum the data of the nodes until the last node
    while temp:
        sum += (temp.data - mean)**2
        counter += 1
        temp = temp.next
    # We calculate the standard deviation
    print(f'sum: {sum}')
    print(f'counter: {counter}')
    stdv = (sum / (counter-1))**0.5
    return stdv

class File:
    def __init__(self):
        self.fileName = None
        self.numData = 0
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
        self.numData = int(input("Enter the number of data to save: "))
        # We get the data
        for i in range(self.numData):
            data = float(input("Enter the data: "))
            file.write(str(data) + "\n")
        file.close()

if __name__ == "__main__":
    op = 1
    while (op != 0):
        print("1. New file")
        print("2. Select a file")
        print("3. Select mood")
        print("4. Calcule the standard deviation")
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
            file.numData = len(file.fileName)
            print(str(file.fileName))
            file.selectMood()
        elif op == 4:
            print(f"Using: {file.fileName}")
            list = LinkedList()
            file_ = open("txt/" + file.fileName , "r")
            for i in file_:
                list.insert(float(i))
            list.print_list()
            print("The standar deviation of the sample is: ", stdv(list))
        elif op == 0:
            print("Bye")
        else:
            print("Invalid option")
# We has gotten the code of PSP0_201938227.py and PSP0_A2_201938227.py
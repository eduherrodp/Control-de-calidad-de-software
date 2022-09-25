# Program B1, PSP0.1
# Programmer: José Eduardo Hernández Rodríguez

# TODO: Instructions
# ! First you need to write a program to count the total program LOC, the total LOC in each object. 
# ! Produce a single LOC count for an entire source program file and separate LOC and method counts for each object. 
# * Print out each object name together with its LOC and method counts. 
# * Also print out the total program LOC count. If an object-oriented language is not used, count the procedure and function LOC and print out the procedure and function names and LOC counts.
# ? Second, your program must indentify modified, deleted, and reused LOC and list them as well when a new version of an existing program is available.

import os

# We define the class that will contain the information of the files

class File:
    def __init__(self, name, path) -> None:
        self.name = name
        self.path = path
        self.methods = 0
        self.objects = 0
        self.numCodeLines = 0

    def __str__(self) -> str:
        return f"[FILE]\nName: {self.name}, Path: {self.path}, Methods: {self.methods}, Objects: {self.objects}, Lines: {self.numCodeLines}"

    # We define the read function that will read the file
    def read(self) -> str:
        with open(self.path, "r") as file:
            self.content = file.read()
        return self.content

    # Function to count the number of lines of code
    def countCodeLines(self) -> int:
        # We count the number of comments
        numComments = self.content.count("#")
        # Count the number of blank lines in the file
        numBlankLines = 0
        for line in self.content.splitlines():
            if line.strip() == "":
                numBlankLines += 1

        # We count the number of lines of code
        self.numCodeLines = self.content.count("\n") +1 - numComments - numBlankLines

        return self.numCodeLines

    # Function to count the number of methods in the file
    def countMethods(self) -> int:
        # We count the number of methods
        self.methods = self.content.count("def ")
        return self.methods

    # Function to count the number of objects in the file
    def countObjects(self) -> int:
        # We count the number of objects
        self.objects = self.content.count("class ")
        return self.objects

# Define the object that will contain the information of the objects

class Object:
    def __init__(self, name, lines) -> None:
        self.name = name
        self.lines = 0

    def __str__(self) -> str:
        return f"[OBJECT]\nName: {self.name}, Lines: {self.lines}"


if __name__ == "__main__":
    # Verify if the program is executed from the path root
    path_root = os.getcwd()
    # Only verify if the path ends with the name of the folder
    if path_root.endswith("\\Program"):

        # First, show the programs in the directory "/Programs"
        files = os.listdir("Programs")
        print("The programs in the directory are:")
        for i in range(len(files)):
            print(f"[{i}]: "+files[i])

        file_to_open = int(input("Select a file: "))
        file = File(files[file_to_open], "Programs/"+files[file_to_open])
        file.name = str(files[file_to_open])

        # ! (Only for reference) Print the information of the object File
        # print("\nInformation before the method call: \n"+file.__str__()+"\n")

        # We read the file and call all the methods for fill the information of the object
        file.read()
        file.countCodeLines()
        file.countMethods()
        file.countObjects()

        # Print the information of the object File
        print("Information after the method call: \n"+file.__str__()+"\n")

    else:
        print("Please execute the program from /Program")
        exit(1)

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
        self.lines = 0

    def __str__(self) -> str:
        return f"Name: {self.name}, Path: {self.path}, Methods: {self.methods}, Objects: {self.objects}, Lines: {self.lines}"

    # We define the read function that will read the file
    def read(self) -> str:
        with open(self.path, "r") as file:
            self.content = file.read()
        return self.content

    # Function to count the numbers of comments in the file
    def countComments(self) -> int:
        # We count the number of comments
        self.numComments = self.content.count("#")
        return self.numComments
    
    # Function to count the number of lines in blank
    def countBlankLines(self) -> int:
        # We count all the lines in blank
        self.numBlankLines = 0
        for line in self.content.splitlines():
            if line.strip() == "":
                self.numBlankLines += 1
        return self.numBlankLines

    # Function to count the number of lines of code
    def countCodeLines(self) -> int:
        # We count the number of lines of code
        self.lines = self.content.count("\n") + 1
        return self.lines


if __name__ == "__main__":
    # Verify if the program is executed from the path root
    print(os.getcwd())
    path_root = os.getcwd()
    # Only verify if the path ends with the name of the folder
    if path_root.endswith("\\Program"):
        print("The program is executed from the path root")


    else:
        print("Please execute the program from /Program")
        exit(1)

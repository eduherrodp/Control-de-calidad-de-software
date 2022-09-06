# Program B1, PSP0
# Programmer: José Eduardo Hernández Rodríguez

# Class File
import os

class File:
    def __init__(self):
        self.name = None

    def read(self):
        # We read the file
        with open("Programs/"+self.name, "r") as file:
            self.content = file.read()
        return self.content

    # Function to count the numbers of comments in the file
    def countComments(self):
        # We count the number of comments
        self.numComments = self.content.count("#")
        return self.numComments

    # Function to count the number of lines in blank
    def countBlankLines(self):
        # We count all the lines in blank
        self.numBlankLines = 0
        for line in self.content.splitlines():
            if line.strip() == "":
                self.numBlankLines += 1
        return self.numBlankLines

    # Function to count the number of lines with code
    def countCodeLines(self):
        # We count the number of lines with code
        self.numCodeLines = self.content.count("\n") +1
        return self.numCodeLines

if __name__ == "__main__":
    files = os.listdir("Programs")
    for i in range(len(files)):
        print(f"[{i}]: "+files[i])
    print("\n")
    file_to_open = int(input("Select a file: "))
    file = File()
    file.name = str(files[file_to_open])

    # Print the name of the file that we are going to read

    print("Using: " + file.name)

    # We read the file
    file.read()

    # We show the number of comments in the file
    # print("Number of comments: " + str(file.countComments()))

    # We show the number of blank lines in the file
    # print("Number of blank lines: " + str(file.countBlankLines()))

    # We show the number of code lines in the file
    # print("Number of code lines: " + str(file.countCodeLines()))

    # We show the logical lines of code
    print("Logical lines of code: " + str(file.countCodeLines() - file.countComments() - file.countBlankLines()))
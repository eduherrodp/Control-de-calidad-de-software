# Program B1, PSP0
# Programmer: José Eduardo Hernández Rodríguez

import os

class File: 
    def __init__(self):
        self.fileName = None
    # Function to read a py file

    def loc(self):
        count = 0
        totals = 0
        file = open("Programs/"+ self.fileName, "r")
        for line in file:
            line = line.strip()
            line = line.split("\n")
            # print(line)
            for char in line:
                if char == "#":
                    count+=1
                    continue
                if char == '':
                    count+=1
                    continue    
            totals += 1
        
        final = totals-count
        print(f"LOC: {str(final)}")
        file.close()


if __name__ == "__main__":
    op = 1
    while(op != 0):
        print("1. Select file")
        print("0: Exit")
        op = int(input("Select a option: "))
        if op == 1:
            files = os.listdir("Programs")
            print("\n")
            for i in range(len(files)):
                print(f"[{i}]: "+files[i])
            print("\n")
            file_to_open = int(input("Select a file: "))
            file = File()
            file.fileName = str(files[file_to_open])
            print(str(file.fileName))

            file.loc()
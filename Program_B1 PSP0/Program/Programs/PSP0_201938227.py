# Program A1. PSP0, Problem 1
# Programmer: José Eduardo Hernández Rodríguez

# * Program to estimate the mean and standar deviation of a 
# * sample of n real numbers. The mean is the average of the
# * numbers.

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
    stdv = (sum / counter)**0.5
    return stdv
    
if __name__ == "__main__":
    # Create a LinkedList
    list = LinkedList()
    # Get the number of elements of the sample
    n = int(input("Enter the number of elements of the sample: "))
    # Get the elements of the sample
    for i in range(n):
        list.insert(float(input("Enter the element: ")))
    # Print the mean and the standar deviation of the sample

    # Print the list
    list.print_list()

    print("The standar deviation of the sample is: ", stdv(list))

# End of the program
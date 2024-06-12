class Person:
    def __init__(self, name):
        self.name = name
        self.list = []

    def split(self, item, num):
        flag = True
        numbers = []
        while flag:
            separate = input(f"hello {self.name} there are {item.quantity} unit\ndivide it to {num} part using space for separating: ")
            numbers = [int(n) for n in separate.split(" ")]
            if sum(numbers) == item.quantity and num == len(numbers):
                flag = False
        item.split(numbers)

    def pick(self, item):
        print(f"hello {self.name} these items are available : ")
        item.printDetails()
        return item.splitList[int(input("please choose an index: "))]

    def add(self, item):
        self.list.append(item)
        item.parent.splitList.remove(item)


class Item:
    def __init__(self, name, quantity, parent=None):
        self.name = name
        self.quantity = quantity
        self.splitList = []
        self.parent = parent

    def split(self, numbers):
        for i in range(len(numbers)):
            self.splitList.append(Item(f"{self.name}/{i+1}of{len(numbers)}", numbers[i], self))

    def printDetails(self):
        for i in range(len(self.splitList)):
            print(f"{i} - {self.splitList[i].name} : {self.splitList[i].quantity}")
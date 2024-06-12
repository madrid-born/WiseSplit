from Classes import Person, Item
from Split2 import split2
from Split3 import split3

P = [Person(f"p{i+1}") for i in range(3)]

X = Item("Cake", 100)

split3(P, X)

for person in P:
    print(f"{person.name} :")
    sum = 0
    for item in person.list:
        sum += item.quantity
        print(f"{item.name} : {item.quantity}")
    print(f"in total {sum}\n")

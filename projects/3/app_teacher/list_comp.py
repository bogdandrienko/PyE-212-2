fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
# print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
# print(newlist)

list1 = [" apple ", " banana ", " cherry ", "kiwi ", " mango"]
list2 = [str(char).strip() for char in list1 if "i" in char and len(str(char).strip()) > 3]
print(list2)

list3 = [str(x).strip() for x in "Яблоко, банан, груша       , киви      ".split(",")]
print(list3)

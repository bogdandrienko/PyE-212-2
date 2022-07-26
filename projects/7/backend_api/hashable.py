import hashlib
from traceback import print_last

# hash_object = hashlib.md5("12345".encode())
hash_object = hashlib.sha256("key1".encode('utf-8'))
print(hash_object.hexdigest())

dict1 = {
    "key1": {"key1": {
        "key1": {"key1": "value1"},
        "key2": {"key1": "value1"},
    }},
    "key2": {"key1": "value1"},
}


numbers_orig = [5, 2, 6, 7, 8, 12, 15, 111]
words_orig = ["hello", 'Alice', "ball", 'eleven', '12']











def myBubbleSort(myList):
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j]<myList[j+1]:
                temp=myList[j]
                myList[j]=myList[j+1]
                myList[j+1]=temp

print("Original list:")
print(numbers_orig)
myBubbleSort(numbers_orig)
print("Sorted list:")
print(numbers_orig)







class A:
    val1 = 12
    def __init__(self, val1) -> None:
        self.val = val1
        self.__val2 = val1 + 5
    
class B:
    val2 = 12
    def __init__(self, val1) -> None:
        pass
    
A.val1
A.val
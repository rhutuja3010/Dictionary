# Q25. Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}


dic={}
for i in range(10):
    latter=input("enter the latter: ")
    number=int(input("enter the number: "))
    dic.update({latter:number})
print(dic)

# Q47.
# A Python Dictionary contains List as value. Write a Python program to clear the list values in
# the said dictionary.
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

d= {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
l=[]
for i in d:
    d.update({i:l})
print(d)
    
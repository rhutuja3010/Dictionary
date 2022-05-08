# // # Q40. Write a Python program to convert more than one list to nested dictionary.
# // # Original strings:
# // # ['S001', 'S002', 'S003', 'S004']
# // # ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# // # [85, 98, 89, 92]
# // # Nested dictionary:
# // # [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
# // # {'S004': {'Saim Richards': 92}}]


a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
l=[]
d1={}
for i in range(len(a)):
    d1.update({a[i]:{b[i]:c[i]}})
l.append(d1)
print(l)
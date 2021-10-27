list1=[]
information={}
name=["username","password","description","date_of_birth","hobby","gender"]
infor=[1,2,3,3,4,5]
for i in range(len(name)) :
    information.update({name[i]:infor[i]})
    list1.append({name[i]:infor[i]})
print(list1)
print(information)
# {1: 10, 2: 60, 3: 30,  5: 50, 6: 60} 

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for key in dic2:
    if key in dic1:
        dic1[key]=dic1[key]+dic2[key]
        dic1.update(dic3)
    else:
        dic1[key]=dic2[key]
print(dic1)






# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
        
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print (len(fruit))
# print(fruit)


# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print (len(Details["Student"])) 


# my_dict = {}
# my_dict [(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict)






# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates[box]))




# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)










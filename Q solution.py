# string="w3resource"
# count={}
# for i in string:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)


# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1:
#     if i in d2:
#         d2[i]=d1[i]+d2[i]
#     else:
#         d2[i]=d1[i]
# print(d2)


# table={}
# for i in range(1,6):
#     # table[i]=i*i
#     table.update({i:i*i})
# print(table) 



# Q37.Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]

# dic={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# for i in dic:
#     print(dic[i][4])




# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

# dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
# for x,y in dict(dic).items():
#     if y==None:
#         del dic[x] 
# print(dic)



# dic={'Cierra Vega':175,'Alden Cantrell':180,'Kierra Gentry':165,'Pierre Cox':190}
# dic1={}
# for i in dic:
#     if dic[i]>170 :
#         dic1.update({i:dic[i]})
# print(dic1)



# a=["r","h","u","t","u"]
# print("".join(a))
# s=1
# for i in range(len(a)):
    # s=str(s)+str(a[i])
# print(s)



# table={}
# for i in range(1,16):
#     # table[i]=i*i
#     table.update({i:i*i})
# print(table)

# dic=['s001','s002','s003','s004']
# dic1=['Adina Park','Leyton Marsh','Duncan Boyle','Saim Richards']
# dic2=[85,98,89,92]
# a=[]
# b={}
# i=0
# while i<len(dic):
#     d={dic1[i]:dic2[i]}
#     e={dic[i]:d}
#     a.append(e) 
#     i+=1
# print(a)




# add={0:10,1:20}
# add.update({2:30})
# print(add)


# a_add={**add,**{2:30}}
# print(a_add)


# # output={1:10,2:20,3:30,4:40,5:50,6:60}
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in (dic1,dic2,dic3):
#     dic4.update(i)
# print(dic4)


# my_dict={'name':'Rhutuja','surname':'Patil','Age':21}
# input=input("enter the input  : ")
# if input in my_dict:
#     print("exist")
# else:
#     print("not exist")



# Q32.Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Sample Output:

# key  value  count                                                                                             
# 1     10      1                                                                                               
# 2     20      2                                                                                               
# 3     30      3                                                                                               
# 4     40      4                                                                                               
# 5     50      5                                                                                               
# 6     60      6
# dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key", "value", "count")
# count=0
# for i in dic:
#     count+=1
#     print(i,"   ",dic[i],"  ",count)



# # Q25. Write a Python program to create a dictionary from a string. 
# # Note: Track the count of the letters from the string.
# # Sample string : 'w3resource'
# # Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}


# dic={}
# for i in range(10):
#     latter=input("enter the latter: ")
#     number=int(input("enter the number: "))
#     dic.update({latter:number})
# print(dic)


# # Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# # Original Dictionary:
# # {'c1': 'Red', 'c2': 'Green', 'c3': None}
# # New Dictionary after dropping empty items:
# # {'c1': 'Red', 'c2': 'Green'}


# dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
# del (dic['c3'])
# print(dic)

# list1=[]
# information={}
# name=["username","password","description","date_of_birth","hobby","gender"]
# infor=[1,2,3,3,4,5]
# for i in range(len(name)) :
#     information.update({name[i]:infor[i]})
#     list1.append({name[i]:infor[i]})
# print(list1)
# print(information) 




# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# # d={}
# # for i in (dic1,dic2,dic3):
# #     d.update(i)
# # print(d)

# for key in dic2:
#     if key in dic1:
#         dic1[key]=dic1[key]+dic2[key]
#         dic1.update(dic3)
#     else:
#         dic1[key]=dic2[key]
# print(dic1)

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
# # print(my_dict)

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



# dict =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# count=0
# sum=[]
# for i in dict.values():
#     sum+=i
# print(sum)
# i=0
# while i<len(sum):
#     count+=1
#     i+=1
# print(count)

# # output [58,56,100]

# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# l=[]
# for i in range(3):
#     max=0
#     for j in my_dict:
#         if max<my_dict[j]:
#             max=my_dict[j]
#             c=j
#     l.append(my_dict[c])
#     my_dict.pop(c)
# print(l)

# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# l=[]
# for i in range(3):
#     max=0
#     for j in my_dict:
#         if max<my_dict[j]:
#             max=my_dict[j]
#             c=j
#     l.append(my_dict[c])
#     my_dict.pop(c)
# print(l)

        


# # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# squre_dic={}
# for i in range(1,16):
#     squre_dic[i]=i*i
# print(squre_dic)




# # Write a program to sort a dictionary in ascending or descending according to its values .

# # Input :-

# # {'bijender':45,'deepak':60,'param':20,"anjili":30,"roshini":50}

# import operator 
# Dictionary={'bijender':45,'deepak':60,'param':20,"anjili":30,"roshini":50}

# asc=dict(sorted(Dictionary.items(),key=operator.itemgetter(1)))
# print(asc)

# dsc=dict(sorted(Dictionary.items(),key=operator.itemgetter(1),reverse=True))
# print(dsc)



# # If input is “name” then output will be “exist”
# # If input is “class” then output will be “not exists”.

# dict = {"name":"Raju", "marks":56}
# input=input("enter the name:")
# if input in dict:
#     print("exist")
# else:
#     print("not exist")


# my_dict = {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#        } 
# sum=0
# for i in my_dict.values():
#     # print(i)
#     sum+=i
# print(sum)




# Dic= {
#         1: 'NAVGURUKUL',
#         2: 'IN',  
#           3:{    
#              'A' : 'WELCOME',
#              'B' : 'To',
#              'C' : 'DHARAMSALA'
#             }
#         }

# del Dic[3]['A']
# print(Dic)


# # output:
# # {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# d={} 
# for i in range (len(list1)):
#     d [list1[i]] = list2[i]
# print(d)


# # output:
# #     {“ball”:”red”,”bat”:4,”wickets”:8}

# dic={
#     "ball":"red",
#     "bat":4,
#     "wickets":8,
#     "ball":"green",
#     "bat":3
#     }
# duplicate={}
# for i in duplicate:
#     if i not in duplicate:
#         duplicate.update(i)
# print(dic)



# # ['2', '7', '9', '5', '1'] 


# a=[
#      {"first":"1"}, 
#      {"second": "2"}, 
#      {"third": "1"}, 
#      {"four": "5"}, 
#      {"five":"5"}, 
#      {"six":"9"},
#      {"seven":"7"}
# ]
# l=[]
# for i in a:
#     for j in i.values():
#         if j not in l:
#             l.append(j)
# print(l)

    
# output:  {
#     'Sonu':98,
#     'Shab':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#   'Shibad':56} 



# d={}
# for i in range(10):
#     name = input("enter the name")
#     marks = int(input("enter the marks"))
#     d.update({name:marks})
# print(d)


# a=['a','b','c','d']
# l=[]
# b=''
# for i in a:
#     b=b+i
# l.append(b)
# print(l)



# # {'M':1,'I':4,'S':4,'P':2}

# string=input("enter the string")
# count={}
# for i in string:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)



# word = string.split()
# fre = [word.count[i] for i in range]
# mydic=dic(zip(word , fre))
# # count+=1
# print(mydic)


# a="welcome to Python programming"
# print(a[::-1])
# print(a.lower())
# print(a[-3::1])
# print(a[0].upper()+a[1:-1]+a[-1].upper())



# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+i
# print(sum)

# c={}
# n={i:i ** 2 for i in range(1,16)}
# print(n)

# c=dict()
# for i in range(1,16):
#     c=i*i
# print(c)  


# c={}
# for i in range(1,16):
#     c[i]=i*i
# print(c) 



# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# d={'a':1,'b':2,'c':3,'d':4}
# c={}
# for i in (s,a,d):
#     c.update(i)
# print(c)


# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     s.update(a)
# print(s)


# # s.update(a)
# # print(s)

# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }

# print(details["name"])
# print(details["lastname"])
# print(details["age"])



# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org"
#     }
# print(details["name"])
# print(details["email"])
# print(details["age"])


# a=[1,4,6,7,5,6,]
# b={}
# for i in a[::-1]:
#         b={i:b}
# print(b)

# student = {"Ankit":78,"Sonu":67,"Monu":90,"Rushu":98,"Piyu":80}
# highest = max (student,key = student.get)
# highestmarks = max (student.values())
# print("student with highest marks is ",highest,"scoling",highestmarks)
# lowest = min (student ,key = student.get )
# lowestmarks = min (student.values())
# print("student with liwest marks is ",lowest,"scoling",lowestmarks)




# a=[1,3,5,[2,3],[5,6],[4,[6,7],1]]
# sum=0
# for i in range(len(a)):
#     if type(a[i])==list:
#         for j in a[i]:
#             sum+=a[i][j]
#             if type(a[i][j])==list:
#                 for k in range(len(a)):
#                     sum+=a[i][j][k]
#     else:
#         sum+=a[i]
# print(sum)
# a=[1,3,5,[2,3],[5,6],[4,[6,7],1]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while  j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                     sum+=a[i][j][k]
#                     k+=1
#             else:
#                 sum+=a[i][j]
#             j+=1
#     else:
#         sum+=a[i]
#     i+=1
# print(sum)




# a=[1,2,[3,4],3,4,[7,8,9],3]
# sum=[]
# sum1=0
# for i in range(len(a)):
#     if type(a[i])==list:
#         for j in range(len(a[i])):
#             sum.append(a[i][j])
#             sum1+=a[i][j]
#     else:
#         sum.append(a[i])
#         sum1+=a[i]
# print(sum)
# print(sum1)


# a=[4,0,9,3,1,2,5,8,6,7]
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             b=a[j]
#             a[j]=a[j+1]
#             a[j+1]=b
# print(a)

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(j,end=" ")
#         j+=1
#     i+=1
#     print()

# a=[1,2,3,4,5,6,7,8,9]
# print(a[2::8])


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist) 


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist) 


# a={'c1':[1,2,3],'c2':[3.5],'c3':[8,9]}
# d={}
# for k,v in a.items():
#     v.clear()
#     d.update({k:v})
# print(d)

# def Join():
#     s=['a','b','c','d']
#     l=[]
#     b=''
#     for i in s:
#         b+=i
#     l.append(b)
#     print(l)
# Join()

# def Append():
#     a=[3,6]
#     print(a+[8])
# Append()


# s="My Name Is Rhutuja"
# l=[]
# i=0
# while i<len(s):
#     if s[i]!=' ':
#         l.append(s[i])
#     i+=1
# print(l)

# def SPLIT():
    # s="My Name Is Rhutuja"
#     l=[]
#     i=0
#     while i<len(s):
#         if s[i]!=' ':
#             l.append(s[i])
#         i+=1
#     print(l)
# s="My Name Is Rhutuja"
# SPLIT()


# def TITLE():
#     d=list1[0].split()
#     mylist=[]
#     for i in d:
#         k=" "
#         for j in range(len(j)):
#             if j==d:
#                 g=i[j].upper()
#                 k+=g
#             else:
#                 k+=i[j]
#         mylist.append(k)
#     print(' '.join(mylist))
# list1=["my name is"]
# TITLE()


# string1=['i im rhutuja patil']
# SPLIT=string1[0].split()
# # print(SPLIT)
# l=[]
# for i in range(len(SPLIT)):
#     s=''
#     for j in range(len(SPLIT[i])):
#         if j==0:
#             s+=SPLIT[i][0].upper()
#         elif j!=0:
#             s+=SPLIT[i][j]
#     l.append(s)
# print(l)


# def TITLE():

#     l=[]
#     for i in range(len(SPLIT)):
#         s=''
#         for j in range(len(SPLIT[i])):
#             if j==0:
#                 s+=SPLIT[i][0].upper()
#             elif j!=0:
#                 s+=SPLIT[i][j]
#         l.append(s)
#     print(l)
# string1=['i im rhutuja patil']
# SPLIT=string1[0].split()
# TITLE()

# string1=['i im rhutuja patil']
# SPLIT=string1[0].split()
# # print(SPLIT)
# l=[]
# for i in range(len(SPLIT)):
#     s=''
#     for j in range(len(SPLIT[i])):
#         if j==0:
#             s+=SPLIT[i][0].upper()
#         elif j!=0:
#             s+=SPLIT[i][j]
#     l.append(s)

# print(l)










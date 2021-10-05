# output [58,56,100]

my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=[]
for i in range(3):
    max=0
    for j in my_dict:
        if max < my_dict[j]:
           max = my_dict[j]
           c=j
    a.append(my_dict[c])
    my_dict.pop(c)
print(a)
    

        
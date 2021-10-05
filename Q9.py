# {'M':1,'I':4,'S':4,'P':2}

string=input("enter the string")
count={}
for i in string:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

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



    
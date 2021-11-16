d={10:"a",20:{30:"c",40:"d"},30:"e"}
sum=0 
for i in d:
    sum+=i
    if type(d[i])==dict:
        for k,v in d[i].items():
            sum+=k
print(sum)



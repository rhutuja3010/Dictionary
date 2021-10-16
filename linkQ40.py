dic=['s001','s002','s003','s004']
dic1=['Adina Park','Leyton Marsh','Duncan Boyle','Saim Richards']
dic2=[85,98,89,92]
a=[]
b={}
i=0
while i<len(dic):
    d={dic1[i]:dic2[i]}
    e={dic[i]:d}
    a.append(e) 
    i+=1
print(a)
dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
sum=[]
for i in dict.values():
    sum+=i
print(sum)
i=0
while i<len(sum):
    a=sum[i]
    count+=1
    i+=1
print(count)
    



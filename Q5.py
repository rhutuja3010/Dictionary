# output:
# {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
d={} 
for i in range (len(list1)):
    d [list1[i]] = list2[i]
print(d)
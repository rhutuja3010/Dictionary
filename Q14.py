
# Write a program to sort a dictionary in ascending or descending according to its values .

# Input :-

# {'bijender':45,'deepak':60,'param':20,"anjili":30,"roshini":50}
 
import operator 
Dictionary={'bijender':45,'deepak':60,'param':20,"anjili":30,"roshini":50}

asc=dict(sorted(Dictionary.items(),key=operator.itemgetter(1)))
print(asc)

dsc=dict(sorted(Dictionary.items(),key=operator.itemgetter(1),reverse=True))
print(dsc)








# If input is “name” then output will be “exist”
# If input is “class” then output will be “not exists”.

dict = {"name":"Raju", "marks":56}
input=input("enter the name:")
if input in dict:
    print("exist")
else:
    print("not exist")
    
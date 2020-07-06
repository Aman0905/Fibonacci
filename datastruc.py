#Assigning elements to list
#using append
list=[1,5,8,4,9]
list.append(8)
print(list)

#using insert
list.insert(1,6)
print(list)
print("\n")


#Accessing elements from tuple
tuple1=("Apple","Mango" , "Orange")
print(tuple1[1])


#Deleting different dictionary elements
dict1={
    "C" : "Easy",
    "C++": "Moderate",
    "Java" : "Tough",
    "Python": "Ready"}
print(dict1)
del dict1["Java"]
print(dict1)

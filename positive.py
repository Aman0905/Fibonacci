list=[]
n= int(input("Enter number of elements :"))
list2=[]
for i in range(0,n):
    p=int(input())

    list.append(p)

print("output")
for i in range(0,n):
    if list[i]>=0:
        list2.append(list[i])

print(list2)

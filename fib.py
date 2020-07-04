#Program to display fibonacci series
n=int(input("Enter the terms?"))
a=0
b=1
count =0


if n <=0:
    print("Enter positive number");
elif n==1:
    print(a)
else :
    print("Fibonacci series:")
    while count < n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1


        
    

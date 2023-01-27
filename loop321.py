n= int(input("enter value:"))

for i in range(1,n+1):
    num =1
    for j in range(1,(n+1)-i):
        print(end = " ")
    for k in range(1,i+1):
        print(num,end = "")
        num = num +1
    print("\r")
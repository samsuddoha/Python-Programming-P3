#find a perfect number
num=int(input("Enter the number: "))
factors=[]
for i in range(1,num):
    if num%i==0:
        factors.append(i)
s=sum(factors)
if s==num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number")

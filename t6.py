fib=[0,1]
cube=[]
n1=0
n2=1
n=int(input("Enter no of terms"))
i=3
while i<=n:
    n3=n1+n2
    n1=n2
    n2=n3
    i+=1
    fib.append(n3)
print(fib)   
print(list(map(lambda x:x**3,fib)))

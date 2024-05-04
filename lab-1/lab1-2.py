a=[]
b=[]
n=int(input("dimensions of vector: "))
for i in range(n):
    x=int(input("Enter elements of vector a:"))
    a.append(x)
for i in range(n):
    y=int(input("Enter elements of vector b:"))
    b.append(y)
print("a=",a)  
print("b=",b)
l=len(a)
prod=0
for i in range(l):
    prod=prod+a[i]*b[i]
    
print("dot product is",prod)
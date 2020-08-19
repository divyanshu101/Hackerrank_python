result=[]
x = int(input())
y = int(input())
z = int(input())
n = int(input())
for a in range(x+1):
   for b in range(y+1):
       for c in range(z+1):
           if (a+b+c !=n):
                 result.append([a,b,c])
print(result)

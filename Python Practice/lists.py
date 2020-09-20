scor=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    scor.append(ele)
print(max([x for x in scor if x != max(scor)]))

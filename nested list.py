n=int(input())
record={}
l=[]
for a in range(0,n):
    value = input()
    key=float(input())
    record[key]=value
    l.append(key)
print(record)
print(l)
sh=(max([x for x in l if x == min(l)]))
print(record[sh])
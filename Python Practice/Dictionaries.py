n=int(input())
pbook={}
for a in range (n):
    Key = input()
    Value = int(input())
    pbook[Key]=Value
s=list(input())
for i in s:
    print(s[i],"=",pbook.get(s[i], "Not found"))

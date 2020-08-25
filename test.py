n = int(input())
n = [input().split() for _ in range(n)]
pbook = {k: v for k,v in n}
while True:
    try:
        x = input()
        if x in pbook:
            print('%s=%s' % (x, pbook[x]))
        else:
            print('Not found')
    except:
        break

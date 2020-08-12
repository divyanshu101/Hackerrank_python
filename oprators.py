mc=float(input())
tip=int(input())
tax=int(input())
a=mc*tip/100
b=mc*tax/100
t=int(round(mc+a+b))
print(round(t))

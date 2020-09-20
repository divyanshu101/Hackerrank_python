def is_leap(y):
    if (1900<=y) and (y<=100000):
        if (y%4 == 0) and (y%100!=0) or (y%400==0):
         
              return"true"
        else:
               return"false"
   
year = int(input())
print(is_leap(year))
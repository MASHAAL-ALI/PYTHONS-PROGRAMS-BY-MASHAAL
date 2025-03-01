print(""" what you want to do
1.addition
2.subtraction
3.multiplication
4.division""")
n=int(input('enter choice: '))
x=int(input('enter x: '))
y=int(input('enter y: '))
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def divide(x,y):
    return x/y
if n==1:
    print('addition of',x,'and',y,'is = ',add(x,y))
elif n==2:
    print('subtraction of',x,'and',y,'is = ',sub(x,y))
elif n==3:
    print('multiplication of',x,'and',y,'is = ',multi(x,y))
elif n==4:
    print('division of',x,'and',y,'is = ',divide(x,y))

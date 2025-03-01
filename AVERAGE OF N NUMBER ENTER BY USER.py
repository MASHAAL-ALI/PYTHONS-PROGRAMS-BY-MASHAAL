n=int(input('ENTER HOW MUCH NUMBER YOU WANT TO TAKE AVG: '))
count=0
for i in range(n):
    a=int(input('ENTER NUMBER: '))
    if a>=0:
        count+=a
##    print('AVERAGE: ',count/n)
    if a<0:
        break
print('AVERAGE: ',count/n)

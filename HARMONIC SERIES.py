n=int(input('ENTER NUMBER TILL YOU WANT SERIES: '))
SUM=0
print('Series: ',end=' ')
for i in range(1,n+1):
    if i!=n:
        print(f'1/{i}+ ',end='')
    SUM+=1/i
else:
     print(f'1/{i}')
print('Sum: ',round(SUM,4))

    

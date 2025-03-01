j=9
count=0
n=int(input('number of term: '))
print('series: ',end='')
for i in range(1,n+1):
    series=str(j)*i
    print(series,end=' ')
    count+=int(series)
print()
print('sum: ',count)

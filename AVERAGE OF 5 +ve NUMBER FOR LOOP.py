count=0
for i in range(5):
    n=int(input('ENTER NUMBER: '))
    if n<0:
        break
    count+=n
else:
    print('AVERAGE: ',count/5)

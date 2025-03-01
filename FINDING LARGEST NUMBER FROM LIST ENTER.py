n=int(input('HOW MANY NUMBER IN LIST: '))
ELEMENT=[]
for i in range(n):
    a=int(input('ENTER ELEMENT OF LIST: '))
    ELEMENT.append(a)
print('THE LARGEST ELEMENT IS: ',max(ELEMENT))

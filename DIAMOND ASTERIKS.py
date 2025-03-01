m=int(input('Enter line: '))
for i in range(1,m+1):
     print(" "*(m-i)+"*"*(2*i-1))
for j in range(m-1,0,-1):
    print(" "*(i-j)+"*"*(2*j-1))

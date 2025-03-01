l=[]
sep=' '
chunk=''
string=input('enter your sentence: ').strip() # strip space at first
for i in string:
    if i==sep:
        l.append(chunk)
        chunk=''
    else:
        chunk+=i
if chunk!='':
    l.append(chunk)
print(l)
        

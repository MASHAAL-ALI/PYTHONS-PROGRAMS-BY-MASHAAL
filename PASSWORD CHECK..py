p=input("enter password:")
if((7<len(p)<15) and ('1' in p or '2' in p or '3' in p) and ('!' in p or '@' in p)):
    print("VALID")
else:
    print("INVALID")

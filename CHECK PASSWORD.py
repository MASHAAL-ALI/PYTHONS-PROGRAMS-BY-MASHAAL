P=input("ENTER YOUR PASSWORD: ")
if 15>len(P)>7:
    if('1' in P or '2' in P or '3' in P):
        if('A' in P or 'B' in P):
            if('!' in P or '@' in P):
                print("VALID PASSWORD")
            else:
                print("ENTER A CHARACTER")
        else:
            print("ENTER A ALPHABET")
    else:
        print("ENTER A NUMBER")
else:
    print("INVALID LENGTH")
        

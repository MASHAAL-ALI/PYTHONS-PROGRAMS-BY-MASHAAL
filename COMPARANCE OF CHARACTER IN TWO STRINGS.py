string_1=input(" string 1=enter any line alphabets limit till 15: ")
string_2=input(" string 2=enter any line alphabets limit till 15: ")
for x in string_1:
    if x in string_1 and x in string_2:
        print('COMMON: ',x)
for y in string_1:
    if y in string_1 and y not in string_2:
        print('UNCOMMON: ',y)

n=input('ENTER ANY SENTENCE: ')
count=0
for i in n:
    if i in 'AEIOUaeiou':
        count+=1
print('TOTAL VOWEL IN SENTENCE: ',count)

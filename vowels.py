word = input("Provide a word to search for vowels: ")
found = {'a' : 0,
         'e' : 0,
         'i' : 0,
         'o' : 0,
         'u' : 0}

for letters in word:
    if letters in found:
        found[letters] += 1
        
for value in sorted(found):
    if found[value] != 0:
        print(value, 'appears',found[value],'time(s)')   

print('    ')    

for k,v in sorted(found.items()):
    if v != 0:
        print(k,'was found',v,'time(s).')

word = input("Provide a word to search for vowels: ")
found = {}
vowels = ['a','e','i','o','u']
for letters in word:
    if letters in vowels:
            found.setdefault(letters,0);
            found[letters] += 1
        
for key in sorted(found):
    print(key, 'appears',found[key],'time(s)')

print('    ')    

for k,v in sorted(found.items()):
    print(k,'was found',v,'time(s).')
        

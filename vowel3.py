word = input("Provide a word to search for vowels: ")
vowels = ['a','e','i','o','u']
found = set(vowels).intersection(set(word))
        
for value in found:
    print(value)


phrase = "don't panic!"
plist = list(phrase)
print(plist)
print(phrase)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase+''.join(plist[5])+''.join(plist[4])+''.join(plist[7])+''.join(plist[6])


print(plist)
print(new_phrase)
   

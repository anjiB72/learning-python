phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for letter in plist:
  if letter != 'o' and letter != 'n' and letter != 't' and letter != 'a' and letter != 'p':
    plist.remove(letter)
plist.pop()
plist.pop(5)
plist.insert(2, ' ')
plist.insert(4, 'a')
plist.pop()
plist.insert(5,'p')
plist.pop()
          

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

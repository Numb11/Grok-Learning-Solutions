word = []
while "" not in word:
  word.append(input("Word: "))
print(f"You know {len(set(word))-1} unique word(s)!")

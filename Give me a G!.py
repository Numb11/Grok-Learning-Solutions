cheer = input("Cheer: ")
numb = 0
while numb<len(cheer):
  print(f"Give me a {cheer[numb]}, {cheer[numb]}!")
  numb = numb+1
print("What does it spell?")
print(cheer.upper())

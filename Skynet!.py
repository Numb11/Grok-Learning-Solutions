code = input("code: ")
code = code.split()
message = []
for i in range(len(code)):
  if code[len(code)-1-i][0].isupper():
     message.append(code[len(code)-1-i])
message = " ".join(message)
print ("says:",message.lower())

message = input("Message? ")
real = ""
numb = 0
for i in range(len(message)//3):
  if numb>0:
   real = real + " "
  real = real + message[numb]
  numb = numb+3
print(real)

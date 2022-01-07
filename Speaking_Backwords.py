line = input("Line: ")
backward = ""
numb = 1
for i in range(len(line)):
 backward = (backward + line[len(line)-numb])
 numb = numb+1
print (backward)

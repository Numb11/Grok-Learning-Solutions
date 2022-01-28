students = input("Students: ")
classroll = students.split(" ")
classroll.sort()
print("Class Roll")
for i in range(len(classroll)):
  print (classroll [i])

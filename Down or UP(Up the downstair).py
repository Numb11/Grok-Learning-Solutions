steps = int(input("How many steps? "))
print("__")
spaces = ("  ")
for i in range(steps-1):
  print(f"{spaces}|_")
  spaces = spaces.join("  ")
print("__"*steps+"|")

floor = int(input("Current floor: "))
destination = int(input("Destination floor: "))
print(f"Level {floor}")
for i in range(destination - floor):
 floor = (floor +1)
 print(f"Level {floor}")

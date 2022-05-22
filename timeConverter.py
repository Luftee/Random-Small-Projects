def format_check(a):
    b = len(a)
    if b != 3 and b != 4:
        return True
    elif int(a) > 2400:
        return True

while True:
    print("Original timezone: ", end = "")
    oldZone = input()
    if format_check(oldZone):
        break
    print("Original time: ", end = "")
    oldTime = input()
    if format_check(oldTime):
        break
    print("New timezone: ", end = "")
    newZone = input()
    if format_check(newZone):
        break

    print("\nNew time: ", end = "")
    print(int(oldTime) - int(oldZone) + int(newZone))
    break
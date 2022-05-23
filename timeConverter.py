def format_check(Global a):
    a = input()
    b = len(a)
    if b != 3 and b != 4:
        return True
    elif int(a) > 2359:
        return True

while True:
    print("Original timezone: ", end = "")
    if format_check(oldZone):
        break
    print("Original time: ", end = "")
    if format_check(oldTime):
        break
    print("New timezone: ", end = "")
    if format_check(newZone):
        break
        
    newTime = int(oldTime) - int(oldZone) + int(newZone)
    if newTime > 2359:
        newTime = newTime - 2400
    
    print("\nNew time: ", end = "")
    print(newTime)
    break

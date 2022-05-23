def format_check(a):
    b = len(a)
    return True if b != 3 and b != 4 else return False
    return True if int(a) > 2359 else return False

while True:
    print("Original timezone: ", end = "")
    oldZone = input()
    break if format_check(oldZone) else continue
    print("Original time: ", end = "")
    oldTime = input()
    break if format_check(oldTime) else continue
    print("New timezone: ", end = "")
    newZone = input()
    break if format_check(newZone) else continue
        
    newTime = int(oldTime) - int(oldZone) + int(newZone)
    newTime = newTime - 2400 if newTime > 2359 else continue
    
    print("\nNew time: ", end = "")
    print(newTime)
    break

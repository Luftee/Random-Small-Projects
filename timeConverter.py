def format_check(a):
    b = len(a)
    return True if b != 3 and b != 4
    return True if int(a) > 2359

while True:
    print("Original timezone: ", end = "")
    oldZone = input()
    break if format_check(oldZone)
    print("Original time: ", end = "")
    oldTime = input()
    break if format_check(oldTime)
    print("New timezone: ", end = "")
    newZone = input()
    break if format_check(newZone)
        
    newTime = int(oldTime) - int(oldZone) + int(newZone)
    newTime = newTime - 2400 if newTime > 2359
    
    print("\nNew time: ", end = "")
    print(newTime)
    break

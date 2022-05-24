def input_check():
    a = input()
    
    def format_error(a):
        if a:
            print("\nFormat error")
            return False

    b = len(a)
    format_error(b < 3 or b > 4)
    format_error(int(a) > 2359)
    format_error(int(str(a)[-2:]) >= 60)
    return a

while True:
    print("Original timezone: ", end = "")
    oldZone = input_check()
    if oldZone == False: break
    print("Original time: ", end = "")
    oldTime = input_check()
    if oldTime == False: break
    print("New timezone: ", end = "")
    newZone = input_check()
    if newZone == False: break
        
    newTime = int(oldTime) - int(oldZone) + int(newZone)
    if int(str(newTime)[-2:]) >= 60: newTime = newTime - 60 + 100
    if newTime > 2359: newTime = newTime - 2400
    
    print("\nNew time: ", end = "")
    if newTime < 1000: print("0", end = "")
    print(newTime)
    break

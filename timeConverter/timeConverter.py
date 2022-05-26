from functions import input_check

if True:
    oldZone = input_check("Original timezone: ")
    if oldZone == False: break
    oldTime = input_check("Original time: ")
    if oldTime == False: break
    newZone = input_check("New timezone: ")
    if newZone == False: break
        
    newTime = int(oldTime) - int(oldZone) + int(newZone)
    if int(str(newTime)[-2:]) >= 60: newTime = newTime - 60 + 100
    if newTime > 2359: newTime = newTime - 2400
    
    print("\nNew time: ", end = "")
    if newTime < 1000: print("0", end = "")
    print(newTime)

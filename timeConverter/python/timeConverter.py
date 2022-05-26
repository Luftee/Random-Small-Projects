def input_check(a):
    def format_error(a):
        if a:
            print("\nWrong format")
            global error; error = True

    b = input(a)
    c = len(b)
    format_error(c < 3 or c > 4)
    format_error(int(b) > 2359)
    format_error(int(str(b)[-2:]) >= 60)

    if error is True:
        return False
    else:
        return b

def main():
    oldZone = input_check("Original timezone: ")
    if oldZone is False:
        return
    oldTime = input_check("Original time: ")
    if oldTime is False:
        return
    newZone = input_check("New timezone: ")
    if newZone is False:
        return
        
    newTime = int(oldTime) - int(oldZone) + int(newZone)
    if int(str(newTime)[-2:]) >= 60:
        newTime = newTime - 60 + 100
    if newTime > 2359:
        newTime = newTime - 2400
    
    print("\nNew time: ", end = "")
    if newTime < 1000:
        print("0", end = "")
    print(newTime)

if __name__ == "__main__":
    main()
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

def calculations():
    newTime = int(oldTime) - int(oldZone) + int(newZone)
    if int(str(newTime)[-2:]) >= 60: newTime = newTime - 60 + 100
    if newTime > 2359: newTime = newTime - 2400

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

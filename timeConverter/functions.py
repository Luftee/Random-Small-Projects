def input_check(b):
    a = input(b)
    
    def format_error(a):
        if a:
            print("\nFormat error")
            return False

    b = len(a)
    format_error(b < 3 or b > 4)
    format_error(int(a) > 2359)
    format_error(int(str(a)[-2:]) >= 60)
    return a

if __name__ == "__main__":
    print("You found a secret message, you are not suppose to run this.")

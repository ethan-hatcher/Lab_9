def main():

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        match option:

            case 1:
                encode()
            case 2:
                decode()
            case 3:
                break

def encode(): 
    password = input("Please enter your password to encode: ")
    new_password = ""
    for char in password:
        char = int(char)
        char = str(char + 3)
        new_password += char
    print("Your password has been encoded and stored!")
    return new_password
def decode():
    pass


if __name__ == "__main__":
    main()

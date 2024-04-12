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
                password = input("Please enter your password to encode: ")
                encoded_password = encode(password)
            case 2:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            case 3:
                break


def encode(password):
    new_password = ""
    for char in password:
        char = int(char)
        char = str(char + 3)
        new_password += char
    print("Your password has been encoded and stored!")
    return new_password


def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        char = int(char)
        char = str(char - 3)
        decoded_password += char
    return decoded_password


if __name__ == "__main__":
    main()

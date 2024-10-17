# Author: Nicholas Cuc

def encode(password):
    encoded_password = ""

    for digit in password:
        encoded_password += str((int(digit) + 3) % 10)

    return encoded_password


# TODO: Make decoder function


def main():
    encoded_password = None

    while True:
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = int(input("Please enter an option: "))

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            pass    # TODO: implement the decoder program
            """if encoded_password is None:
                print("No encoded password found. Please encode a password first.")
            else:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")"""

        # Exit program
        elif option == "3":
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

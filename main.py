# Author: Nicholas Cuc

# Encoder program
def encode(password):
    encoded_password = ""

    for digit in password:
        # Shift each digit by 3
        encoded_password += str((int(digit) + 3) % 10)

    return encoded_password


# TODO: Make decoder function
#added by xiaolei huang
def decode(encoded_password): #decodes on a char by char basis
    decoded_password=""
    for digit in encoded_password:
        if digit== "0":
            decoded_password+= "7"
        elif digit== "1":
            decoded_password+="8"
        elif digit=="2":
            decoded_password+= "9"
        elif digit== "3":
            decoded_password+="0"
        elif digit=="4":
            decoded_password+= "1"
        elif digit== "5":
            decoded_password+="2"
        elif digit=="6":
            decoded_password+= "3"
        elif digit== "7":
            decoded_password+="4"
        elif digit=="8":
            decoded_password+= "5"
        elif digit== "9":
            decoded_password+= "6"
    print(f' The encoded password is {encoded_password}, and the original password is {decoded_password}.')
    return decoded_password



# The main() that contains the basic menu/options
def main():
    encoded_password = None

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = int(input("Please enter an option: "))

        # option == 1 then prompt user to provide a password to encode
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()

        # option == 2 then print out the encoded and decoded password
        elif option == 2:
            decode(encoded_password)

        # option == 3 then exit program
        elif option == 3:
            break

        # If invalid option inputted then print out "Invalid option, please try again."
        else:
            print("Invalid option, please try again.")
            print()

if __name__ == "__main__":
    # Runs main function
    main()

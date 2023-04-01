from art import logo

# Declare variable
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

end_of_encrypt = False


# Function to decode / encode word or phrase
def caesar(choice_of_direction, text_of_caesar, shift_caesar):

    """ Function to decode / encode word or phrase
    Request :
    choice_of_direction -> encode/decode
    text_of_caesar -> varchar
    shift_caesar  -> integer """

    # Declare Variable
    caesar_word = ""
    caesar_index = 0
    alphabet_len = len(alphabet)

    # Cycle for to read letter in "text_of_caesar"
    for letter in text_of_caesar:
        # if condition to check the index letter

        if letter in alphabet:
            alphabet_index = alphabet.index(letter)

            # if condition to check direction
            if choice_of_direction == "encode":
                caesar_index = alphabet_index + shift_caesar
                # Cycle while condition to exit "caesar_index < alphabet_len"
                while caesar_index >= alphabet_len:
                    caesar_index = caesar_index - alphabet_len
            elif choice_of_direction == "decode":
                caesar_index = alphabet_index - shift_caesar
            caesar_word += alphabet[caesar_index]
        else:
            caesar_word += letter

    print(f"\nThe {choice_of_direction}d text is : {caesar_word}")


while not end_of_encrypt:
    # Declare Variable
    direction = ""
    shift = ""

    print(logo)

    # Ask user to insert direction, text to encode/decode, and shift number
    while (direction != "encode") and (direction != "decode"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    text = input("Type your message: ").lower()

    while not shift.isnumeric():
        shift = input("Type the shift number: ")

    shift = int(shift)
    # Call function "caesar"
    caesar(direction, text, shift)

    want_continuous = input("\nDo you want encode/decode again? ( Y / N )  : ").lower()

    if want_continuous == "y":
        end_of_encrypt = False
    elif want_continuous == "n":
        end_of_encrypt = True
        print("Goodbye")
        break
    else:
        print("Sorry your choice is uncorrected!")

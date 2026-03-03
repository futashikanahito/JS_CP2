# JS, 1st, Morse Code Translator

# Make a tuple of all morse characters
morse = (
    ".-",    # A
    "-...",  # B
    "-.-.",  # C
    "-..",   # D
    ".",     # E
    "..-.",  # F
    "--.",   # G
    "....",  # H
    "..",    # I
    ".---",  # J
    "-.-",   # K
    ".-..",  # L
    "--",    # M
    "-.",    # N
    "---",   # O
    ".--.",  # P
    "--.-",  # Q
    ".-.",   # R
    "...",   # S
    "-",     # T
    "..-",   # U
    "...-",  # V
    ".--",   # W
    "-..-",  # X
    "-.--",  # Y
    "--..",  # Z
    "-----", # 0
    ".----", # 1
    "..---", # 2
    "...--", # 3
    "....-", # 4
    ".....", # 5
    "-....", # 6
    "--...", # 7
    "---..", # 8
    "----.", # 9
    ".-.-.-", # .
    "--..--", # ,
    "..--..", # ?
    ".----.", # '
    "-.-.--", # !
    "-..-.",  # /
    "-.--.",  # (
    "-.--.-", # )
    ".-...",  # &
    "---...", # :
    "-.-.-.", # ;
    "-...-",  # =
    ".-.-.",  # +
    "-....-", # -
    "..--.-", # _
    ".-..-.", # "
    "...-..-",# $
    ".--.-.", # @
)
# Make a tuple of all english characters
english = (
    "A", "B", "C", "D", "E", 
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", 
    "Z", "0", "1", "2", "3", 
    "4", "5", "6", "7", "8", 
    "9", ".", ",", "?", "'", 
    "!", "/", "(", ")", "&", 
    ":", ";", "=", "+", "-", 
    "_", '"', "$", "@",
)

# Create a function for morse to english
def from_morse():
    # Ask user for input
    change = input("Input your morse code message: ").split(" ")
    result = ""

    # Loop through every word
    for code in change:
        # Replace / with spaces
        if code == "/":
            result += " "
        # Use the tuples to translate the other things through indexes
        elif code in morse:
            index = morse.index(code)
            result += english[index]

    # Print the translated message
    print(f"Translated message: {result}")
    input("Press enter to continue...")

# Create a function for english to morse
def to_morse():
    # Ask user for input
    change = input("Input your english message: ").upper()
    result = ""

    # Loop through every word
    for char in change:
        # Replace spaces with /
        if char == " ":
            result += "/ "
        # Use the tuples to translate the other things through indexes
        elif char in english:
            index = english.index(char)
            result += morse[index] + " "

    # Print the translated message
    print(f"Translated message: {result}")
    input("Press enter to continue...")

# Create a function for main
def main():
    # Forever loop
    while True:
        print("\033c", end="")
        # Ask user what they want to do
        choice = input("What would you like to do:\n 1. Morse to english translator\n 2. English to morse translator\n 3. Exit\n")
        while choice != "1" and choice != "2" and choice != "3":
            choice = input("That was not a valid input, Try again: ")
        # If user chooses to translate from morse to english call that function
        if choice == "1":
            from_morse()
        # If user chooses to translate from english to morse call that function
        elif choice == "2":
            to_morse()
        # If user chooses to leave stop program
        else:
            print("Thank you for using this program.")
            break
main()
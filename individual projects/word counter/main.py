# JS, 1st, Word Counter

# ----- PSEUDOCODE -----
# 1. Ask user for a valid file path (loop until found)
# 2. Show menu with options: Update, View, Add content, Exit
# 3. Based on choice:
#    - Update: count words and print new count
#    - View: print document text
#    - Add: take multi-line input and append to file
#    - Exit: print goodbye and quit
# 4. After each action (except Exit), print timestamp and append word count to file

# ----- CODE & PSEUDOCODE -----
import file_saver
import time_saver

# Pseudocode for update():
# - Call organize() to count words in the file
# - Print the updated word count
def update(current_file):
    word_count = file_saver.organize(current_file)
    print(f"\nDocument updated. Word count: {word_count}\n")

# Pseudocode for view():
# - Call get_main_text() to retrieve document content (excluding word count footer)
# - Print the content
def view(current_file):
    print("\nDocument content:")
    main_text = file_saver.get_main_text(current_file)
    print(main_text)
    print()

# Pseudocode for add():
# - Prompt user to enter lines of text; stop when they enter a blank line
# - Read the current main text from the file
# - Append the new lines to the existing text
# - Write the combined text back to the file
def add(current_file):
    print("\nEnter new content (press Enter twice to finish):")

    lines = []

    while True:
        line = input()

        if line == "":
            break

        lines.append(line)

    main_text = file_saver.main_text(current_file)
    new_text = main_text + ("\n" if main_text else "") + "\n".join(lines)

    with open(current_file, "w") as file:
        file.write(new_text)

    print("Content added successfully.\n")

# Pseudocode for main():
# - Loop: ask for file path; break when valid file is found
# - Loop: show menu, read choice, call matching function
# - After each action (except Exit), get time_saverstamp and word count, append to file
def main():

    while True:
        current_file = input("\nEnter the exact file path for your document: ").strip()

        try:
            with open(current_file, "r") as file:
                print()
                break

        except:
            print("File not found. Please try again.")

    while True:
        print("""-- Document Word Count Updater ---
    1. Update document info
    2. View document
    3. Add content to document
    4. Exit""")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            update(current_file)
        elif choice == "2":
            view(current_file)
        elif choice == "3":
            add(current_file)
        elif choice == "4":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 7.")
        
        #PRINT TIMESTAMP AND OTHER STUFF IDK I KINDA JUST WORK HERE
        timestamp = time_saver.timestamp()
        word_count = file_saver.organize(current_file)
        file_saver.append(current_file, word_count, timestamp)

main()
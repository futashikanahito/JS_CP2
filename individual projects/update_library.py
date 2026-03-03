# JS, 1st, Personal Library Program

# ----- PSEUDOCODE -----
# import the csv library

# load library function
#   open the csv file
#   read each row and save it as a dictionary
#   add each dictionary to a list
#   return the list

# save library function
#   open the csv file
#   write all the items in the list to the file
#   print "Library saved"

# show function
#   loop through each item in the library
#       print the number, title, creator, year, and genre

# add item function
#   ask the user for title, creator, year, and genre
#   create a new dictionary with that info
#   add it to the library list
#   print a confirmation message

# update item function
#   if the library is empty, say so and stop
#   show the library
#   ask the user which number they want to update
#   ask for new values (if they press enter, keep the old value)
#   update the item with any new values they typed

# delete item function
#   if the library is empty, say so and stop
#   show the library
#   ask the user which number they want to delete
#   ask them to confirm
#   if they say yes, remove that item from the list

# main function
#   load the library from the file
#   loop forever:
#       show the menu
#       ask the user to pick an option
#       if 1: show the library
#       if 2: add an item
#       if 3: update an item
#       if 4: delete an item
#       if 5: save the library
#       if 6: reload the library from the file
#           if there are unsaved changes, ask if they want to save first
#       if 7: exit
#           if there are unsaved changes, ask if they want to save first
#           print goodbye and stop the loop
#       otherwise: print "invalid option"

# run main

# ----- CODE & PSUEDOCODE -----
# import the csv library
import csv

# load library function
#   open the csv file
#   read each row and save it as a dictionary
#   add each dictionary to a list
#   return the list
def load_library():
    library = []
    with open("csvs/songs.csv", mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, 1):
            item = {"title": row.get("title", "").strip(), "creator": row.get("creator", "").strip(), "year": row.get("year", "").strip(), "genre": row.get("genre", "").strip()}
            library.append(item)
    return library

# save library function
#   open the csv file
#   write all the items in the list to the file
#   print "Library saved"
def save_library(unsaved_changes, library):
    with open("csvs/songs.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "creator", "year", "genre"])
        writer.writeheader()
        writer.writerows(library)
    unsaved_changes = False
    print("Library saved.")
    return unsaved_changes

# helper function
def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field is required. Please enter a value.")

# helper function
def get_index(prompt, max_index):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            index = int(value) - 1
            if 0 <= index < max_index:
                return index
        print(f"Please enter a number between 1 and {max_index}.")

# show function
#   loop through each item in the library
#       print the number, title, creator, year, and genre
def show(library):
    for i, item in enumerate(library, 1):
        print(f"""{i}, {item['title']}:
    Creator : {item['creator']}
    Year    : {item['year']}
    Genre   : {item['genre']}""")

# add item function
#   ask the user for title, creator, year, and genre
#   create a new dictionary with that info
#   add it to the library list
#   print a confirmation message
def add_item(unsaved_changes, library):
    print("\n-- Add Item --")
    title = get_input("Title: ")
    creator = get_input("Creator (author/artist/director): ")
    year = get_input("Year: ")
    genre = get_input("Genre: ")
    library.append({"title": title, "creator": creator, "year": year, "genre": genre})
    unsaved_changes = True
    print(f'"{title}" added to library.')
    return unsaved_changes, library

# update item function
#   if the library is empty, say so and stop
#   show the library
#   ask the user which number they want to update
#   ask for new values (if they press enter, keep the old value)
#   update the item with any new values they typed
def update_item(unsaved_changes, library):
    show(library)
    index = get_index("Enter the number of the item to update: ", len(library))
    item = library[index]
    print(f'\nUpdating "{item["title"]}". Press Enter to keep current value.')
    new_title = input(f"Title [{item['title']}]: ").strip()
    new_creator = input(f"Creator [{item['creator']}]: ").strip()
    new_year_raw = input(f"Year [{item['year']}]: ").strip()
    new_genre = input(f"Genre [{item['genre']}]: ").strip()
    if new_title:
        item["title"] = new_title
    if new_creator:
        item["creator"] = new_creator
    if new_year_raw:
        if new_year_raw.isdigit() and 1 <= int(new_year_raw) <= 9999:
            item["year"] = int(new_year_raw)
        else:
            print("Invalid year entered. Year not updated.")
    if new_genre:
        item["genre"] = new_genre
    unsaved_changes = True
    print("Item updated.")
    return unsaved_changes, library

# delete item function
#   if the library is empty, say so and stop
#   show the library
#   ask the user which number they want to delete
#   ask them to confirm
#   if they say yes, remove that item from the list
def delete_item(unsaved_changes, library):
    show(library)
    index = get_index("\nEnter the number of the item to delete: ", len(library))
    title = library[index]["title"]
    confirm = input(f'Are you sure you want to delete "{title}"? (y/n): ').strip().lower()
    if confirm in ("y", "yes"):
        library.pop(index)
        unsaved_changes = True
        print(f'"{title}" deleted.')
    else:
        print("Deletion cancelled.")
    return unsaved_changes, library

# main function
#   load the library from the file
#   loop forever:
#       show the menu
#       ask the user to pick an option
#       if 1: show the library
#       if 2: add an item
#       if 3: update an item
#       if 4: delete an item
#       if 5: save the library
#       if 6: reload the library from the file
#           if there are unsaved changes, ask if they want to save first
#       if 7: exit
#           if there are unsaved changes, ask if they want to save first
#           print goodbye and stop the loop
#       otherwise: print "invalid option"
def main():
    unsaved_changes = False
    library = load_library()
    while True:
        print("""Personal Library:
    1. Show list
    2. Add item
    3. Update item
    4. Delete item
    5. Save library
    6. Reload library from file
    7. Exit""")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show(library)
        elif choice == "2":
            unsaved_changes, library = add_item(unsaved_changes, library)
        elif choice == "3":
            unsaved_changes, library = update_item(unsaved_changes, library)
        elif choice == "4":
            unsaved_changes, library = delete_item(unsaved_changes, library)
        elif choice == "5":
            unsaved_changes = save_library(unsaved_changes, library)
        elif choice == "6":
            if unsaved_changes:
                choice = input("You have unsaved changes. Save before continuing? (y/n): ").strip().lower()
                if choice == "y" or choice == "yes":
                    save_library(unsaved_changes, library)
            load_library()
            print("Reloaded library from songs.csv.")
        elif choice == "7":
            if unsaved_changes:
                choice = input("You have unsaved changes. Save before continuing? (y/n): ").strip().lower()
                if choice == "y" or choice == "yes":
                    save_library(unsaved_changes, library)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 7.")

# run main
main()
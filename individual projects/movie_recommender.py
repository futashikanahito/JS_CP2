# JS\n 1st\n Movie Recommender

# ----- PSUEDOCODE -----
# import csv and menu (my helper function which makes it look all pretty)
# define view function
#   open the file
#       print each line in the file nicely

# define search function
#   ask the user for filters they want to apply
#   ask them what they want to search from those specific filters
#   check the file for the filters and the user's search and add the movie if it has those things
#   print those movies

# define main function
#   forever loop
#       ask the user what they want to do
#       call the specific function
# call main

# ----- CODE -----
import csv

def view():
    try:
        with open("csvs/movies.csv", "r") as file:
            content = csv.reader(file)
            for line in content:
                print(f"Title: {line[0]}\n Director: {line[1]}\n Genre: {line[2]}\n Rating: {line[3]}\n Length (in minutes): {line[4]}\n Notable Actors: {line[5]}")
    except:
        print("That file was not found.")
    

def search():
    choices = input("Choose filters to apply (enter numbers separated by commas, e.g., 1,3):\n 1. Genre\n 2. Director\n 3. Actor\n 4. Length (min & max)\n WARNING: THERE MIGHT BE DUPLICATE MOVIES\n - ").split(",")
    choices = [c.strip() for c in choices]
    filters = {}
    results = []
    max_length = None
    min_length = None

    if "1" in choices:
        filters["genre"] = input("Enter genre (e.g., 'Sci-Fi'): ").strip().lower()
    if "2" in choices:
        filters["director"] = input("Enter director: ").strip().lower()
    if "3" in choices:
        filters["actor"] = input("Enter actor: ").strip().lower()
    if "4" in choices:
        min_inp = input("Enter minimum length in minutes (or leave blank): ").strip()
        max_inp = input("Enter maximum length in minutes (or leave blank): ").strip()
        min_length = int(min_inp) if min_inp else None
        max_length = int(max_inp) if max_inp else None
    
    try:
        with open("csvs/movies.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                title, director, genre, year, length, actors = line
                length = int(length)
                insert = True
                if "genre" in filters and filters["genre"] not in genre.lower():
                    insert = False
                if "director" in filters and filters["director"] not in director.lower():
                    insert = False
                if "actor" in filters and filters["actor"] not in actors.lower():
                    insert = False
                if min_length is not None and length < min_length:
                    insert = False
                if max_length is not None and length > max_length:
                    insert = False
                if insert:
                    results.append((title, year, genre, director, actors, length))

    except FileNotFoundError:
        print("movies.csv not found")
        return

    if not results:
        print("No movies match those filters. Try removing one filter or widening the length range.")
        return

    print("\nRESULTS:\n")
    for m in results:
        print(f"Title: {m[0]}\n Director: {m[1]}\n Genre: {m[2]}\n Rating: {m[3]}\n Length (in minutes): {m[4]}\n Notable Actors: {m[5]}")

def main():
    while True:
        choice = input("Type the number for the action you would like to perform:\n 1. Search / Get Recommendations\n 2. Print Full Movie List\n 3. Exit\n - ")
        if choice == "1":
            search()
        elif choice == "2":
            view()
        else:
            print("Thank you for using this program!")
            break

main()
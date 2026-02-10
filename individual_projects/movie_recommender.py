# JS\n 1st\n Movie Recommender

# ----- PSUEDOCODE -----
# import csv and menu (my helper function which makes it look all pretty)
# define view function
#   
# define search function
#
# define main function
#
# call main
# ----- PSUEDOCODE & CODE -----
#from menu import menu
import csv, os
from helpers import menu

def view():
    try:
        with open("csvs/movies.csv", "r") as file:
            content = csv.reader(file)
            for line in content:
                print(f"Title: {line[0]}\n Director: {line[1]}\n Genre: {line[2]}\n Rating: {line[3]}\n Length (in minutes): {line[4]}\n Notable Actors: {line[5]}")
    except:
        print("That file was not found.")
    

def search():
    inp = input()
    try:
        with open("csvs/movies.csv", "r") as file:
            content = csv.reader(file)
            for line in content:
                print(line)
                for cell in line:
                    if inp in cell:
                        print(f"Title: {line[0]}\n Director: {line[1]}\n Genre: {line[2]}\n Rating: {line[3]}\n Length (in minutes): {line[4]}\n Notable Actors: {line[5]}")
    except:
        print("That file was not found.")

def main():
    if os.name == 'nt':
        options = ["View All Movies", "Search / Recommend Movies", "Exit"]
        while True:
            choice = menu(options)
            if choice == 0:
                view()
            elif choice == 1:
                search()
            else:
                print("Thank you for using this program!")
                break
    else:
        while True:
            choice = input("Type the number for the action you would like to perform:\n\n 1. Search / Get Recommendations\n 2. Print Full Movie List\n 3. Exit\n -")
            if choice == 0:
                view()
            elif choice == 1:
                search()
            else:
                print("Thank you for using this program!")
                break

main()
'''This module executes the system.'''
import readtolist as a
import borrow_return as br
from display import display
path="books.txt"
list2d=a.convert(path)


def borrow_return(list2d):
    """This module provides the available choice to choose from and calls
        the respective functions from their respective modules."""
    more="y"
    while more=="y":
        print("\t1. Press 'b' to borrow book.\n\t2. Press 'r' to return book.\n\t\
3. Press 'd' to display available books.")
        user_choice=input("Do you want to display, borrow or return book?").lower()
        if user_choice=='b':
            br.borrow_book(list2d)      #executes if user wants to borrow book
        elif user_choice=='r':
            br.return_book(list2d)      #executes if the user wants to return borrowed book
        elif user_choice=='d':
            display(list2d)             #executes if user wants to displlay available books
        else:
            print("Please enter a valid option.")       #executes if user chooses invalid option
        more=input("Do you want to do more transaction?(y/n) ").lower()

borrow_return(list2d)

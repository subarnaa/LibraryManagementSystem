def display(database):
    """ This function reads the 2d list and displays the books information in tabular form."""
    for i in range(len(database)):
        for j in range(len(database[i])):
            print(database[i][j],end=("\t\t\t"))
        print("\n")


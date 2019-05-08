'''This module contains the functions to be carried out when book is borrowed or returned.'''
import datetime
import os
import readtolist as rtl
import checkfine as cf
def borrow_book(list2d):
    """This function manages the information before and after borrowing the book."""
    bookID=input("Enter BookID: ").upper()
    valid=True
    for i in range (1,len(list(list2d))):
        if bookID in list2d[i]:                 #checks if the book is present in database or not
            if int(list2d[i][3])>0:             #checks if selected book is available or not
                list2d[i][3]=str(int(list2d[i][3])-1)
                rtl.update_database(list2d)     #updates the quantity of book in the database
                con=input("Book Name: " + list2d[i][1] + "\nAre you sure you want to borrow this book?(y/n) ")
                if con=="y":
                    username=input("Enter your name: ").upper()
                    try:                        #throws error if file doen't exist.
                        file=open(bookID+"-"+username+".txt","r")
                        file.close()
                    except:                     #runs when there is error
                        file=open(bookID+"-"+username+".txt","w")
                        write=','.join(list2d[i])
                        file.write(write+","+username+","+str(datetime.datetime.now()))
                        file.close()
                        print("Note: The book must be returned within 10 days.\nIn case of \
late return, you will be charged $1.5 extra per day.")
                    else:                       #runs when there is no error
                        print("You have already borrowed this book.")
                    finally:                    #runs everytime even when there is error
                        valid=True
                        break
                else:
                    print("Exiting.....")
            else:
                print("Sorry, the specified book is out of stock.")
                valid=True
        elif bookID not in list2d[i]:
            valid=False
    if valid==False:
        print("Not a valid book ID.\nExiting.....")
            

def return_book(list2d):
    """This function mainly takes the borrowed books back and updates the database."""
    bookID=input("Enter BookID: ").upper()
    username=input("Enter your name: ").upper()
    filename=bookID+"-"+username+".txt"
    try:                                            #throws an error if the logfile doesn't exists
        file=open(filename,"r")
        file.close()
    except:                                         #runs the following if there is error
        print("You have not borrowed this book. Please check the bookID or name. ")
    else:                                           #runs only if there is no error
        for i in range (1,len(list2d)):
            if bookID in list2d[i]:
                list2d[i][3]=str(int(list2d[i][3])+1)
        rtl.update_database(list2d)                 #updates the quantity of book in the database
        file=open(filename,"a")
        log_content=rtl.read_from_log(filename)         
        deadline=cf.check_deadline(filename)        #calculates number of days after deadline
        total_price=cf.total_price(log_content[4],deadline)         #calculates total price
        to_print="Fine: "+cf.check_fine(deadline)+"\nTotal Price: "+total_price+\
                  "\nThank you for returning the book. :-) Have a good day ahead!"
        file.write("\nReturned at: "+ str(datetime.datetime.now()) +\
                   "\nFine: " + cf.check_fine(deadline) +"\nTotal Price: "+total_price)
        file.close()
        os.rename(filename,bookID+"-"+username+"-RETURNED.txt")
        print(to_print)













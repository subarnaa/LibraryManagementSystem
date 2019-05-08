def file_read(path):
    """This function opens the database file i.e "books.txt" in read mode. The, it reads and stores each line of the file in a list."""
    file=open(path,"r")
    content=file.readlines()                    #reads each line and stores in list.
    return content
    file.close()

def content_to_list(prev_list):
    """This function converts the list obtained from file_read() function to a 2d list."""
    db=[]
    for i in prev_list:
        db.append(i.replace("\n","").split(","))
    return db

def convert(path):
    """The ffunction uses file_read() and content_to_list() function and returns the 2d list directly."""
    new_list=file_read(path)                    #creates list
    list2d=content_to_list(new_list)            #creats 2d list from above list
    return list2d

def read_from_log(logfile):
    """This function reads the logfile created while borrowing book and converts the file content to a 2d list."""
    file=open(logfile,"r")
    content=file.read()
    in_list=content.split(",")
    return in_list
    file.close()

def update_database(list2d):
    """This function opens the database file inwrite mode and updates the information of books as per transaction."""
    file = open("books.txt","w")
    for each in list2d:
        to_write=','.join(each)
        file.write(to_write+"\n")               #writes i.e. updates the database
    file.close()



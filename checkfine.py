'''This module contains three functions that check the deadline, calculate fine
and calculate total price.'''
import datetime
import readtolist as rtl

def check_deadline(logfile):
    """This function returns the number of days for which the book has been borrowed."""
    file=open(logfile,"r")
    content=file.read()
    new_list=content.split(",")
    print(new_list)
    datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'                         #datetime format
    date1 = str(datetime.datetime.now()) 
    date2 = new_list[6]
    diff= datetime.datetime.strptime(date1, datetimeFormat)\
          - datetime.datetime.strptime(date2, datetimeFormat)         #calculates time difference
    file.close()
    return diff.days                                                #returns only the days


def check_fine(time_diff):
    """This function calculates and returns the total fine in case of late submission."""
    fine=0
    if time_diff>10:
        fine=(time_diff-10)*1.5                                     #calculates fine
    total_fine="$"+str(fine)
    return total_fine

def total_price(price,time_diff):
    """This function adds the fine amount and price of the book and returns total price."""
    price=float(price.replace("$",""))+float(check_fine(time_diff).replace("$",""))
    total_price="$"+str(price)
    return(total_price)



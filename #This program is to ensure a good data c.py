##############################################################################
#This program is to ensure a good data collection of Julie's Party Hire Store#
##############################################################################

#import tkinter so we can make a GUI
from tkinter import *

#quit subroutine
def quit () :
    main_window.destroy()

#print details of all the customers
def print_customer_details () :
    #these are global variables that are used
    global j_names, total_entries, name_count
    name_count=0
    #Create the column headings
    Label(main_window, font=("Helvetica 10 bold"), text="Full Name") .grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Receipt Number") .grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Item") .grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Number of Item/s") .grid(column=3, row=7)
    #add each item in the list onto its own row
    while name_count < total_entries :
        Label(main_window, text=name_count) .grid(column=0, row=name_count+8)
        Label(main_window, text=(customer_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(customer_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count += 1

#Check the inputs are all valid
def check_inputs ():
    #these are the global variables that are used
    global customer_details, entry_name, entry_receipt, entry_item, entry_quantity
    input_check = 0
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text="               ") .grid(column=2,row=1)
    Label(main_window, text="               ") .grid(column=2,row=2)
    Label(main_window, text="               ") .grid(column=2,row=3)
    #Check that Full Name is not blank, set error text if blank   
    if len(entry_name.get()) == 0 :
        Label(main_window,fg="red", text="Required") .grid(column=2,row=0)
        input_check = 1
    #Check that Receipt Number is not blank, set error text if blank     
    if len(entry_receipt.get()) == 0 :
        Label(main_window,fg="red", text="Required") .grid(column=2,row=1)
        input_check = 1
    #Check that Item is not blank, set error text if blank     
    if len(entry_item.get()) == 0 :
        Label(main_window,fg="red", text="Required") .grid(column=2,row=2)
        input_check = 1
    #Check the number of item/s is not blank and between 1 and 500, set error text if blank  
    if (entry_quantity.get().isdigit()) : 
        if  int(entry_quantity.get()) < 1 or  int(entry_quantity.get()) > 500:
            Label(main_window,fg="red", text="1-500 only") .grid(column=2,row=2)
            input_check = 1
    else :
        Label(main_window,fg="red", text="1-500 only") .grid(column=2,row=2)
        input_check = 1      
    if input_check == 0 : append_name()

#add the next customer to the list
def append_name ():
    #these are the global variables that are used
    global customer_details, entry_name, entry_receipt, entry_item, entry_quantity, total_entries
    #append each item to its own area of the list
    customer_details.append([entry_name.get(),entry_receipt.get(),entry_item.get(),entry_quantity.get()])
    #clear the boxes
    entry_name.delete(0,'end')
    entry_receipt.delete(0,'end')
    entry_item.delete(0,'end')
    entry_quantity.delete(0,'end')
    total_entries +=  1

#start the program running
def main ():
    #create the GUI and start it up
    main_window =Tk ()
    setup_buttons ()
    main_window.mainloop ()
        
main ()
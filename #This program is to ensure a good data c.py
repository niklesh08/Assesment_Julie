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
    

#start the program running
def main ():
    #create the GUI and start it up
    main_window =Tk ()
    setup_buttons ()
    main_window.mainloop ()
        
main ()
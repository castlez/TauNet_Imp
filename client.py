#TauNet Client Program
#Copyright (c) 2015 Jonathan Castle

#First version of the client side for
#TauNet messaging system.

import socket
from crypto import *
from util import *
from subprocess import call
from test import Test

port = 6283
k = str.encode("password")

#main method
def main():
    
    #execute tests
    Test()
    display = "" #used for smooth displaying of address book and messages
    while True:
        #gather users response to menu options
        call(["clear"]) #clear the screen
        print(display + "\n\n")
        display = "" #reset display so it doesn't keep printing previous operations
        ans = input("###  TauNet Menu  ###\n1. send message\n2. read messages\n3. check address book\n4. add to address book\n5. quit\n>>>")
        if (ans not in ['1','2','3','4','5']): #if invalid input, try again
            continue
        
        #send a message
        if (ans == '1'):
            call(["clear"]) #clear the screen
            host = input("Host?(type '@' for address book): ")
            while (host == '@'):
                call(["clear"]) #clear the screen
                print (getAddressBook("address.txt"))
                host = input("Host?(type '@' for address book): ")

            if (sendMessage(host,port,k) == 0):
                display = "[TauNet Error] Failed to send message! Connection could not be established.(check 'errorlog.txt' for error info)\n"
        #read messages
        elif (ans == '2'):
            display = readMessages("log.txt")
            if(display == '0'):
                display = "[TauNet Error] Failed to load messages, file may be empty or not exist.\n"
        #display address book
        elif (ans == '3'):
            display = getAddressBook("address.txt")
            if(display == '0'):
                display = "[TauNet Error] Failed to load address book, file may be empty or not exist.\n"
        #add a new contact
        elif (ans == '4'):
            call(["clear"]) #clear the screen
            #gather new contact info
            newContact = input("Who would you like to add? (enter user name): ")
            newHost = input("Enter hostname/ip address: ")
            newPort = input("Enter the port number: ")
            #add it to address book and display results
            result = addToAddressBook(newContact, newHost, newPort, "address.txt")
            display = "Added '" + result + "' to address book!\n"
        #quit
        elif (ans == '5'):
            return 1
    
main()

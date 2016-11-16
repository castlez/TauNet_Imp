#TauNet Client Program
#Copyright (c) 2015 Jonathan Castle

#First version of the utilities for
#TauNet messaging system.

import socket
from crypto import *
import os.path
from datetime import *
import time
import traceback

#sends a message to the user with the given user name (or host name)
def sendMessage(username, port, k):

    #create the socket and get the host name
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    host = getHost(username,"address.txt")
    
    try:
        #attempt to connect to the host and send a message 
        s.connect((host, int(port)))
        message = input("what is your message? ")
        toSend = "version: 0.2\r\nfrom: castlez\r\nto: " + username + "\r\n" + "\r\n" + message + "\r\n"
        toSend = encrypt(toSend,20,k)
        s.send(toSend)
        
        #close the connection
        s.close()
    except Exception as inst:
        #log error, close the connection and return failure
        trace = traceback.format_exc()
        logError(inst, trace)
        s.close()
        return 0
    
    #return success
    return 1

#logs an error
def logError(inst,trace):
    err = open("errorlog.txt",'a')
    ts = time.time()
    t = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    emessage  = "\n##########\nTimestamp: " + str(t)
    emessage += "\nInstance: " + str(type(inst))
    emessage += "\nStack Trace: \n" + trace
    emessage += "\n##########\n\n"
    err.write(emessage)
    err.close()

#reads the address book file and returns its contents
def getAddressBook(aBook):
    if (os.path.isfile(aBook) == False):
        return "0"
    f = open(aBook, 'r')
    r = f.read()
    f.close()
    return r

#reads the messages file and returns its contents
def readMessages(log):
    if (os.path.isfile(log) == False):
        return "0"
    f = open(log,'r')
    r = f.read()
    f.close()
    return r

#attempts to get the host name from the address book.
#if it fails to find the name in the address book
#it returns the supplied username (allows passing
#of raw host names)
def getHost(username,aBook):
    if (os.path.isfile(aBook) == False):
        return username

    f = open(aBook, 'r')
    for line in f:
        if username in line:
            r = line.split(",")[1]
            f.close()
            return str(r)
    f.close()
    return username

#checks if the message has an empty body
#also implicitly rejects improperly formatted
#messages
def isEmptyMessage(message):
    parts = message.split("\r\n")
    if (parts[4] == ""):
        return True
    return False

#adds a new contact to the address book
def addToAddressBook(newContact, newHost, newPort, addressBook):
    newContactInfo = '\n' + newContact + "," + newHost + "," + newPort
    f = open(addressBook,'a')
    f.write(newContactInfo)
    f.close()
    return newContactInfo



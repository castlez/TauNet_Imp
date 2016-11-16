#TauNet Test Program
#Copyright (c) 2015 Jonathan Castle

#First version of the Test package for
#TauNet messaging system

from util import *
import os

def Test():
    testUtil_sendMessage_invalidInput()
    testUtil_getAddressBook_noFile()
    testUtil_readMesseges_noFile()
    testUtil_getHost_mockedAddressBook()
    testUtil_getHost_missingAddressBook()
    testUtil_isEmptyMessage()
    testUtil_addToAddressBook_newContact()
    testUtil_addToAddressBook_missingFile()


def testUtil_sendMessage_invalidInput():
    assert sendMessage("","","") == 0
    assert sendMessage("127.0.0.1","","keyword") == 0

def testUtil_getAddressBook_noFile():
    assert getAddressBook("doesntexist.NON") == "0"

def testUtil_readMesseges_noFile():
    assert readMessages("doesntexist.NON") == "0"


def testUtil_getHost_mockedAddressBook():
    f = open("testAddressBook.txt",'w')
    f.write("username,hostname,")
    f.close()
    assert getHost("username","testAddressBook.txt") == "hostname"
    os.remove("testAddressBook.txt")

def testUtil_getHost_missingAddressBook():
    assert getHost("wontfindthis","doesntexist.NON") == "wontfindthis"

#tests both empty and non empty messages
def testUtil_isEmptyMessage():
    empty = ""
    m = "version: 0.2\r\nfrom: castlez\r\nto: " + "test" + "\r\n" + "\r\n" + empty + "\r\n"
    assert isEmptyMessage(m) == True

    n = "version: 0.2\r\nfrom: castlez\r\nto: " + "test" + "\r\n" + "\r\n" + "not empty" + "\r\n"
    assert isEmptyMessage(n) == False
 
def testUtil_addToAddressBook_newContact():
    f = open("testAddressBook.txt" , 'w')
    f.write("a,random,contact")
    f.close()
    assert addToAddressBook("testU", "testH","testP","testAddressBook.txt") == "\ntestU,testH,testP"
    t = open("testAddressBook.txt",'r')
    assert t.read() == "a,random,contact\ntestU,testH,testP"
    os.remove("testAddressBook.txt")

def testUtil_addToAddressBook_missingFile():
    assert addToAddressBook("testU", "testH","testP","testAddressBook.txt") == "\ntestU,testH,testP"
    t = open("testAddressBook.txt",'r')
    assert t.read() == "\ntestU,testH,testP"
    os.remove("testAddressBook.txt")


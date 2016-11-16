#TauNet server program
#Copyright (c) 2015 Jonathan Castle

#The first version of the server side
#for the TauNet messaging system.

host = ""
port = 6283
import socket
from crypto import *
from util import *
from test import Test

#execute tests
Test()

#create incoming socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
print("server launched!")

s.listen(5)
k = str.encode("password")

#listen for a connection until the server is aborted
while True:
    conn, addr = s.accept()
    response = conn.recv(1024)
    toRead = decrypt(response,20,k)
    if (len(toRead) == 0): #if the response length is zero, ignore it
        continue

    #print response to terminal and log its contents in log.txt
    print(str(toRead))

    #if the message body is empty, discard it
    if (isEmptyMessage(str(toRead))):
        continue
    f = open("log.txt",'a')
    f.write("\n##Message from '" + str(addr[0]) + "' ##\n")
    f.write(str(toRead))

    #close the connection
    f.close()


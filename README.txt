TauNet Version 0.2
Copyright (c) 2015 Jonathan Castle

This is the informational document for the TauNet
node messaging system. It will cover how to install
and run the TauNet system, as well as clarify any
possible problems with execution.

INSTALLATION
To install the TauNet Messaging System, place
the "server.py", "client.py", "crypto.py", "util.py", and 
"test.py" into the same directory.

EXECUTION
The server portion of this system (server.py) needs to be
running to receive messages. The client portion of the
system (client.py) will be executed to read messages,
check the address book, and send messages. Both modules
must be run on the same raspberry pi for the TauNet system
to run as desired. 

>To execute the server (must stay open to receive messages)
>>python3 server.py

>To execute the client
>>python3 client.py

NOTE
The only way the client and server can be run in the same 
terminal is if you run the server as a background process 
(the way this is done depends on the system).

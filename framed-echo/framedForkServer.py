#! /usr/bin/env python3
import sys, os, socket
sys.path.append("../lib")       # for params
import params

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

while True:
    sock, addr = lsock.accept()

    from framedSock import framedSend, framedReceive

    if not os.fork():
        print("new child process handling connection from", addr)
        fileString = ""
        while True:
            payload = framedReceive(sock, debug)
            if debug: print("rec'd: ", payload)
            if payload: fileString += payload.decode().replace("\x00", "\n")
            else:
                auxStrArr = fileString.split("//myname")
                if os.path.exists(os.path.join(os.getcwd()+"/receiving/"+ auxStrArr[0])):
                    print("Have to overwrite")
                myPath = os.path.join(os.getcwd()+"/receiving/"+auxStrArr[0])
                with open(myPath, 'w') as file:
                    file.write(auxStrArr[1])
                    file.close()
                    sys.exit(1)
            payload += b"!"             # make emphatic!
            framedSend(sock, payload, debug)

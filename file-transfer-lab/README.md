#File Transfer Lab
It's a simple file transfer protocol which opens the files from the client and transfers it to the server
into the "received" folder.

* How To Use:
    - If you want to use the proxy first go to the folder stammer-proxy and run it with:
        `$ ./stammerProxy.py
    - Open run the file server with:
        `$ python3 fileForkServer.py
    - To run the client use:
        `$ python3 fileClient.py
        You'll be prompted to select if you want to use the proxy (type "p") or not (type"l"), 
        the proxy must be running beforeif you want to use it. Then, you'll be prompted to enter the
        name of the file you want to transfer, if the name of the file is incorrect you'll be prompted
        to  try again until it's correct.
* Where is it transfered:
    It will be transfered to an auxiliary folder called "receiving" inside the same folder that the 
    fileForkServer is located.
* When a file already exists:
    If the file being received already exists on the directory the user will be prompted to write  a
    new file name, optionally (s)he can decided to leave it with the original name and overwrite the
    past copy.
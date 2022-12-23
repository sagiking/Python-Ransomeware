There are three python scripts:
One to encrypt the files (ransomeware.py)
One to decrypt the files (ransomeware_dec.py)
One to open http server (server.py)

The encrypting file generate a random key, and going through all the files
in the path thats written in the program, and encrypt only the files with the specific extensions
thats wriiten in the enc_ext list, the program using xor with the random key and sending 
the key to a web server thats listen in port 80 in post request.
After the file has finished running it deletes itself.

To start the python programs you need to install the moudles inside the files
or to compiled to executable file (dont forget to change the file name in the encryption constants).

The decypting file getting as a input the key and going through all the files
in the path thats written in the program, and decrypt only the files with the specific extensions
thats wriiten in the enc_ext list, the program using the same method and xor the data with the key.

The server script is for getting the key and store it, its store the data in a file thats called .logs

The encryption program need a listening http server on port 80 that can accept
post requests for it to work, you can use the python script i uploaded
thats called server.py, or make yourself a new one.


Any use of the software is at your own risk!

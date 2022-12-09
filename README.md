There are two python scripts:
One to encrypt the files
One to decrypt the files

The encrypting file generate a random key, and going through all the files
in the path thats written in the program, and encrypt only the files with the specific extensions
thats wriiten in the enc_ext list, the program using xor with the random key and sending 
the key to a web server thats listen in port 80 in post request.
After the file has finished running it deletes itself.

The decypting file getting as a input the key and going through all the files
in the path thats written in the program, and decrypt only the files with the specific extensions
thats wriiten in the enc_ext list, the program using the same method and xor the data with the key.

The encryption program need a listening http server on port 80 that can store
post requests for it to work.


Any use of the software is at your own risk!

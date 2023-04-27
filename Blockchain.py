#!/usr/bin/python3

import sys
import os
from os.path import exists
import datetime
import struct
import hashlib
from hashlib import *
import uuid

# --------------------------------------
# get environment variable
# --------------------------------------
#for gradescope
path = os.getenv("BCHOC_FILE_PATH")

#for testing
#path = "./output.txt"

chain = []

# --------------------------------------
# add
# --------------------------------------
def add(path, caseID, items):

    # if path exists------------- 
    if (exists(path) == True):
        print ("Case: ", caseID)


        # open and read binary from path
        file = open(path, 'rb')
        file_data = file.read()

        # add block
        prev = ''
        prev_hash = str.encode(prev)

        time_now = (datetime.datetime.now()).timestamp()

        case_id = caseID.replace("-", "")
        evidence_item = 0
        state = "CHECKEDIN"
        state_b = bytes(state, "utf-8")
        data_length = 0
        data = b''
        

        for i in items:
            print("Added item: ", i)
            print("\tStatus: ", state)
            print("\tTime of action: ", time_now)

            evidence_item = int(i)
            # open and read and add to path
            with open(path, 'ab') as file:

                file.write(

                    # struct.pack("format", prev_hash, time_now, case_id, evidence_item, state, data_length, data)
                    struct.pack("32s d 16s I 12s I", 
                                *(prev_hash, time_now, bytes(reversed(uuid.UUID(case_id).bytes)), evidence_item, state_b, data_length)
                    )
                )
                file.write(
                    struct.pack("14s", data)
                )
        
    # else (if path does not exist)------------- 
    elif (exists(path) == False):
        init(path)
# --------------------------------------
# checkout
# --------------------------------------
def checkout():
    print("checkout")

# --------------------------------------
# checkin
# --------------------------------------
def checkin():
    print("checkin")
    
# --------------------------------------
# log
# --------------------------------------
def log():
    print("log")    
    
# --------------------------------------
# remove
# --------------------------------------
def remove():
    print("remove")      

# --------------------------------------
# init
# --------------------------------------
def init(path):
    
    # if path does not exist------------- 
    if not exists(path):
        print("Blockchain file not found. Created INITIAL block.")
        
        # create block
        prev = ''
        prev_hash = str.encode(prev)
        time_now = (datetime.datetime.now()).timestamp()
        case_id = str.encode('')
        evidence_item = 0
        state = "INITIAL"
        data_length = 14
        data = 0

        # create and write to file
        with open(path, 'ab') as file:

            file.write(

                # struct.pack("format", prev_hash, time_now, case_id, evidence_item, state, data_length, data)
                struct.pack("32s d 16s I 12s I", 
                            *(prev_hash, time_now, case_id, evidence_item, str.encode(state), data_length)
                )
            )

    # if path exists------------- 
    elif exists(path):
        print("Blockchain file found with INITIAL block.")
        exit(0)
    
# --------------------------------------
# verify
# --------------------------------------
def verify():
    print("verify")      
  

# --------------------------------------
# input parsing
# --------------------------------------
input = (sys.argv)
caseID = 0
itemID = 0

if (len(input)) > 1:

    # if 2nd argument is "add" ------------- 
    if input[1] == "add":
    
        items = []
    
        # if 3rd argument is "-c"
        if input[2] == "-c":
            caseID = input[3]
        else:
            exit(1)
        if len(input) > 5:
            exit(1)
        # loop for item_number input
        for i in range(4, len(input), 2):
            if input[i] == "-i":
                itemID = input[i+1]
                items.append(itemID)

        add(path, caseID, items)

    
    # if 2nd argument is "checkout" -------------     
    elif input[1] == "checkout":
        checkout()
         
        # item_id input
        if input[2] == "-i":
            itemID = input[3]
        
    # if 2nd argument is "checkin" -------------     
    elif input[1] == "checkin":
        checkin()
                
        # item_id input
        if input[2] == "-i":
            itemID = input[3]
        
    # if 2nd argument is "log" -------------     
    if input[1] == "log":
        log()   
        
        # loop for log input 
        for i in range(1, len(input)):
            
            if input[i] == "-r":
                print("-r")
                
            elif input[i] == "-n":
                numEnteries = input[i + 1]
                
            elif input[i] == "-c":
                caseID = input[i + 1]
                
            elif input[i] == "-i":
                itemID = input[i + 1]
      
    # if 2nd argument is "remove" -------------     
    elif input[1] == "remove":
        items = []     
        
        # item_number input
        if input[2] == "-i":
            itemID = input[3]
            
        # reason input
        if input[4] == "-y":
            reason = input[5]
            
         # loop for owner input
        for i in range(6, len(input), 2):
            if input[i] == "-o":
                itemID = input[i+1]
                items.append(itemID)
                
        remove()

    # if 2nd argument is "init" ------------- 
    elif input[1] == "init":
        if len(input)> 2:
            exit(1)
        else:
            init(path)

    # if 2nd argument is "verify" -------------     
    elif input[1] == "verify":
        verify() 

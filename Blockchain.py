#!/usr/bin/python3

import sys
import datetime

chain = []

class block:
    def __init__(self, caseID, itemID, state, time_now):
        self.caseID = caseID
        self.itemID = itemID
        self.state = state
        self.time_now = time_now
        
        print("Added item: ", self.itemID)
        print("  Status: ", self.state)
        print("  Time of action: ", self.time_now)  

# --------------------------------------
# add
# --------------------------------------
def add(caseID, itemID, state = "CHECKEDIN"):
    
    time_now = datetime.datetime.now()
    
    if len(chain) == 0:
        print("Case: ", caseID)
        chain.append(block(caseID, itemID, state, time_now))
        
    elif chain[len(chain)-1].caseID == caseID:
        chain.append(block(caseID, itemID, state, time_now))
        
    elif chain[len(chain)-1].caseID == caseID:
        print("Case: ", caseID)
        chain.append(block(caseID, itemID, state, time_now))
   
        
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
def init():
    print("init")
    
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
    
        # if 3rd argument is "-c"
        if input[2] == "-c":
            caseID = input[3]
    
        # loop for item_number input
        for i in range(4, len(input), 2):
            if input[i] == "-i":
                itemID = input[i+1]
                add(caseID, itemID)
        
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
        remove()       
        
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
        
    # if 2nd argument is "init" ------------- 
    elif input[1] == "init":
        init()       
        
    # if 2nd argument is "verify" -------------     
    elif input[1] == "verify":
        verify() 

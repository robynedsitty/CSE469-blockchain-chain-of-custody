#!/usr/bin/python3

import sys

def add():
    print("add")

def checkout():
    print("checkout")

def checkin():
    print("checkin")
    
def log():
    print("log")    
    
def remove():
    print("remove")      

def init():
    print("init")
    
def verify():
    print("verify")      
    
input = (sys.argv)

if (len(input)) > 1:

    # if 2nd argument is "add" ------------- 
    if input[1] == "add":
        add() 
    
        # if 3rd argument is "-c"
        if input[2] == "-c":
            caseID = input[3]
            print(caseID)
    
        # loop for item_number input
        for i in range(4, len(input), 2):
            if input[i] == "-i":
                itemID = input[i+1]
                print(itemID)
        
        
    # if 2nd argument is "checkout" -------------     
    elif input[1] == "checkout":
        checkout()
         
        # loop for item_number input
        for i in range(4, len(input), 2):
            if input[i] == "-i":
                itemID = input[i+1]
                print(itemID)
        
    # if 2nd argument is "checkin" -------------     
    elif input[1] == "checkin":
        checkin()
                
        # loop for item_number input
        for i in range(4, len(input), 2):
            if input[i] == "-i":
                itemID = input[i+1]
                print(itemID)
        
    # if 2nd argument is "log" -------------     
    if input[1] == "log":
        log()   
        
        # loop for log input 
        for i in range(1, len(input)):
            
            if input[i] == "-r":
                print("-r")
                
            elif input[i] == "-n":
                print("-n")
                
            elif input[i] == "-c":
                print("-c")
                
            elif input[i] == "-i":
                print("-i")
      
    # if 2nd argument is "remove" -------------     
    elif input[1] == "remove":
        remove()       
        
    # if 2nd argument is "init" ------------- 
    elif input[1] == "init":
        init()       
        
    # if 2nd argument is "verify" -------------     
    elif input[1] == "verify":
        verify() 

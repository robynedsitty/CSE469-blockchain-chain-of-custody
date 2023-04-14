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
    
    
if (len(sys.argv)) > 1:
    arg1 = sys.argv[1]

    # if 2nd argument is "add" ------------- 
    if arg1 == "add":
        add() 
        
    # if 2nd argument is "checkout" -------------     
    elif arg1 == "checkout":
        checkout()
        
    # if 2nd argument is "checkin" -------------     
    elif arg1 == "checkin":
        checkin()
        
    # if 2nd argument is "log" -------------     
    elif arg1 == "log":
        log()    
      
    # if 2nd argument is "remove" -------------     
    elif arg1 == "remove":
        remove()       
        
    # if 2nd argument is "init" ------------- 
    elif arg1 == "init":
        init()       
        
    # if 2nd argument is "verify" -------------     
    elif arg1 == "verify":
        verify()    

#!/usr/bin/env python

#Code in sublime, test in terminal.

import threading

def do_this():
    print "This is the second thread!"
    
    global dead # initialising flag in this function, Note that the value will be updated in real time.
    
    x=0 #Counter to checkout how many time the loop is running
    #Creating an infinite loop
    while( not dead):
        x += 1
        pass    #Infinite loop, Infinitely does nothing.
    print x
    
def main():
    
    global dead     #Creating a flag of sorts to exit the infinite loop
    
    dead = False    #Making the initial value False , so the other thread won't go into infinite loop initially.
    
    #creating a new thread object
    new_thread = threading.Thread (target=do_this)
    #target() : specifies what to execute on making the object
    new_thread.start() # Executes new_thread.run
    #Runs the new_thread object we made
    
    print "This is the first thread."
    
    print threading.active_count()
    print threading.enumerate()
    print threading.current_thread()
    
    raw_input ("Hit enter to die!")
    dead = True     #Updates dead to True GLOBALLY.
    
if ( __name__=="__main__"):
    main()

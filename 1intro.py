#!/usr/bin/env python

import threading

def do_this():
    print "This is the second thread!"
    
    #Creating an infinite loop
    while(True):
        pass    #Infinite loop, so only this thread is working now. Infinitely doing nothing.
    
def main():
    #creating a new thread object
    new_thread = threading.Thread (target=do_this)
    #target() : specifies what to execute on making the object
    new_thread.start() # Executes new_thread.run
    #Runs the new_thread object we made
    print threading.active_count()
    print threading.enumerate()
    print threading.current_thread()
    
if ( __name__=="__main__"):
    main()

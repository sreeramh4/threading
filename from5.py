#!/usr/bin/env python

import threading

def do_this():

	global x
	print "This is the second thread's counter"
	while( x<300):
		x +=1
	print x

def do_after():
	global x
	print "This is the third thread's counter"
	while (x< 600):
		x += 1
	print x


def main():
	global x
	x=0

	print "This is the First thread"
	thread_duo = threading.Thread( target= do_this, name= "alt1" )
	thread_duo.start()
	thread_duo.join #Would ensure that the next thread is executed only after this threads done.

	thread_trio = threading.Thread( target= do_after, name= "alt2" )
	thread_trio.start()

if ( __name__ == "__main__"):
	main()

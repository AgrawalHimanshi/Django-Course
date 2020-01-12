try:
    f=open('simple.txt','r')
#use 'w' instead or 'r' to avoid error
 #will produce error during writing but will continue.
    f.write('test write to simple text!')
#can also use except only witn no IOError to
#consider all types of errors
except IOError:
    print("ERROR: COULD NOT FIND FILE OR DATA!")
# else:
#     print("SUCCESS!")
#     f.close()
#after error also if we want to continue a work
#then instead of else use finally kerword
finally:
    print("I always work!")

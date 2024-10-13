import time
print (time.localtime())
print()
print()

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
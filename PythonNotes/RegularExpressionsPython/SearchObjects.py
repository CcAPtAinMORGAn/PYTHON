import re
line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
 print ("match --> matchObj.group() : ", matchObj.group())
else:
 print ("No match!!")
#matchObj is unable to match with word dogs as dogs is last word of
#the sentence that is why we need to use searchObj
searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
    print ("search --> searchObj.group() : ", searchObj.group())
else:
 print ("Nothing found!!")

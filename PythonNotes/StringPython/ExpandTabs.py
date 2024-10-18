str = "this is\tstring example....wow!!!"
print ("Original string: " + str)

print ("Default exapanded tab: " + str.expandtabs())

print ("Double exapanded tab: " + str.expandtabs(16))
# Double Expanded Tab: Here, expandtabs(16) replaces the tab with
# 16 spaces instead.

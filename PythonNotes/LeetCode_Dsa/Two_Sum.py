nums = [2,5,11,7]

target = 9

n = len(nums)

map = {}


for i in range(n):
  
  x = target - nums[i]
  
  if x in map:
    print(map[x] , i )
    break
  
  map[nums[i]] = i

  print(map)  
  
  

    # map = [2   ]
    # 9 - 2 = 7     2 is stored in num map
    # 9 - 7 = 2     2 is found in num map
    
    # if x i.e difference is found in num map print the index of number stored in the map
    # here 2 is stored at index 0 in  the map so we print the index 0 
    # also we print the index of the number 7 from nums array i.e 1
    
    # 9 - 11 = -2
    # 9 - 15 = -6
    
    
    
    

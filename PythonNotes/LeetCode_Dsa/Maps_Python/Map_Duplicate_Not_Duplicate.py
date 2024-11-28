nums = [2, 8, 10, 10, 11,10,11,11]

n = len(nums)

map = {}


x = -1

for i in range(n):
  
  if nums[i] in map:
    print(nums[i])
    
      
  else:
    x+=1
    map[nums[i]] = x
  
      
print(map)

print(map[10])

print(map[11])
  
print(map[2])
    

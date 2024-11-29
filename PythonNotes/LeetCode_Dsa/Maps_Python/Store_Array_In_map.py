
nums = [2,5,1,7,8]

map = {}

n = len(nums)

for i in range(n):
  
  print(nums[i] ,"at index",i)
  
  map[nums[i]] = i
  
print(map)  
  

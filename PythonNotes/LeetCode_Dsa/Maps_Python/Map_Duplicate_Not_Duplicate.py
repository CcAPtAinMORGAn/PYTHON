
nums = [1,2,3,10,10]


n = len(nums)

map = {}

for i in range(n):
  
  map[nums[i]] = i
  
print(map)

x = len(map)

if(x<n):
  print("contains duplicate")
  
else:
  print("Doesn't contain duplicate")

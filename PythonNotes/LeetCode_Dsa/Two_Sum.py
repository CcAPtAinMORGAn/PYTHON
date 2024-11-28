
nums = [2,7,11,15]

target = 9

numMap = {}
n = len(nums)

for i in range(n):
    x = target - nums[i]
    
    if x in numMap:
      print(numMap[x], i)
    
    numMap[nums[i]] = i

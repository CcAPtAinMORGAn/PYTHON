nums = [2,7,11,15]
Target=int(input("Enter Target: "))

for i in range (0,4):
    for j in range (i+1,4):
        if(nums[i]+nums[j]==Target):
            print("Target is sum of index",i,"and",j,".")
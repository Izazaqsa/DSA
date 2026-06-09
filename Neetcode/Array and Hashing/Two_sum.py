nums = [3,4,5,7]
target = 7
indices = []
def checking (nums, target):
    for i in range (len(nums)):
        for j in range (1,len(nums)):
            if (nums[i]+nums[j]==target) and i != j:
                indices.extend([i,j])
                return indices
            
print (checking(nums, target))
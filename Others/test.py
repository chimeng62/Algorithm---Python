from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
        
    counter = 0
    maxCounter =0
    
    for e in nums:
        if nums[e] == 1:
            print("Counter++")
            counter += 1
            
            if  counter > maxCounter :
                maxCounter = counter
        else:
            counter = 0
            
    return maxCounter

n = [1,0,1,1,1,1,0,1]

print(findMaxConsecutiveOnes(n))
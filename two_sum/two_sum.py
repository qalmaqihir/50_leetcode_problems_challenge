from typing import List


def two_sum_naive(nums:List[int], target:int)-> List[int]:
    count = 0
    while count<len(nums):
        check = target - nums[count]
        for i in range(0,len(nums)):
            if i == count:
                continue
            if nums[i]==check:
                return [count,i]
        count+=1


# nums = [2,7,11,15]
# target = 9

# nums = [3,2,4]
# target = 6

nums = [3,3]
target = 6

print(two_sum_naive(nums,target))






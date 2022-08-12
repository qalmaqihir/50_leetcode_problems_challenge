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


def two_sum_dict(nums:List[int], target:int)-> List[int]:
    check_dict = {}
    n = len(nums)
    # print(f"Starting dictionary {check_dict}")
    for i in range(0, n):
        check = target - nums[i]
        if (check in check_dict):
            # print(f"found value of {check} at check_dict[check] = {check_dict[check]}")
            return [check_dict[check], i]
        # print(f"dictionary after adding {check} to it {check_dict}")
        # print(f"Value of check_dict[nums[i]] = {check_dict[nums[i]]}")
        check_dict[nums[i]] = i

    # check_dict={}
    # print(f"Starting dictionary {check_dict}")
    # for i in range(len(nums)):
    #     check = target-nums[i]
    #     if check not in check_dict:
    #         check_dict[nums[i]]=i
    #         print(f"dictionary after adding {check} to it {check_dict}")
    #         print(f"Value of check_dict[nums[i]] = {check_dict[nums[i]]}")
    #     print(f"found value of {check} at check_dict[check] = {check_dict[check]}")
    #     return [check_dict[check],i]




nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

# nums = [3,3]
# target = 6

# print(two_sum_naive(nums,target))
print(two_sum_dict(nums,target))






from typing import List


def contain_duplicates_naive(nums:List[int])-> bool:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i==j:
                continue
            elif nums[i]==nums[j]:
                return True
    return False

def contain_duplicates_optimzied(nums:List[int])-> bool:
    check_dict={}
    print(f"Dictionary at start = {check_dict}")
    for i in range(len(nums)):
        if nums[i] in check_dict:
            print(f"nums[i] {nums[i]} is in dictionary at {i}")
            return True
        check_dict[nums[i]]=False
        print(check_dict)








nums=[1,2,3,1]
# print(contain_duplicates_naive(nums:List[int])-> bool:)
print(contain_duplicates_optimzied(nums))

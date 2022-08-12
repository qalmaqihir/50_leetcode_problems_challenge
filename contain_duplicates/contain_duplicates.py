from typing import List


def contain_duplicates(nums:List[int])-> bool:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i==j:
                continue
            elif nums[i]==nums[j]:
                return True
    return False


nums=[1,2,3,1]
print(contain_duplicates(nums))

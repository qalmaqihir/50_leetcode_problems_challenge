from typing import List


def majority_element(nums:List[int])->int:
    m={}
    for i in range(len(nums)):
        if nums[i] in m:
            m[nums[i]]+=1
            if m[nums[i]]>len(nums)//2:
                return nums[i]
        else:
            m[nums[i]]=1

m={}
n=[2,3,4,0,0,3,3]
for i in range(len(n)):
    if n[i] in m:
        m[n[i]]+=1
    m[n[i]]=1
print(m)

nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
print(majority_element(nums))

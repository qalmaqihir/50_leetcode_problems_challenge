from typing import List


def single_number_formula(nums:List[int])->int:
    # A mathematical solution
    all_sum = sum(nums)
    unique_sum = sum(set(nums))
    # Use the formual 2*unique_sum-sum = ans
    return 2 * unique_sum - all_sum



def single_number_my(nums: List[int]) -> int:
    m = {}
    for i in nums:
        if i not in m:
            m[i] = 1
        else:
            m[i] = 2
    print(m)
    for i in m:
        print('m[i] = ', m[i])
        print('i = ', i)
        if m[i] == 1:
            print('inside if', i)
            return i


nums=[2,2,1,4,4]

nums=[4,1,2,1,2]

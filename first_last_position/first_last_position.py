from typing import List


def first_last_position(nums:List[int], target:int)-> List[int]:
    left = 0
    right = len(nums) - 1
    found = [-1, -1]
    while left <= right:
        if nums[left] == target:
            found[0] = left
            print(f"left found at {left}")
            break
        left += 1
    while left<=right:
        if nums[right] == target:
            found[1] = right
            print(f"right found at {right}")
            break
        right -= 1
    return found



print(first_last_position([5,7,7,8,8,10],8))



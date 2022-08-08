from typing import List


def container_with_most_water(height: List[int])-> int:
    left =0
    right =len(height)-1
    max_height=-100000000000000000
    while left<=right:
        distance =  right-left
        heights = min(height[left],height[right])
        new_height= distance*heights
        max_height=max(max_height, new_height)
        if height[left]>height[right]:
            right-=1
        elif height[left]<height[right]:
            left +=1
        else:
            left+=1
            right-=1

    return max_height


height = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water(height))
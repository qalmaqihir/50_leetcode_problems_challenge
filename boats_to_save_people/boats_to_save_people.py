import math
from typing import List


def boats_to_save_people(people:List[int], limit:int)-> int:
    boats=0
    left=0
    right=len(people)-1
    people.sort()
    while left<=right:
        if people[left]==limit:
            boats+=1
            left+=1
        elif people[right]==limit:
            boats+= 1
            right-=1
        elif people[right]+people[left]==limit:
            boats+=1
            left+=1
            right-=1
        elif people[right]+people[left]>limit:
            right-=1
            boats+=1
        elif people[right]+people[left]<limit:
            left+=1
            boats+=1
            right-=1
    return boats

    # for i in range(len(people)-1):
    #     if people[i]==limit:
    #         people.remove(people[i])
    #         boats+=1
    #     else:
    #         for j in range(len(people)-1):
    #             if people[i]+people[j]==limit:
    #                 people.remove(people[i])
    #                 people.remove(people[j])
    #                 boats+=1
    # boats+=len(people)
    # return boats






people = [3, 5, 3, 4]
limit = 5
print(boats_to_save_people(people, limit))

# checked = dict()
# boats=0
# limit=3
# for i in range(len(people)):
#     if people[i]==limit:
#         boats+=1
#     else:
#         target=math.abs(limit-people[i])
#
#
#     checked[people[i]]=0
#
#
# print(checked)


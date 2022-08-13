from typing import List


def group_anagram(strs:List[str])-> List[List[str]]:
    m={}
    for i in range(len(strs)):
        hashed=''.join(sorted(strs[i]))
        if  hashed not in m:
            m[hashed]=[]
        m[hashed].append(strs[i])
    return list(m.values())



strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(strs))


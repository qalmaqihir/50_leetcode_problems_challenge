def anagram_solution2(s1,s2):
    list1=list(s1)
    list2=list(s2)

    list1.sort()
    list2.sort()

    pos=0
    matches=True
    while pos < len(list2):
        if list2[pos]==list1[pos]:
            pos+=1
        else:
            matches=False

    return matches



print(anagram_solution2('abcde','edcba'))
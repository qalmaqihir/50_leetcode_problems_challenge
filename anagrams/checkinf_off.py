def anagram_solution1(s1, s2):
    a_list=list(s2)

    pos=0
    still_ok = True
    while pos<len(a_list) and still_ok:
        pos2=0
        found=False
        while pos2<len(a_list) and not found:
            if s1[pos]==s2[pos2]:
                found=True
            else:
                pos2+=1
        if found:
            a_list[pos2]=None
        else:
            still_ok=False
        pos+=1
    return still_ok



print(anagram_solution1('abcd','dcba'))

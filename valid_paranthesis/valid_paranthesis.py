def is_equal(c1,c2):
    if c1=="(" and c2==")":
        return True
    if c1=="{" and c2=="}":
        return True
    if c1=="[" and c2=="]":
        return True
    return False


def valid_paranthesis(s:str)->bool:
    st=[]
    for character in s:
        if (len(st)!=0):
            li =st[-1]
            if (is_equal(li, character)):
                st.pop()
                continue
        st.append(character)
    return len(st)==0



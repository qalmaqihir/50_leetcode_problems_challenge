def backtracking(ans,m,digits,combination, index):
    if index>len(digits):
        return
    if len(combination)==len(digits):
        ans.append(combination[:])
        return

    current_digit=digits[index]
    current_string=m[current_digit]

    for i in range(len(current_string)):
        backtracking(ans,m,digits,combination+current_string[i],index+1)

    def letter_combinations(digits,):
        ans=[]
        if len(digits)==0:
            return ans
        m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        backtracking(ans,m,digits,"",0)
        return ans
    

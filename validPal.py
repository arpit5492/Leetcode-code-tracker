import re

def isPalindrome(s):
    extr_str = re.sub(r'[^a-zA-Z0-9]', '', s)
    lower_str = extr_str.lower()
    #start pointer
    i = 0
    #end pointer
    j = len(lower_str)-1
    while(i<j):
        if(lower_str[i]!=lower_str[j]):
            return False
        else:
            i=i+1
            j=j-1
    return True

print(isPalindrome('A man, a plan, a canal: Panama'))
        

def isPalindrome(s):
    #code here
    s1=s[::-1]
    s2=''.join(s1)
    if s.casefold()==s2.casefold():  #to ignore the upper/lowe case structure .casefold()
        return True
    else:
        return False
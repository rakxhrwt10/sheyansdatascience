This solution does not use the string functions like tolower() or islower(). Only ASCII values.
class Solution:
    def toLower (self , s : str)-> str :
        #code here
        temp = ''
        res = ""
        for c in s:
            if ord(c) >= 65 and ord(c) <= 90:
                temp = chr(ord(c) + 32)
                res += temp
            else:
                res += c
            
        return res
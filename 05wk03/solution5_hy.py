
'''
https://leetcode.com/problems/string-to-integer-atoi

05/17/2020
regex 사용 - Runtime: 32 ms, faster than 73.48% / Memory Usage: 13.9 MB, less than 5.95% of submissions
대략.. 50% faster 인거 같다

Remarks:
 - import re의 위치가 속도에 영향이 있는거 같다. class 위에 했을때가 제일 빠르다.
 - regex 사용해서 조금 더 느린거 같지만.. re를 사용하는게 똘똘한 방법이 아닐까..

'''


import re   

class Solution:
    
    def myAtoi(self, str: str) -> int:
        
        MAX_INT = 2147483647  # (2**31) - 1
        MIN_INT = -2147483648  # -2**31

        p = re.compile(r'[-+]?[0-9]+')
        num_list = p.findall(str.lstrip())
        
        if str.lstrip() == "" or not num_list:
            return 0
        
        if str.lstrip()[0].isdigit() \
        or ((str.lstrip()[0] == '-' or str.lstrip()[0] == '+') and str.lstrip()[1].isdigit()):
            
            num = int(num_list[0])

            if num <= MIN_INT: 
                return MIN_INT

            elif num >= MAX_INT:
                return MAX_INT

            return num
        
        else:
            return 0

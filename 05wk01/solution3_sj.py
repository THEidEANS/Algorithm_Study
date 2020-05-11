# Somjang 05/11/2020
class Solution_sj:
    def lengthOfLongestSubstring(self, my_str: str) -> int:
        answer = 0
        
        substrings = []
        
        my_str_list = list(my_str)
        
        set_list = set(my_str_list)
        
        if len(set_list) == 0:
            answer = 0
        elif len(set_list) == 1:
            answer = 1
        else:
            for i in range(len(my_str_list)):
                sub = []
                for j in range(i, len(my_str_list)):
                    if my_str_list[j] in sub:
                        substring = ''.join(sub)
                        substrings.append(len(substring))
                        break
                    sub.append(my_str_list[j])
                    
                    if j == len(my_str_list) - 1:
                        substring = ''.join(sub)
                        substrings.append(len(substring))

            answer = max(substrings)
                            
        return answer
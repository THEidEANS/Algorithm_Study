'''
05032020
처음에 잘 생각하다 하나씩 추가되면서 꼬여버린 더 좋았을법한 로직..!!
일단 Success를 받은 후 다른 solution 참고하여 better solution 시도하였습니다.

Remarks:
 - enumerate()를 쓰자! 친숙하지않았지만 이제부터 친숙해지는걸로
 - position, value 둘다 tracking을 해야한다! - dict를 사용하는걸로

'''

# Finally better solution
class Solution_hy:
    def lengthOfLongestSubstring(self, s: str) -> int:

        counter = 0
        max_val = 0
        dup_idx = 0
        start = 0
        
        # to store key: char, val: index
        pos_dict = {}
        
        for i, val in enumerate(s):
            
            # check if there is duplicate pair
            if val in pos_dict:
                dup_idx = pos_dict[val]
                
                # start postion setup
                if dup_idx >= start:
                    start = dup_idx + 1
                    counter = i - dup_idx
                # id dup_index is smaller than start, we can add to the counter
                else:
                    counter += 1
                    
            # update counter
            else:
                counter += 1
            
            # Add index/val pair
            pos_dict[val] = i
            
            # update max_val
            if max_val < counter:
                max_val = counter
            
        return max_val


# ----------------------------------------------------------------------------

# BAD BAD.. O(n^2)
# First try H.Kim
class bad_Solution_hy:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        str_list = list(s)
        counter = 0
        max_val = 0
        prev_char = ''
        
        # set for tracking duplicate letter
        dup_char = set()
        
        
        for i in range(0, len(s)):
        
            # always less than max
            if max_val >= len(s)-i+1:
                return max_val
                
            # unless dup_char is not found
            j = 0
            while i+j < len(s) and s[i+j] not in dup_char:
                counter += 1
                # add to dup_set
                dup_char.add(s[i+j])
                j += 1 
            
            # longest check
            if max_val < counter:
                max_val = counter
                
            counter = 0        
            dup_char.clear()
            
            
        return max_val


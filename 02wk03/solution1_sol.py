## Sol
class Solution_sol:
    def reverse(self, x: int) -> int:    
        
        if x < 0:
            str_x = str(abs(x))
            result = -int(str_x[::-1])
            return result if pow(-2, 31) < result < pow(2, 31) - 1 else 0
    
        if x >= 0:
            str_x = str(x)
            result = int(str_x[::-1])
            return result if pow(-2, 31) < result < pow(2, 31) - 1 else 0


        if x % 10 == 0:
            str_x = str(x//10)
            result = int(str_x[::-1])
            return result if pow(-2, 31) < result < pow(2, 31) - 1 else 0
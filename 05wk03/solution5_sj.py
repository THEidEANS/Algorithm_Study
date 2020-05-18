import re

class Solution:
    def myAtoi(self, string) -> int:
        answer = 0
        
        string = string.strip()
    
        if string == "":
            answer = 0
        else:
            number_list = re.findall(r"^[-+]?[0-9]+", string)

            print(number_list)

            if len(number_list) == 0:
                answer = 0
            else:
                number = int(number_list[0])
                if number > pow(2, 31) - 1:
                    number = pow(2, 31) -1
                elif number < pow(2, 31) * (-1):
                    number = pow(2, 31) * (-1)

                answer = number
        
        return answer
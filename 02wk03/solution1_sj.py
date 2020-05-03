## Ssomjang
class Solution_sj:
    def reverse(self, input_num: int) -> int:
        input_num_str = str(input_num)
        input_num_str = list(input_num_str)

        if input_num_str[0] == '-':
            input_num_str_new = input_num_str[1:]
            input_num_str_new = reversed(input_num_str_new)
            input_num_str_new = ''.join(input_num_str_new)
            answer = '-' + input_num_str_new

        else:
            input_num_str = reversed(input_num_str)
            answer = ''.join(input_num_str)
            
        if int(answer) > 2 ** 31 or int(answer) < (-2) ** 31:
            return 0
        else:
            return int(answer)
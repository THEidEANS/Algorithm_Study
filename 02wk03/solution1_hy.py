## H.Kim
class Solution_hy:
    def reverse(self, x: int) -> int:

        str_x = str(x)
        list_x = list(str_x)

        half = len(str_x) // 2
        last_indx = len(str_x) - 1

        # 양수인경우
        if x > 0:
            for i in range(0,half):
                temp = list_x[i]
                list_x[i] = list_x[last_indx-i]
                list_x[last_indx-i] = temp

            result_str = ''.join(list_x)

        # 음수인경우
        else:
            for i in range(0,half):
                temp = list_x[i+1]
                list_x[i+1] = list_x[last_indx-i]
                list_x[last_indx-i] = temp

            result_str = ''.join(list_x)


        if int(result_str) < -2**31 or int(result_str) > (2**31)-1:
            return 0
        else:
            return int(result_str)
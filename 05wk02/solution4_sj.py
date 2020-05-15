class Solution_sj:
    def convert(self, s: str, numRows: int) -> str:
        max_interval = 2 * (numRows - 1)
        
        string_len = len(s)
        
        string_list = list(s)
        
        new_string = []
        
        if string_len == 1 or numRows == 1:
            answer = s
        else:
            for i in range(numRows):
                index_num = i

                if (i == 0) or (i == numRows - 1):
                    while True:
                        if index_num > string_len-1:
                            break
                        new_string.append(string_list[index_num])
                        index_num = index_num + max_interval

                else:
                    interval_first = 2 * (numRows - 1 - i)
                    interval_second = max_interval - interval_first

                    count = 0

                    while True:
                        if index_num > string_len-1:
                            break

                        new_string.append(string_list[index_num])

                        if count % 2 == 0:
                            index_num = index_num + interval_first
                        elif count % 2 == 1:
                            index_num = index_num + interval_second

                        count = count + 1

            answer = ''.join(new_string)
        
        return answer
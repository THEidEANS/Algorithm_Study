
'''
https://leetcode.com/problems/zigzag-conversion

05/15/2020
처음에는 딕션너리사용하여 글자별로 좌표를 넣어주어 좌표의 row별 정렬하여 글자 출력 - ~30% 밖에 나오지 않음 쥬륵
솔루션방법 참고하여 다시 시도
똑같이 row가 numRow-1과 0일때 조건을 사용하지만 row별 글자를 저장하여 출력 - ~95% 증가!

Remarks:
    - dict.values()로 looping하여 글자를 붙이는거 보다 join을 사용하였더니 점수가 증가
    - Null condition도 잘 생각하자
    - Memory usage는 능률적이지 않다.. 다 비슷한거 같은데.. (아닌가..)
    - Row별 print이니 제발 row별 저장이 되는 방법을 생각해보자. 무조건 전체저장 아냐야아
'''


class Solution:

    # better solution - beats 95.49%, memory usage is so bad..
    def convert(self, s: str, numRows: int) -> str:

        if not s:
            return ""
        
        if numRows == 1 or len(s) <= numRows:
            return s
        
        result = ''
        row_dict = {}

        # +: 밑으로, -: 대각선으로
        row_dir = 1    
        n_idx = 0

        for i, val in enumerate(s):
            
            # dictionary가 처음이거나 해당 key가 처음 입력될 때
            if n_idx not in row_dict:
                row_dict[n_idx] = val
            else:
                row_dict[n_idx] = row_dict[n_idx] + val

            n_idx += row_dir

            if n_idx == 0 or n_idx == numRows-1:
                row_dir *= -1

                
        return ''.join(row_dict.values())


''''
    # sorting 작업때문인지.. 20-30% 느리다.. 흑흑
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s.strip()) < 3 or numRows == 1 or len(s) <= numRows:
            return s
        
        xy_dict = {}
        result = ''
        
        col = 0
        row = 0
        i = 0

        xy_dict[i] = (col, row)

        # 그림을 그리자
        while i < len(s)-1:
            
            # 대각선을 그리자
            if row == numRows-1:
                while i < len(s)-1 and row > 0:
                    i += 1
                    col += 1
                    row -= 1    
                    xy_dict[i] = (col, row)

            # 직선으로 그리자
            else:
                row += 1
                i += 1
                xy_dict[i] = (col, row)


        # dictionary를 row값으로 정렬.. cost가 많이 나갈거같아...
        sorted_dict_by_row = sorted(xy_dict, key=lambda k: xy_dict[k][1])
        
        # sorted key(index) list를 가지고 result print
        for key in sorted_dict_by_row:
            result += s[key]
        
        return result
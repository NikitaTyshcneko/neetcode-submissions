class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        result_string = ''
        count_one = 1

        for i in s:
            if i == '1' and count_one == 0:
                result_string = '1'+result_string
            elif i == '1' and count_one == 1:
                count_one-=1
            else:
                result_string += '0'

        return result_string+'1'
        
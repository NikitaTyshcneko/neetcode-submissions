class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dict_s = collections.defaultdict(int)

        for i in s:
            dict_s[int(i)]+=1
        
        result_string = '1'*(dict_s[1]-1)
        result_string += '0'*dict_s[0]
        print(result_string)

        return result_string+'1'
        
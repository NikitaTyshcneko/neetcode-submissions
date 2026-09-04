class Solution:
    def isHappy(self, n: int) -> bool:
        n_set = set()
        temp_n = str(n)
        result = 0
        while True:
            result = 0
            for i in temp_n:
                result+=pow(int(i), 2)
            if result in n_set: return False
            if result == 1: return True
            n_set.add(result)
            temp_n = str(result)
        
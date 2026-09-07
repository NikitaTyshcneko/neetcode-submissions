class Solution:
    def largestGoodInteger(self, num: str) -> str:
        counter = 0
        current = ''

        for i, v in enumerate(num):
            if v == num[i-1]: counter+=1
            else: counter=1
            if counter == 3 and current == '': current= v
            elif counter == 3 and int(v) > int(current):
                current = v
        
        return current*3
        
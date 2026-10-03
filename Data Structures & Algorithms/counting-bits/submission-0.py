class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]*(n+1)
        for i in range(n+1):
            result[i]+=i%2
            # if number/2==1: result[i]+=1
            number=i//2
            result[i]+= result[number]
        return result
            

        
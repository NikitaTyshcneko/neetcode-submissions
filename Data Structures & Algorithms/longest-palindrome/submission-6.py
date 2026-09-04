class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_letters = collections.defaultdict(int)
        total = 0
        previous_odd = {'value': 0, 'letter': ''}
        current_odd = {'value': 0, 'letter': ''}

        for i in s:
            dict_letters[i] += 1
            if dict_letters[i]%2==0:
                total+=2
        
        
        for v in dict_letters.values():
            if v%2!=0:
                total+=1
                break
        return total

        
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        string_dict = collections.defaultdict(int)

        for i in arr:
            string_dict[i]+=1
        
        unique = [i for i, v in string_dict.items() if v == 1]

        return unique[k-1] if k<=len(unique) else ''
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        tuple_names=[]

        for i in sorted(dict(zip(heights, names)).items(), reverse=True):
            tuple_names.append(i[1] )

        return tuple_names
        
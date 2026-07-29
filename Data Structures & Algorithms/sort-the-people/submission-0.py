class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs=list(zip(heights,names))
        pairs.sort(reverse=True)
        return [name for _ , name in pairs]








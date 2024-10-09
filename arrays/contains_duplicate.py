class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupliSet = set()
        print(type(dupliSet))
        for i in nums:
            if i in dupliSet:
                return True
            dupliSet.add(i)
        return False
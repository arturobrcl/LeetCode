class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        setArr = list(set(arr))
        occurr = []
        for i in range(len(setArr)):
            if arr.count(setArr[i]) in occurr:
                return False
            else:
                occurr.append(arr.count(setArr[i]))
        
        return True

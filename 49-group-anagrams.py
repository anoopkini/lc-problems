class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnList = collections.defaultdict(list)

        for str in strs:
            counts = [0] * 26

            for char in str:
                counts[ord(char)-ord('a')] += 1
            
            returnList[tuple(counts)].append(str)

        return returnList.values()

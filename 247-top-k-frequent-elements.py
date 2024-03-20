class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # { num -> count}
        # res   = []
        freq  = [[] for i in range(len(nums) + 1)] # [[],[],[],[],[],[],[]]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        # [[],[3],[2],[1],[],[]]
        for num, count in count.items():
            freq[count].append(num)
        
        res = []

        for i in range(len(freq) - 1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
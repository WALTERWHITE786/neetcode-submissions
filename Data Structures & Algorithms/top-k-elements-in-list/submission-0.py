class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
        b=[[] for _ in nums]
        for x in d:
            b[d[x]-1].append(x)
        return [x for f in b[::-1] for x in f][:k]


       




           


        


        
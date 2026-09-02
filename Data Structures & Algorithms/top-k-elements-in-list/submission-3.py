class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for x in nums:
            count[x]=count.get(x,0)+1
        
        buckets=[[] for _ in nums]

        for x in count:
            buckets[count[x]-1].append(x)

        return [x for bucket in buckets[::-1] for x in bucket][:k]
            










       




           


        


        
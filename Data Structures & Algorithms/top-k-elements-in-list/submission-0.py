class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_count = {}
        for i in nums:
            if i not in hash_count:
                hash_count[i] = 1
            else: hash_count[i] += 1
        hash_sorted = dict(sorted(hash_count.items(), key=lambda item: item[1],reverse=True))
        result = []
        for t in hash_sorted:
            k-= 1
            result.append(t)
            if k <= 0:
                break
        return result
        
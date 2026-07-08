class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_string = {}
        for s in strs:
            sr = "".join(sorted(s))
            if sr not in hash_string:
                hash_string[sr] = [s]
            else:
                hash_string[sr].append(s)
        result = []
        for i in hash_string:
            result.append(hash_string[i])
        return result
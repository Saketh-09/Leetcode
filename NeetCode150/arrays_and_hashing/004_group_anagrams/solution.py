class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c) - ord('a')] += 1
            hashMap[tuple(count)].append(i)
        return hashMap.values()
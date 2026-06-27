class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for str1 in strs:
            key = "".join(sorted(str1))
            if key not in grp:
                grp[key] = []
            grp[key].append(str1)
        return list(grp.values())
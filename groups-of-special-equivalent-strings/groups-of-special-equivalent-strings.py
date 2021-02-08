class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = []
        for a in A:
            evens = list(a[::2])
            evens.sort()
            odds = list(a[1::2])
            odds.sort()
            in_special_group=False
            for g in groups:
                if evens==g[0] and odds==g[1]:
                    in_special_group=True
                    break
            if not in_special_group:
                groups.append([evens, odds])
        return len(groups)
                
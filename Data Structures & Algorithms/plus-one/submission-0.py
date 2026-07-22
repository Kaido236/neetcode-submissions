class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        gd1 = map(str,digits)
        gd2 = "".join(gd1)
        gd3 = int(gd2)
        gd4 = gd3 + 1
        gd5 = str(gd4)
        gd6 = list(gd5)
        gd7 = []
        for i in gd6:
            gd7.append(int(i))
        return gd7
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        countt = 0
        for i in details:
            if int(i[11:13]) > 60:
                countt += 1

        return countt
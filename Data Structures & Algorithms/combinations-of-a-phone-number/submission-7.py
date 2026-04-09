class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: "ABC",
            3: "DEF",
            4: "GHI",
            5: "JKL",
            6: "MNO",
            7: "PQRS",
            8: "TUV",
            9: "WXYZ",
        }

        comb = []
        def build_seq(dig, seq):
            print(dig, seq)
            if len(dig)>0:
                for d in mapping[int(dig[0])]:
                    build_seq(dig = dig[1:], seq = seq + str(d).lower())
            else:
                if len(seq)>0:
                    comb.append(seq)

        build_seq(digits, "")
        return comb

        
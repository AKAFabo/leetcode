class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s


        idx = 0
        zigUp = False
        rows = [""] * numRows

        for ch in s:
            rows[idx] += ch

            #Condicion de rebote
            if idx == numRows - 1:
                zigUp = True
            elif idx == 0:
                zigUp = False    

            #Con el rebote cambie el index de cada letra
            if zigUp:
                idx-=1
            else:
                idx+=1

        return "".join(rows)

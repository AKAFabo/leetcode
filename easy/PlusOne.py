class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        x = digits
        x2 = []

        potencia = 10 ** (len(x) - 1)
        n = 0

        #build number

        for i in range(len(x)):

            n = n + x[i] * potencia
            potencia = potencia // 10

        n += 1

        for i in range(len(str(n))):
            x2.append(int(str(n)[i]))



        return x2
                
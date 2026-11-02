class Solution:
    def romanToInt(self, s: str) -> int:

        #Bullshit solution gg
        r = 0
        i = 0
        while i < (len(s)):

            if s[i] == 'I':
                if i + 1 < len(s) and s[i+1] == 'V': 
                    r+=4
                    i+=2
                elif i + 1 < len(s) and s[i+1] == 'X':
                    r+=9
                    i+=2
                else:
                    r+=1
                    i+=1
            elif s[i] == 'V':
                r+=5
                i+=1

            elif s[i] == 'X':
                if i + 1 < len(s) and s[i+1] == 'L':
                    r+=40
                    i+=2
                elif i + 1 < len(s) and s[i+1] == 'C':
                    r+=90
                    i+=2
                else:
                    r+=10
                    i+=1

            elif s[i] == 'L':
                r+=50
                i+=1

            elif s[i] == 'C':
                if i + 1 < len(s) and s[i+1] == 'D':
                    r+=400
                    i+=2
                elif i + 1 < len(s) and s[i+1] == 'M':
                    r+=900
                    i+=2
                else:
                    r+=100
                    i+=1

            elif s[i] == 'D':
                r+=500
                i+=1

            else:
                r+=1000
                i+=1


        return r        


        
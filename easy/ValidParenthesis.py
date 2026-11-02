class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        openBracket = ['(','[','{']
        closeBracket = [')', '}',']']

        for ch in s:
            if ch in openBracket:
                stack.append(ch)

            if ch in closeBracket:

                if not stack:          # cierre sin nada que cerrar
                    return False

                cl = stack[-1]

                if ch == ')' and cl == '(': stack.pop()
                elif ch =='}' and cl == '{': stack.pop()
                elif ch == ']' and cl == '[': stack.pop()

                else:
                    return False

        return not stack

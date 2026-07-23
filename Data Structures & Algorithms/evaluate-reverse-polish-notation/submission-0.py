class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if len(stack) > 1 and i in ["+","-","*","/"]:
                element1 = int(stack.pop())
                element2 = int(stack.pop())

                if i == "+":
                    temp = element1 + element2
                elif i == "-":
                    temp = element2 - element1
                elif i == "*":
                    temp = element2 * element1
                elif i == "/":
                    temp = int(element2 / element1)
                
                stack.append(str(temp))
                continue
            stack.append(i)
        return int(stack[0])
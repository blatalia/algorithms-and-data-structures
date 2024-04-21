"""
stack implementation with postfix notation used for evaluation of mathematical expressions
"""


class Stack:
    def __init__(self, full):
        self.stack = []
        self.full = full

    def is_empty(self):
        if len(self.stack) == 0:
            return True

    def is_full(self):
        if len(self.stack) == self.full:
            return True

    def push(self, a):
        if not self.is_full():
            self.stack += [a]
        # else:
        #     print("The stack is full!")
        # for informing that the stack is full

    def pop(self):
        if not self.is_empty():
            j = self.stack[-1]
            del self.stack[-1]
            # print("This is the popped value: ", j)
            # for printing the popped value
        return j

    def top(self):
        return self.stack[-1]

    def __repr__(self):
        return str(self.stack)

class ConverterEvaluator:
    def __init__(self, infix):
        self.infix = infix
        self.output = [""]
        self.convertedinfix = []

    def infix_to_postfix(self):
        stackpostfix = Stack(len(self.infix))

        self.infix = self.infix.split()
        operators = ['+', '-', '*', '/', '(', ')']
        priority_of_operators = {'(': 0, ')': 0, '*': 1, '/': 1, '+': 2, '-': 2}

        if len(self.infix) != 1:
            for char in self.infix:
                top = stackpostfix.top() if not stackpostfix.is_empty() else 0
                if char not in operators:
                    self.output.append(char)
                elif char in operators and char == "(":
                    stackpostfix.push(char)
                elif char in operators and char == ")":
                    for element in reversed(stackpostfix.stack):
                        if element in operators and element not in "()":
                            j = stackpostfix.pop()
                            self.output.append(j)
                        elif element == "(":
                            stackpostfix.pop()
                            break
                elif char in operators:
                    if not stackpostfix.is_empty():
                        if priority_of_operators[char] > priority_of_operators[top]:
                            stackpostfix.push(char)
                        elif priority_of_operators[char] <= priority_of_operators[top]:
                            while priority_of_operators[char] <= priority_of_operators[top] and not stackpostfix.is_empty():
                                top = stackpostfix.top()
                                if stackpostfix.is_empty() or priority_of_operators[top] < priority_of_operators[char]:
                                    break
                                else:
                                    j = stackpostfix.pop()
                                    self.output += j
                            stackpostfix.push(char)
                    else:
                        stackpostfix.push(char)
            for element in reversed(stackpostfix.stack):
                while not stackpostfix.is_empty():
                    self.output += stackpostfix.pop()
        print("This is the expression in postfix expression:", " ".join(self.output[1:]))
        return self.output[1:]

    def evaluate_postfix(self):
        self.infix_to_postfix()
        stackevaluate = Stack(len(self.infix))
        operators = ['+', '-', '*', '/']
        final_result = ""
        for element in self.output:
            if element not in operators:
                stackevaluate.push(element)
            else:
                x = float(stackevaluate.pop())
                y = float(stackevaluate.pop())
                if element == '+':
                    z = y + x
                    stackevaluate.push(z)
                elif element == '-':
                    z = y - x
                    stackevaluate.push(z)
                elif element == '*':
                    z = y * x
                    stackevaluate.push(z)
                elif element == '/':
                    z = y / x
                    stackevaluate.push(z)
        final_result += str(stackevaluate.pop())
        print("This is the final result: ", final_result)
        return final_result


expression1 = ConverterEvaluator("( 3 * -6 + 2 ) + ( 14.0 / 3 + 4 )")
expression1.evaluate_postfix()

expression2 = ConverterEvaluator("17 * ( 2 + 3 ) + 4 + ( 8 * 5 )")
expression2.evaluate_postfix()
class PrefixToPostfix:
    def __init__(self, expression):
        self.prefix_expression = expression

    def prefix_to_postfix_conversion(self):
        temp_expr = []
        for item in reversed(self.prefix_expression):
            if (item >= 'a' and item <= 'z') or (item >= 'A' and item <= 'Z'):
                temp_expr.append(item)
            else:
                if temp_expr[-1] is not "" and temp_expr[-2] is not "":
                    temp = temp_expr[-1] + temp_expr[-2] + item
                    temp_expr.pop()
                    temp_expr[-1] = temp
        print("Final is: {}".format(temp_expr[0]))


if __name__ == "__main__":
    expr = input("Enter the prefix expression with out any spaces: ")
    pp = PrefixToPostfix(expr)
    pp.prefix_to_postfix_conversion()

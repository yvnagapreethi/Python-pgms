class StackUsingList:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push_an_element(self,ele):
        self.stack.append(ele)

    def print_stack_elements(self):
        for item in self.stack:
            print(item)
    
    def pop_an_element(self):
        if len(self.stack) == 0:
            print("There are no elments in the stack to pop")
        else:
            print("The poped element is: {}".format(self.stack[-1]))
            self.stack.pop()


if __name__ == "__main__":
    stk = StackUsingList()
    while True:
        print("Select any number from below:\n1.Push an element into the stack\n2.Pop out an element from the stack\n3.Display all the elements present in the stack\n")
        digit = int(input("Press the number: "))
        if digit == 1:
            stk.push_an_element(int(input("Enter the element to push into the stack")))
        elif digit == 2:
            stk.pop_an_element()
        elif digit == 3:
            stk.print_stack_elements()
        else:
            break
        
    

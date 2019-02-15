class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None


class StackUsingLinkedList:
    def __init__(self):
        self.root = None

    def push_stack_element(self,data):
        if self.root is None:
            new = StackNode(data)
            self.root = new
        else:
            new_node = StackNode(data)
            new_node.next = self.root
            self.root = new_node

    def pop_stack_element(self):
        if self.root is None:
            print("There are no elements to pop from the stack")
        else:
            print("Popped element is : {}".format(self.root.data))
            self.root = self.root.next

    def display_stack_elements(self):
        temp = self.root
        while temp:
            print(temp.data)
            temp = temp.next

sll = StackUsingLinkedList()
sll.push_stack_element(22)
sll.push_stack_element(45)
sll.push_stack_element(67)
sll.push_stack_element(98)
sll.push_stack_element(23)
sll.display_stack_elements()
sll.pop_stack_element()
sll.pop_stack_element()
sll.display_stack_elements()

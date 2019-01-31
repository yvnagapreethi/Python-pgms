"""Class code goes from here"""
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def create_root_element(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def create_last_element(self,value):
        if self.head is None:
            self.create_root_element(value)
        else:
            temp = self.head
            while temp:
                if temp.next is None:
                    # print("None")
                    node1 = Node(value)
                    temp.next = node1
                    node1.prev = temp
                    break
                temp = temp.next

    def create_middle_element(self, prev_elem, new_ele):
        if self.head is None:
            self.create_root_element(new_ele)
        elif self.head.next is None:
            self.create_last_element(new_ele)
        else:
            temp = self.head
            while temp:
                if temp.data == prev_elem:
                    new_node1 = Node(new_ele)
                    new_node1.next = temp.next
                    new_node1.next.prev = new_node1
                    temp.next = new_node1
                    new_node1.prev = temp
                    break
                temp = temp.next
            else:
                print("The entered element is not in the list.")
                
    def delete_first_element(self):
        if self.head is None:
            print("There are no elements present in the list to delete")
        else:
            print("Head element deleted is: {}".format(self.head.data))
            temporary = self.head.next
            self.head.next = None
            temporary.prev = None
            self.head = temporary
    
    def delete_last_element(self):
        if self.head is None:
            print("There are no elements present in the list to delete")
        elif self.head.next is None:
            self.delete_first_element()
        else:
            temp = self.head
            while temp:
                if temp.next.next is None:
                    print("The last element deleted is: {}".format(temp.next.data))
                    temp.next.prev = None
                    temp.next = None
                    break
                temp = temp.next
    
    def delete_middle_element(self,del_val):
        if self.head is None:
            print("There are no elements present in the list to delete")
        elif self.head.data == del_val:
            self.delete_first_element()
        else:
            
            temp = self.head
            while temp:
                if temp.data == del_val:
                    
                    if temp.next is None:
                        self.delete_last_element()
                        break
                    else:
                        print("The value deleted is {}".format(del_val))
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        break
                temp = temp.next
            else:
                print("No such elements present in the list")
                    

    def print_all_elements(self):
        temp = self.head
        print("The elements present in the list are:")
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    dll = DoubleLinkedList()
    while True:
        print("Select any number from below:\n1.Create a Head node\n2.Appending a node at the end of list\n3.Insert an element at specific location\n4.Delete Head Element\n5.Delete an element by providing key value\n6.Deleting the last elemetn present in the list\n7.Display the elements present in the list")
        digit = int(input("Press the number: "))
        if digit == 1:
            dll.create_root_element(int(input("Enter the data to make it as a head element in the list")))
        elif digit == 2:
            dll.create_last_element(int(input("Enter the data to make it as a last element in the list")))
        elif digit == 3:
            prv_data = int(input("Enter the already existing element value so that new ele will be placed after this"))
            new_data = int(input("Enter the new data value to add into the list"))
            dll.create_middle_element(prv_data, new_data)
        elif digit == 4:
            dll.delete_first_element()
        elif digit == 5:
            element = int(input("Enter the element you want to delete from the list: "))
            dll.delete_middle_element(element)
        elif digit == 6:
            dll.delete_last_element()
        elif digit == 7:
            dll.print_all_elements()
        else:
            break

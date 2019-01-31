class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list_values(self):
        temp = self.head
        print("The elements present in the list are:")
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node_data, new_data):

        temp_node = self.head
        while temp_node.next:
            if temp_node.data == prev_node_data:
                nnode = Node(new_data)
                nnode.next = temp_node.next
                temp_node.next = nnode
                break
            elif temp_node.next.next is None and temp_node.next.data == prev_node_data:
                self.append(new_data)
                break

            temp_node = temp_node.next
        else:
            print("No element found in the list with the value {} ".format(prev_node_data))

    def append(self, new_data):
        node1 = Node(new_data)
        if self.head is None:
            self.head = node1
            return
        else:
            temp1 = self.head
            while(temp1.next):
                temp1 = temp1.next
            temp1.next = node1

    def delete_using_key(self, key):
        if self.head.data == key:
            self.delete_head()

        else:
            temp_node = self.head
            while temp_node.next:
                if temp_node.next.data == key:
                    temp_node.next = temp_node.next.next
                    break
                elif temp_node.next.next is None:
                    self.delete_last_element()
                    break
                temp_node = temp_node.next
            else:
                print("Element not found in the list.")

    def delete_head(self):
        self.head = self.head.next
        print("Deleted the head element")

    def delete_last_element(self):
        temp_node = self.head
        while temp_node.next:
            if temp_node.next.next is None:
                temp_node.next = None
                print("Deleted the last element")
                break

            temp_node = temp_node.next


if __name__ == "__main__":
    llist = LinkedList()
    while True:
        print("Select any number from below:\n1.Create a Head node\n2.Appending a node at the end of list\n3.Insert an element at specific location\n4.Delete Head Element\n5.Delete an element by providing key value\n6.Deleting the last elemetn present in the list\n7.Display the elements present in the list")
        digit = int(input("Press the number: "))
        if digit == 1:
            llist.push(int(input("Enter the data to make it as a head element in the list")))
        elif digit == 2:
            llist.append(int(input("Enter the data to make it as a last element in the list")))
        elif digit == 3:
            prv_data = int(input("Enter the already existing element value so that new ele will be placed after this"))
            new_data = int(input("Enter the new data value to add into the list"))
            llist.insertAfter(prv_data, new_data)
        elif digit == 4:
            llist.delete_head()
        elif digit == 5:
            element = int(input("Enter the element you want to delete from the list: "))
            llist.delete_using_key(element)
        elif digit == 6:
            llist.delete_last_element()
        elif digit == 7:
            llist.print_list_values()
        else:
            break

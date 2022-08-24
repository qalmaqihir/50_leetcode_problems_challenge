class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " --> ")
            temp = temp.next
        print(linked_list+"None")

    def insertNode(self, value, pos):
        target = Node(value)
        if pos==0:
            target.next = self.head
            self.head=target
            return
        def get_prev(pos):
            temp=self.head
            count=1
            while(count<pos):
                temp=temp.next
                count+=1
            return temp

        prev=get_prev(pos)
        nextNode=prev.next

        prev.next = target
        target.next=nextNode

    def remove(self,value):
        temp=self.head
        if temp is None:
            return
        if(temp.data==value):
            self.head=temp.next
            temp=None
            return
        while(temp.next.data!=value):
            temp=temp.next
        target=temp.next
        temp.next=target.next
        target.next=None



# Node strucutre: 5 => 1 => 3 => 7


linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.printList()

linked_list.insertNode(-2,4)
linked_list.printList()

linked_list.remove(-2)
linked_list.printList()














# class Node:
#     def __int__(self,data):
#         self.data=data
#         self.next = None
#
#
#
# class LinkedList:
#     def __int__(self):
#         self.head=None
#
#     def print_list(self):
#         temp= self.head
#         linked_lis=""
#         while(temp):
#             linked_lis+=(str(temp.data)+" ")
#             temp=temp.next
#         print(linked_lis)
#
#
# linked_list = LinkedList()
#
# linked_list.head=Node()
# node1=Node()
# node2=Node()
# node3=Node()
# node4=Node()
#
# linked_list.head.next=node1
# node1.next=node2
# node2.next=node3
# node3.next=node4
#
# linked_list.print_list()
#
#
#
#
#
#
#

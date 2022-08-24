class Node:
    def __int__(self, data):
        self.data=data
        self.next=None
        self.prev=None


class DoubleLinkedList:
    def __int__(self):
        self.head=None


    def create_list(self, arr):
        start=self.head
        n=len(arr)
        temp=start
        i=0
        while(i<n):
            newNode=Node(arr[i])
            if(i==0):
                start=newNode
                temp=start
            else:
                temp.next=newNode
                newNode.prev=temp
                temp=temp.next
            i+=1
            self.head=start

    def print_list(self):
        temp=self.head
        linked_list=" "
        while(temp):
            linked_list+=(str(temp.data)+ " --> ")
            temp=temp.next

        print(linked_list)



arr = [1,2,3,4,5]

llist = DoubleLinkedList()
#llist.print_list()
llist.create_list(arr)
#
# llist.print_list()
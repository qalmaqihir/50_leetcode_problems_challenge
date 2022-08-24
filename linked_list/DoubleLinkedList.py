class Node:
    def __int__(self, data):
        self.data=data
        self.next=None
        self.prev=None


class DoubleLinkedList:
    def __int__(self):
        self.head = None

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
        linked_list=""
        while(temp):
            linked_list+=(str(temp.data)+ " --> ")
            temp=temp.next

        print(linked_list)

    def count_list(self):
        temp=self.head
        count=0
        while(temp is not None):
            count+=1
        return count

    def insert_at_location(self,value, index):
        temp=self.head
        count=self.count_list()

        if count+1<index:
            return temp

        newNode=Node(value)

        if index==1:
            newNode.next=temp
            temp.pre=newNode
            self.head=newNode
            return self.head
        if index==count+1:
            while(temp.next is not None):
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp
            return self.head

        i=0
        while(i<index-1):
            temp=temp.next
            i+=1
        node_at_target=temp.next

        newNode.next=node_at_target
        node_at_target.prev=newNode
        newNode=temp
        return self.head

    def delete_at_location(self,index):
        temp=self.head

        count=self.count_list()
        if count<index:
            return temp

        if index==1:
            temp=temp.next
            self.head=temp
            return self.head
        if count==index:
            while(temp.next is not None and temp.next.next is not None):
                temp=temp.next
            temp.next=None
            return self.head
        i=1
        while i< index-1:
            temp=temp.next
            i+=1
        preNode=temp
        node_at_target=temp.next
        nextNode=node_at_target.next

        nextNode.prev=preNode
        preNode.next=nextNode
        return self.head






arr = [1,2,3,4,5]

llist = DoubleLinkedList()
#llist.print_list()
llist.create_list(arr)
#
# llist.print_list()
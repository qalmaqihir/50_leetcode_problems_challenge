class Queue:
    def __int__(self):
        self.q=[]

    def enqueue(self,x):
        self.q.append(x)

    def dequeue(self):
        if self.get_len()>0:
            self.q.pop(0)


    def get_top(self):
        if self.get_len()>0:
            return self.q[0]
        return None

    def get_len(self):
        return len(self.q)
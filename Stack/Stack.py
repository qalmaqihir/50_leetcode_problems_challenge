class Stack():
    def __int__(self):
        self.st=[]

    def push(self,x):
        self.st.append(x)

    def pop(self):
        if self.get_len()>0:
            self.st.pop()

    def get_top(self):
        if self.get_len()>0:
            return self.st[-1]
        return None

    def get_len(self):
        return len(self.st)


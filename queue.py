class Queue:
    def __init__(self):
        self.queue = []


    def add(self, el: any):
        self.queue.append(el)

        
    def get_idx(self, idx: int):
        return self.queue[idx]
    
        
    @property
    def get(self):
        return self.queue[0]
    
    
    @property
    def pop(self):
        self.queue.pop(0)
class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
      
    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])
      
    @classmethod
    def from_array(cls, arr):
        #I try to avoid recursive
        if not arr: 
            return None
        
        head = None
        for ele in arr[::-1]:
            head = Cons(ele,head)
        
        return head

    def filter(self, fn):
        #TODO: construct new algebraic list containing only elements
        #      that satisfy the predicate.
        if fn(self.head):
            return Cons(self.head, self.tail and self.tail.filter(fn))
        else:
            return self.tail and self.tail.filter(fn)
    
    def map(self, fn):
        #TODO: construct a new algebraic list containing all elements
        #      resulting from applying the mapper function to a list.
        return Cons(fn(self.head), self.tail and self.tail.map(fn))
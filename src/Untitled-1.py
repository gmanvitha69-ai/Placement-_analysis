def swapPairWise (self):
    dummy = Node(-1)
    dummy.next = self.head
    prev = dummy
    while prev,next != None and prev.next.next != None
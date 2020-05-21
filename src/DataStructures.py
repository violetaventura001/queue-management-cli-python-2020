class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):#Enqueue: Adds an item to the queue
        new_queue = self.get_queue()
        new_queue.append(item)
        self._queue = new_queue
    def dequeue(self):#dequeue: removes an item from the queue
        removed_queue = self.get_queue()
        if self._mode == "LIFO":
            item = removed_queue.pop()
        else:
            item = removed_queue.pop(0)   
        self._queue = removed_queue
        return item
    def get_queue(self):#getting the phone number from the array
        return self._queue
    def size(self):
        return len(self.get_queue())
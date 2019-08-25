#!/usr/bin/env python3

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.

        """
        self.size = size
        self._data = [None]*size
        self._size = 0
        self._front = 0
        self.sum = 0
        
    
    def dequeue(self):
    	self.sum -= self._data[self._front]
    	self._data[self._front] = None #check if it can be an empty string in the test cases, if yes then include condition of being empty
    	self._front = (self._front + 1) % len(self._data)
    	self._size -= 1


    def enqueue(self,val):
    	if self._size < self.size:
    		self._data[(self._size)] = val
    		self._size += 1
    		self.sum += val
    	else:

    		self.dequeue()
    		avail = (self._front + self._size) % len(self._data)
    		self._data[avail] = val
    		self._size += 1
    		self.sum += val

    def next(self, val):
    	self.enqueue(val)
    	return ((self.sum)/self._size)

    	
        


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
obj.next(1)
obj.next(10)
obj.next(3)
obj.next(5)

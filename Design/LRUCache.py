class DoublyLinkedList():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head, self.tail = DoublyLinkedList(), DoublyLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        
    def add_node(self,node):
        #always adding new node at the head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def remove_node(self,node):
        #removing the node
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def move_to_head(self,node):
        self.remove_node(node)
        self.add_node(node)
        

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self.move_to_head(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = DoublyLinkedList()
            new_node.key = key
            new_node.value = value
            self.cache[key] = new_node
            self.add_node(new_node)
            self.size += 1
            if self.size > self.capacity:
                res = self.tail.prev
                self.remove_node(res)
                self.size -=1
                del self.cache[res.key]
        else:
            node.value = value
            self.move_to_head(node)
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
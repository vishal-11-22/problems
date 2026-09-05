class Node:
    def __init__(self,data,key):
        self.prev=None
        self.next=None
        self.data=data
        self.key=key

class Dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_beg(self,node):
        if self.head is None:
            self.head=node
            self.tail=node
            return
        node.next=self.head
        self.head.prev=node
        self.head=node
        return
    def insert_end(self,node):
        if self.head is None and self.tail is None:
            self.insert_beg(node)
            return
        self.tail.next=node
        node.prev=self.tail
        self.tail=node
    def move_node_to_front(self,node):
        if self.head==node:
            return
        if node.next is not None:
            node.prev.next=node.next
            node.next.prev=node.prev
        else:
            self.tail=node.prev
            node.prev.next=None
        node.prev=None
        node.next=None
        self.insert_beg(node)


    def delete_end(self):
        
        if self.head==self.tail:
            n=self.head
            self.head=self.tail=None
            return  n
        n=self.tail
        self.tail=self.tail.prev
        self.tail.next=None
        return n
            

    # def move_node_to_back(node):
    #     if self.tail==node:
    #         return
    #     if self.head==node:
    #         self.head=self.head.next
    #         self.insert_end(node)
    #         return
    #     node.prev.next=node.next
    #     node.next.prev=node.prev
    #     self.insert_end(node)
    
    

class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity=capacity
        self.hashmap=dict()
        self.seq=Dll()

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node_address=self.hashmap[key]
        data=node_address.data
        self.seq.move_node_to_front(node_address)
        return data
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node=self.hashmap[key]
            node.data=value
            self.seq.move_node_to_front(node)
            return
        if self.max_capacity>len(self.hashmap):
            n=Node(value,key)
            self.seq.insert_beg(n)
            self.hashmap[key]=n
            return

        last_node=self.seq.delete_end()
        if last_node:
            self.hashmap.pop(last_node.key)
        
        n=Node(value,key)
        self.seq.insert_beg(n)
        self.hashmap[key]=n

        
        
            
            
                
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
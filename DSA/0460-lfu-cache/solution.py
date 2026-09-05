from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add_first(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)

        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0

        self.keyMap = {}
        self.freqMap = defaultdict(DLL)

    def update(self, node):
        freq = node.freq

        self.freqMap[freq].remove(node)

        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1

        self.freqMap[node.freq].add_first(node)

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1

        node = self.keyMap[key]
        self.update(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            self.update(node)
            return

        if len(self.keyMap) == self.capacity:
            node = self.freqMap[self.minFreq].remove_last()
            del self.keyMap[node.key]

        node = Node(key, value)

        self.keyMap[key] = node
        self.freqMap[1].add_first(node)

        self.minFreq = 1





















# class Node:
#     def __init__(self,key,value):
#         self.prev=None
#         self.next=None
#         self.key=key
#         self.value=value
#         self.freq=1

# class Doublyll:
#     def __init__(self):
#         self.head=None
#         self.tail=None

#     def insert_correct_pos(self,node):
#         if self.head==None and self.tail==None:
#             self.head=node
#             self.tail=node
#             return
#         if node.next is None and node.prev is None:
#             self.tail.next=node
#             node.prev=self.tail
#             self.tail=node
#             return
#         if node==self.head:
#             return
#         itr=node.prev
#         if node.next is not None:
#             node.next.prev = node.prev
#         else:
#             self.tail = node.prev

#         if node.prev is not None:
#             node.prev.next = node.next
        
#         node.next=node.prev=None
#         while itr.prev is not None and itr.freq<=node.freq:
#             itr=itr.prev
#         if itr.prev==None:
#             self.head,itr.prev,node.next=node,node,itr
#             node.prev = None
#             return
#         itr.next,node.next,itr.next.prev,node.prev=node,itr.next,node,itr


#     def delete_end(self):
#         if self.head==self.tail:
#             n=self.head
#             self.head=None
#             self.tail=None
#             return n
#         n=self.tail
#         self.tail=self.tail.prev
#         self.tail.next=None
#         return n

    

# class LFUCache:

#     def __init__(self, capacity: int):
#         self.max_capacity=capacity
#         self.hashmap=dict()
#         self.seq=Doublyll()
        

#     def get(self, key: int) -> int:
#         if key in self.hashmap:
#             node_add=self.hashmap[key]
#             node_add.freq+=1
#             data=node_add.value
#             self.seq.insert_correct_pos(node_add)
#             return data
#         return -1
        

#     def put(self, key: int, value: int) -> None:
#         n=Node(key,value)
#         if self.max_capacity>len(self.hashmap) and key not in self.hashmap:
#             self.hashmap[key]=n
#             self.seq.insert_correct_pos(n)
#             return
#         if key in self.hashmap:
#             node_add=self.hashmap[key]
#             node_add.freq+=1
#             node_add.value=value
#             self.seq.insert_correct_pos(node_add)
#             return
#         if self.max_capacity<=len(self.hashmap):
#             node=self.seq.delete_end()
#             self.hashmap.pop(node.key)
#             self.seq.insert_correct_pos(n)
#             self.hashmap[key]=n
#             return
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
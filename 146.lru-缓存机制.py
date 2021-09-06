#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
class node():
    def __init__(self, value, next, pre):
        self.value = value
        self.next = next
        self.pre = pre

class LRUCache():
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def move_to_end(self, node):
        self.del_node(node)
        self.add_node_to_end(node)

    def add_node_to_end(self,node):
        if not self.head:
            self.head = self.tail = node
            self.cache[node.value[0]] = self.head
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node

            self.cache[node.value[0]] = self.tail

    def del_node(self, node):
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre

        if node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            self.tail = node.pre

        self.cache.pop(node.value[0])

        node.pre = node.next = None


    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_to_end(self.cache[key])
            return self.tail.value[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.move_to_end(self.cache[key])
            self.tail.value[1] = value
        else:                
            self.add_node_to_end(node([key,value], None, None))

            if len(self.cache) > self.capacity:
                self.del_node(self.head)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

sol = LRUCache(1)
sol.put(2,1)
sol.get(2)

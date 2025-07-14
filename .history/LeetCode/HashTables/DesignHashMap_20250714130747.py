class ListNode:
    def __init__(self,key=-1,value=-1,next=None):
        self.key=key
        self.value=value
        self.next=next


class MyHashMap:
    def __init__(self):
        self.map=[ListNode() for i in range(1000)]


    def hash(self,key):
        return key%len(self.map)
        

    def put(self, key: int, value: int) -> None:
        cur=self.map[self.hash(key)]
        while cur.next:
            if cur.next.key==key:
                cur.next.value=value
                return
            cur=cur.next
        cur.next=ListNode(key,value)
        

    def get(self, key: int) -> int:
        cur=self.map[self.hash(key)].next
        while cur:
            if cur.key==key:
                return cur.value   
            cur=cur.next
        return -1

    def remove(self, key: int) -> None:
        cur=self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key==key:
                cur.next=cur.next.next
            cur=cur.next
            
#This code implements a simple hash map using separate chaining for collision resolution.
#It uses a linked list to store key-value pairs at each index of the hash table.
class Node:
    
    def __init__(self, value) -> None:
        self.data = value
        self.next = None  


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.n = 0
    
    def __len__(self):
        return self.n  
    
    
    def  insert_head(self, value):
        
        #create new node
        new_node= Node(value)
        
        # create connection
        new_node.next = self.head
        
        # reassign the head
        
        self.head = new_node
        
        self.n +=1
    
    def __str__(self):
        curr = self.head
        result = ''
        
        while curr !=None:
            # print(curr.data)
            result += str(curr.data) + '->'
            curr = curr.next
            
        return result[:-2]   
    
    def append(self, value):
        new_node = Node(value)
        if self.head ==None:
            self.head = new_node
            self.n += 1
            return
             
        curr =self.head
        
        
        while curr.next != None:
            curr = curr.next
            
        # reached to the last node
        
        curr.next = new_node
        self.n +=1
             
    def insert_after(self, after, value):
        curr = self.head
        
        new_node = Node(value)
        
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        
        # logic if item mil gya then curr not equal to none      
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n+=1
        else:
            return "item not found"     
        
        # Item nhi mila 
        
    def clear(self):
        self.head= None
        self.n = 0
        
    def delete_head(self):
        if self.head == None:
            return "Empty LL"
        
        self.head = self.head.next
        self.n-=1   
        
    def pop(self):
        if self.head==None:
            return "Empty LL"
        
        curr = self.head
        
        # curr == None None, checking with None node
        # curr.next == None, checking with last node
        # curr.next.next==None, checking with second last node   
        
        # kya hoga if linked list me 1 hi item hai ?
        if self.head.next== None:
            # linked list me 1 hi itme hai delete from head
            return self.delete_head()
        
        
        while curr.next.next !=None:
            
            curr = curr.next
            
        # the current is second last element 
        curr.next = None
        self.n-=1
        
    def remove(self, value):
        if self.head== None:
            return "Empty LL"
        
        if self.head.data==value:
            return self.delete_head()
        curr = self.head
        
        while curr.next!=None:
            if curr.next.data==value:
                break
            curr = curr.next
            
        #  2 cases milege 
        if curr.next==None:
            return "item not exist"
        else:
            curr.next = curr.next.next
            
    def serach(self, value):
        curr= self.head
        pos = 0
        
        while curr !=None:
            if curr.data == value:
               return pos
            curr = curr.next
            pos +=1
            
        return "Item not found "
    
    # get item with help of index
    def __getItem__(self, index):
        curr = self.head
        pos = 0
        
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
            
        return "IndexError"  
    
    def replace_max(self, value):
        temp = self.head
        max = temp
        
        while temp !=None:
            if temp.data > max.data:
                max = temp
            temp = temp.next
            
        max.data = value
        
    
    def add_odd_node(self):
        curr = self.head
        
        result = 0
        position = 0
        
        while curr != None:
            if position %2 !=0:
                result += curr.data
                
            position +=1
            curr = curr.next
        
        return result    
    
    def reverse(self):
        prev_node = None
        curr_node = self.head
        
        while curr_node !=None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            
        self.head = prev_node
    
                    
L= LinkedList()
(L.insert_head(1))
(L.insert_head(2))
(L.insert_head(3))
(L.insert_head(4))

print(L)
#L.append(5)
#(L.insert_after(1, 500))
#L.clear()
#L.delete_head()
#L.pop()
#L.remove(2)
#print(L.serach(1))
# print(L.__getItem__(0))
# L.replace_max(2343)
#print(L.add_odd_node())
# L.reverse()
L.sql_command()
print(L)       
# print(len(L))    
    
# for read only we need to use Array 
# for write opration we need to use Linked list      
    

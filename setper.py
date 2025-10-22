class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def  __str__(self):
        if self.is_empty():
            return 'Empty list'
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current =current.next
        return '->'.join(elements) + '-> None'
        
    def is_empty(self):
        return self.head is None
    
    def get_size(self):
        return self.size
    
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current=current.next
            current.next = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return 'This list if already empty!'
        removed_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return removed_data
    
    def search_element(self, value):
        count = 0
        current = self.head
        if self.is_empty():
            return 'This lis is aredly empty'
        
        else:
            while current:
                if current.data == value:
                    count +=1
                    print(f'count {count}: numb {value}')
                current = current.next

    def search_max_element(self):
        if self.is_empty():
            return 'This list if already empty!'
        current = self.head
        max_value = current.data
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value
        

first_list = LinkedList()

first_list.add_first(2 and 4 and 5)
first_list.add_first(5)
first_list.add_first(4 and 5)
first_list.add_first(1)
first_list.search_element(5)
first_list.search_max_element()
print(first_list.search_element(5))
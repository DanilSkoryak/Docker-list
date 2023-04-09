class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght = 0
    
    class Node:
        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node


    def push(self, element):
        self.head = self.Node(element, self.head)


    def pop(self):
        if self.head is None:
            return None
        element = self.head.element
        self.head = self.head.next_node
        return element
        


    def __str__(self):
        s = '['
        node = self.head
        while node.next_node:
            s += str(node.element) + ', '
            node = node.next_node
        s += str(node.element) + ']'
    

    @staticmethod
    def get_id(element):
        if element is None:
            return None
        return str(id(element))[8:]
    

    def get_info(self):
        i = 0
        node = self.head
        while node.next_node:
            print(f'{i}. {self.get_id(node)}\tvalue: {node.element}\n\tnext_node: {self.get_id(node.next_node)}')
            node = node.next_node
            i += 1
        print(f'{i}. {self.get_id(node)}\tvalue: {node.element}\n\tnext_node: {self.get_id(node.next_node)}')
    

class Word:
    def __init__(self, word):
        self.word = word
        self.linked_list = LinkedList()
        for char in self.word:
            self.linked_list.push(char)
            
    def reverse(self):
        reverse_word = ''
        curr = self.linked_list.head
        while curr is not None:
            reverse_word += curr.element
            curr = curr.next_node
        return reverse_word



lst = LinkedList()
lst.push(3)
lst.push(-1)
lst.push(7)
lst.push(10)

res = lst.pop()
lst.get_info()
print(res)

my_word = Word('Text')
print(my_word.reverse())

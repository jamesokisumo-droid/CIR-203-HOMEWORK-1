class Node:
    def __init__(self, data):
        self.data = data    
        self.next = None     

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


students = LinkedList()
students.add({
    "name": "Edwin",
    "admission_no": "CIT/001/024",
    "grades": {
        "CIT 115": "A",
        "CIR 203": "B+",
        "CIR 205": "A-"
    }
})

students.add({
    "name": "Sephania",
    "admission_no": "CIT/002/024",
    "grades": {
        "CIT 115": "B",
        "CIR 203": "A",
        "CIR 205": "B+"
    }
})

students.add({
    "name": "James",
    "admission_no": "CIT/00034/024",
    "grades": {
        "CIT 115": "A-",
        "CIR 203": "A",
        "CIR 205": "A"
    }
})
students.display()

{'name': 'Edwin', 'admission_no': 'CIT/001/024',
 'grades': {'CIT 115': 'A', 'CIR 203': 'B+', 'CIR 205': 'A-'}}

{'name': 'Sephania', 'admission_no': 'CIT/002/024',
 'grades': {'CIT 115': 'B', 'CIR 203': 'A', 'CIR 205': 'B+'}}

{'name': 'James', 'admission_no': 'CIT/00034/024',
 'grades': {'CIT 115': 'A-', 'CIR 203': 'A', 'CIR 205': 'A'}}



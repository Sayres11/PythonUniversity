class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        new_element = Element(data)
        if self.head is None:
            self.head = new_element
            self.tail = new_element
        else:
            current = self.head
            previous = None
            while current is not None and current.data <= data:
                previous = current
                current = current.nextE
            if previous is None:
                self.head = new_element
            else:
                previous.nextE = new_element
            new_element.nextE = current
            if current is None:
                self.tail = new_element
        self.size += 1

    def get(self, e):
        current = self.head
        while current is not None:
            if current.data == e:
                return current.data
            current = current.nextE
        return None

    def delete(self, e):
        current = self.head
        previous = None
        while current is not None:
            if current.data == e:
                if previous is None:
                    self.head = current.nextE
                else:
                    previous.nextE = current.nextE
                if current.nextE is None:
                    self.tail = previous
                self.size -= 1
                return
            previous = current
            current = current.nextE

    def append(self, e, func=None):
        new_element = Element(e)
        if self.head is None:
            self.head = new_element
            self.tail = new_element
        else:
            current = self.head
            previous = None
            while current is not None and (func(current.data, e) if func is not None else current.data >= e):
                previous = current
                current = current.nextE
            if previous is None:
                self.head = new_element
            else:
                previous.nextE = new_element
            new_element.nextE = current
            if current is None:
                self.tail = new_element
        self.size += 1

    def __str__(self):
        current = self.head
        output = ""
        while current is not None:
            output += str(current.data) + " "
            current = current.nextE
        return output.strip()

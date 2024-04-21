"""
stack and singly linked list implementation used for palindrome evaluation
"""


class Stack:
    def __init__(self, full):
        self.stack = []
        self.full = full

    def is_empty(self):
        if len(self.stack) == 0:
            return True

    def is_full(self):
        if len(self.stack) == self.full:
            return True

    def push(self, a):
        if not self.is_full():
            self.stack += [a]

    def pop(self):
        if not self.is_empty():
            e = self.stack[-1]
            del self.stack[-1]
        return e

    def top_value(self):
        return self.stack[-1]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_expression(self, expression):
        for char in expression:
            node = Node(char)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end='')
            current = current.next
        print()


class CheckForPalindromes:
    def __init__(self, palindrome):
        self.palindrome = palindrome

    def check_for_palindrome(self):
        sll_palindrome = SinglyLinkedList()
        sll_palindrome.insert_expression(self.palindrome)
        in_stack = Stack(len(self.palindrome))

        print("Is", self.palindrome, "a palindrome?")
        
        current_element = sll_palindrome.head
        while current_element:
            in_stack.push(current_element.data)
            current_element = current_element.next

        current_element = sll_palindrome.head
        while current_element:
            if current_element.data == in_stack.top_value():
                in_stack.pop()
            else:
                pass
            current_element = current_element.next

        if in_stack.is_empty():
            print("It's a palindrome!")
        else:
            print("It's not a palindrome...")


palindrome1 = CheckForPalindromes("3120213")
palindrome1.check_for_palindrome()

palindrome2 = CheckForPalindromes("12203022")
palindrome2.check_for_palindrome()

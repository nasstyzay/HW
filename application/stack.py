class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

def is_balanced(s):
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    open_par = set(bracket_map.keys())
    stack = Stack()

    for char in s:
        if char in open_par:
            stack.push(char)
        elif char in bracket_map.values():
            if stack.is_empty() or bracket_map[stack.pop()] != char:
                return "Несбалансированно"
    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


if __name__ == "__main__":
    test_strings = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "}{",
        "{{[(])]}}",
        "[[{())}]"
    ]

    for test in test_strings:
        result = is_balanced(test)
        print(f"{test}: {result}")

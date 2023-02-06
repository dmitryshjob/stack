
class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self): # проверка стека на пустоту. Метод возвращает True или False
        if len(self.values) == 0:
            return True
        else:
            return False    

    def push(self, item): # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.values.append(item)

    def pop(self): # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        return self.values.pop()

    def peek(self): # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        return self.values[-1]

    def size(self): # возвращает количество элементов в стеке.
        return len(self.values)


def balance(string):
    open = ['(', '{', '[']
    closed = [')', '}', ']']
    stack = Stack()

    if len(string) % 2 > 0:
        return 'Несбалансированно'

    for ind, el in enumerate(string):
        if el in open:
            stack.push(el)
        elif el in closed:
            if stack.is_empty():
                return 'Несбалансированно'
            elif open.index(stack.peek()) != closed.index(el):
                return 'Несбалансированно'
            else:
                stack.pop()
                if stack.is_empty() and ind == len(string)-1:
                    return 'Сбалансированно'



stack_1 = '(((([{}]))))'
stack_2 = '[([])((([[[]]])))]{()}'
stack_3 = '{{[()]}}'
stack_4 = '}{}'
stack_5 = '{{[(])]}}'
stack_6 = '[[{())}]'

if __name__ == '__main__':
    print(balance(stack_1))
    print(balance(stack_2))
    print(balance(stack_3))
    print(balance(stack_4))
    print(balance(stack_5))
    print(balance(stack_6))
    

class Stack:

    def __init__(self, initial=[]):
        # private field
        self.__items = initial

    def isEmpty(self):
        #return len(self.__items) == 0
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items)-1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        output = "\n".join([str(item) for item in self.__items[::-1]])
        return output

    def __add__(self, other):
        new_initial = self.__items + other.__items
        temp = Stack(new_initial)
        return temp

    #private method
    def __erase(self):
        self.__items = []



#this works only when stack.py will be run as script file
if __name__ == '__main__':
    stacky = Stack([123,"hyi",True])
    print stacky

    add_stacky = Stack([1,2,3]) + Stack([True, False])
    print add_stacky
import copy

class Queue:
    def __init__(self, initial = []):
        self.__items = initial

    def get_items(self):
        return copy.deepcopy(self.__items)

    def isEmpty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

if __name__ == '__main__':
    q = Queue([1, 2, 3])
    print q.get_items()





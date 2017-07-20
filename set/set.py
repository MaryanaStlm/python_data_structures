import copy

class Set:
    def __init__(self, initial = []):
       unique_list = []
       for i in initial:
           if i not in unique_list:
               unique_list.append(i)
       self.__items = unique_list

    def get_items(self):
        return copy.deepcopy(self.__items)

    #union
    def __add__(self, other):
        new_initial = self.__items + other.__items
        return Set(new_initial)

    def intersection(self, other):
        intersection_list = []
        for i in self.__items:
            if i in other.__items:
                intersection_list.append(i)
        res = Set(intersection_list)
        return res

    #difference
    #does not working
    '''def __sub__(self, other):
        new_initial = self.__items - other.__items
        return Set(new_initial)'''

    def difference(self, other):
        difference_list = []
        for i in self.__items:
            if i not in other.__items:
                difference_list.append(i)
        return Set(difference_list)

    def is_subset(self, other):
        subset = True
        for i in self.__items:
            if i not in other.__items:
                subset = False
        return subset

#if __name__ == '__main__':



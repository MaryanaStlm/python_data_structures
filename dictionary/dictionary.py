class Dictionary(object):

    def __init__(self, list_of_tuples=[]):
        self.dict = []

        unique_list = []
        key_list = []

        for tpl in list_of_tuples:
            if len(tpl) != 2:
                raise Exception('Dictionary element has only key and value')
            key, val = tpl
            if key not in key_list:
                self.dict.append((key, val))
                key_list.append(key)

    def items(self):
        return self.dict

    def keys(self):
        keys = []
        for key, val in self.dict:
            keys.append(key)
        return keys

    def values(self):
        values = []
        for key, val in self.dict:
            values.append(val)
        return values

    def update(self, key_to_append, value_to_append):
        if key_to_append in self.keys():
            raise Exseption('this key is already in dict')
        else:
            self.dict.append((key_to_append, value_to_append))

    def get(self, key_to_find):
        for key, val in self.dict:
            if key_to_find == key:
                return val

    def setdefault(self, key_to_find, default = None):
        for key, val in self.dict:
            if key_to_find == key:
                return val
        else:
            self.update(key_to_find, default)

    def pop(self, key_to_del):
        for tpl in self.dict:
            key, val = tpl
            if key_to_del == key:
                self.dict.remove(tpl)
                return val

    def __getitem__(self, key_to_find):
        for key, val in self.dict:
            if key_to_find == key:
                return val
        raise Exception('No value with this key')

    def __setitem__(self, key_to_find, value_to_find):
        if key_to_find not in self.keys():
            self.dict.append((key_to_find, value_to_find))
        else:
            for key, val in self.dict:
                if key_to_find == key:
                    self.dict.remove((key, val))
                    self.dict.append((key_to_find, value_to_find))



class Dictionary(object):
    # TODO: ensure that keys in self.dict are unique

    def __init__(self, list_of_tuples=[]):
        self.dict = []

        if len(list_of_tuples) > 0:

            for tpl in list_of_tuples:
                if len(tpl) != 2:
                    raise Exception('wrong length of tuple in list')

                key, val = tpl


                if key is not None and val is not None:
                    self.dict.append((key, val))
                else:
                    raise Exception('you have to pass list of two element tuples')

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

    def update(self, key, value):
        self.dict.append((key, value))

    def get(self, key_to_find):
        for key, val in self.dict:
            if key_to_find == key:
                return val

    def setdefault(self, key_to_find):
        for key, val in self.dict:
            if key_to_find == key:
                return val
        else:
            val = None
            self.update(key_to_find, val)

    def pop(self, key_to_del):
        for tpl in self.dict:
            key, val = tpl
            if key_to_del == key:
                self.dict.remove(tpl)
                return val



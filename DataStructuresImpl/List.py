class MyList (list):
    def __getitem__(self, key):
        if key >= len(self):
            return -1
        return super(MyList, self).__getitem__(key)
    def __setitem__(self, key, value):
        if key >= len(self):
            self.append(value)
        else:
            super(MyList,self).__setitem__(key, value)

a = MyList([1, 2, 3])
print(a[5])

class TypedList(list):
    def __init__(self, iterable = None, data_type = None):
        super().__init__(iterable)
        self.data_type = data_type
        if self.data_type is None and iterable:
            self.data_type = type(iterable[0])
        for value in iterable:
            if not isinstance(value, self.data_type):
                raise ValueError("Only one type nedeed")

    def append (self, val):
        if not isinstance(val,self.data_type):
            raise ValueError("Only one type nedeed")
        super(TypedList,self).append(val)

a = TypedList(["a"])
print(a)
a.append("b")
print(a)
a.append(1)



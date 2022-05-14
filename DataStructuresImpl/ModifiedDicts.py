class MyDict(dict):
    def __getitem__(self, item):
        if item in self:
            return super(MyDict, self).__getitem__(item)
        raise ValueError("There is no such key in this dict")

d = MyDict(({"a": 1,"b": 2}))
print(d['c'])

class IndexDict(dict):
    def __getitem__(self, item):
        if isinstance(item,int):
            return list(self.items())[item]
        else:
            return super().__getitem__(item)


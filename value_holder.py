class Value_Holder():
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)
    
    def __set__(self, instance, value):
        ### maybe something
        setattr(instance, self.private_name, value)
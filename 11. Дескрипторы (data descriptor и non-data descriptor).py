class Integer:
    def set_name(self, owner, name):
        self.name = '_' + name

    def get(self, instance, owner):
        return instance.dict[self.name]

    def set(self, instance, value):
        print(f'set: {self.name} = {value}')
        instance.dict[self.name] = value


class Point3d:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

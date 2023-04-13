class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    def __str__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val

class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.ar = [self.__cell() for _ in range(self.__max_length)]

    def __str__(self):
        return " ".join(map(str, self.ar))

    def __check_index(self, index):
        if type(index) != int or not 0 <= index < self.__max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __setitem__(self, index, val):
        self.__check_index(index)
        self.ar[index].value = val

    def __getitem__(self, index):
        self.__check_index(index)
        return self.ar[index].value
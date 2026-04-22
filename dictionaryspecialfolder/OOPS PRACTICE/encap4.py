class DataCleaner:
    def __init__(self, data):
        self.__data = data   # private

    def clean(self):
        self.__data = [x for x in self.__data if x >= 0]
        return self.__data

d = DataCleaner([10, -5, 20])
print(d.clean())
from NewModule.Cell import MyCell


class MyMap:
    def __init__(self, streets):
        self.map = []
        self.__cell_count = streets
        for i in range(self.__cell_count):
            self.map.append(MyCell(f'{i+1}', 60 + i*10, 5 + i*5))

    def print_cell(self, ind):
        self.map[ind].print_data()

    def get_size(self):
        return self.__cell_count

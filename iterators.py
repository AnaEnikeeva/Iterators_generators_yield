class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.index_list = 0
        self.index_element = 0
        return self

    def __next__(self):
        while self.index_list < len(self.list_of_list):
            if self.index_element < len(self.list_of_list[self.index_list]):
                item = self.list_of_list[self.index_list][self.index_element]
                self.index_element += 1
                return item
            if self.index_list == len(self.list_of_list):
                raise StopIteration
         




def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

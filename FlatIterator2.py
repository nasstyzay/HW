class FlatIterator:

    def __init__(self, list_of_list):
        self.stack = list(reversed(list_of_list))

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_item = self.stack.pop()
            if isinstance(current_item, list):
                self.stack.extend(reversed(current_item))
            else:
                return current_item
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    expected_result = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_2), expected_result):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == expected_result


if __name__ == '__main__':
    test_3()

import types

def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):
            for subitem in flat_generator(item):
                yield subitem
        else:
            yield item

def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

if __name__ == '__main__':
    test_4()

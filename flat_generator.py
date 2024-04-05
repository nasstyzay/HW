import types

def flat_generator(list_of_lists):
    for list_item in list_of_lists:
        if isinstance(list_item, list):
            for item in list_item:
                yield item
        else:
            yield list_item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


    generated_list = list(flat_generator(list_of_lists_1))


    for flat_iterator_item, check_item in zip(generated_list, ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item

    assert generated_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()



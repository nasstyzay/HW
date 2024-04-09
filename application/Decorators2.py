import types
from datetime import datetime


def logger(path):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            if isinstance(result, types.GeneratorType):
                return log_generator(result, path, old_function.__name__, *args, **kwargs)
            return result

        return new_function

    return decorator


def log_generator(generator, path, func_name, *args, **kwargs):
    with open(path, 'a') as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        arguments = ', '.join([str(a) for a in args] + [f"{k}={v}" for k, v in kwargs.items()])
        log_file.write(f"{timestamp} - Вызов функции: {func_name} с аргументами: {arguments}\n")

    for value in generator:
        with open(path, 'a') as log_file:
            log_file.write(f"{timestamp} - Yield: {value}\n")
        yield value



@logger('flat_generator.log')
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

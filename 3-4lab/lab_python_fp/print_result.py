def print_result(func):
    def wrapper(*args, **kwargs):
        nekto = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(nekto,list):
            for i in nekto:
                print(i)
        elif isinstance(nekto,dict):
            for k,v in nekto.items():
                print(f'{k}={v}')
        else:
            print(nekto)
        return nekto
    return wrapper



@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
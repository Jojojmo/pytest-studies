from pytest import mark

from codigo.codes import print_beauty, sum_arr, unique_arr, is_number_prime, is_right_triangle


def test_print_beauty_returns_none():
    string = 'Hello World!'        #Given - Dado
    result = print_beauty(string)  #When  - Quando
    assert result == None          #Then  - Então

@mark.arr
def test_sum_arr_big_nums_returns_list():
    assert sum_arr([10**12, 20**8, 40**27])


@mark.arr
def test_unique_arr_big_index_returns_list():
    assert unique_arr([10] * 1000 + [5] * 50 + [14] * 9821)


@mark.skip(reason='Esperando acesso ao banco de dados')
def test_unique_arr_user_returns_list():
    assert unique_arr([0])

@mark.prime_numbers
@mark.parametrize(
        'prime_number',
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
)
def test_is_number_prime_prime_battery_retuns_true(prime_number):
    assert is_number_prime(prime_number) == True


@mark.triangle
@mark.parametrize(
        'a,b,c',
        [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41)]
)
def test_is_right_triangle_battery_returns_true(a, b, c):
    assert is_right_triangle(a, b, c)



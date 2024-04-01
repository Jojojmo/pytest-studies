def print_beauty(string:str) -> None:
    print(f'‧͙⁺˚*･༓☾ {string} ☽༓･*˚⁺‧͙')

def sum_arr(arr:list) -> list:
    return [sum(arr)]

def unique_arr(arr:list) -> list:
    return list(set(arr))

def is_number_prime(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        # Verifica a divisibilidade apenas até a raiz quadrada do número
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

def is_right_triangle(a, b, c):
    # Verifica se os lados formam um triângulo
    if a + b > c and a + c > b and b + c > a:
        # Encontra o quadrado do lado mais longo (hipotenusa)
        hypotenuse_squared = max(a, b, c) ** 2
        # Soma dos quadrados dos outros dois lados
        sum_of_squares_of_legs = a**2 + b**2 + c**2 - hypotenuse_squared

        # Verifica se satisfaz o Teorema de Pitágoras
        if hypotenuse_squared == sum_of_squares_of_legs:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print_beauty('Hello World')
    my_sum = sum_arr([1,2,3,4,5])
    print(my_sum)
    print(unique_arr([1,2,2,4,3]))
    print(is_number_prime(1))
    print(is_right_triangle(3,4,5))
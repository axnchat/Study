# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 40

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 40
    if n <= 1:
        return n
    Fib = [0] * (n+1)
    Fib[1], Fib[2] = 1, 1
    for i in range(3, n+1):
        Fib[i] = Fib[i - 1] + Fib[i - 2]
    print(Fib)
    return Fib[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

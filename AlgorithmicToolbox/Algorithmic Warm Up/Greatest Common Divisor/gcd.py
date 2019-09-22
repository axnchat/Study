# python3


def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False


def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    if(a == b):
        return a
    if(a<b):
        rem= b%a
        #print("rem1:"+str(rem))
        if rem!=0:
            return gcd(a,rem)
        else: return a
    else:
        rem=a%b
        #print("rem2:" + str(rem))
        if rem!=0:
            return gcd(b,rem)
        else: return b





if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))

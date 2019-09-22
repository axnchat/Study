# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple

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


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    gcd_new=gcd(a,b)
    return int (a*b/gcd_new)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))

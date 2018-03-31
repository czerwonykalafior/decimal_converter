from the_stack import Stack

# https://codereview.stackexchange.com/questions/134154/decimal-to-binary-algorithm
# https://en.wikipedia.org/wiki/Decimal
# https://en.wikipedia.org/wiki/Binary_number
# http://www.samouczekprogramisty.pl/system-dwojkowy/


# n                                              = 11 in base-10 number system
#     8     +     0     +     2     +     1      = 11
#      2^3              +      2^1  +      2^0   = 11
# (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0)  = 11
# 1         0         1         1
# binary(n) = 1011 in base-2 numeral system      = 11 in base-10 number system
# bin(n)    = 0b1011


def dec_to_bin_while(n):
    remstack = Stack()

    while n > 0:
        rem = n % 2
        remstack.push(rem)
        n //= 2

    bin_str = ''

    while not remstack.is_empty():
        bin_str += str(remstack.pop())

    return bin_str


def dec_to_bin_mem(n):
    bits = list()

    bits.append(str(0 if n % 2 == 0 else 1))
    while n > 1:
        n //= 2
        bits.append(str(0 if n % 2 == 0 else 1))

    bits.reverse()
    return ''.join(bits)


def dec_to_bin_rec_list(n):
    return dec_to_bin_rec_list(n // 2) + [n % 2] if n > 1 else [n]


def dec_to_bin_rec(n):
    if n == 0:
        return ''
    else:
        return dec_to_bin_rec(n//2) + str(n % 2)

if __name__ == '__main__':

    decimal = 11

    print(dec_to_bin_while(decimal))
    print(dec_to_bin_mem(decimal))
    print(dec_to_bin_rec(decimal))

    bin_list = dec_to_bin_rec_list(decimal)

    # https://stackoverflow.com/questions/9060653/list-comprehension-without-in-python
    bin_list_str = ''.join(str(v) for v in bin_list)
    print(bin_list_str)

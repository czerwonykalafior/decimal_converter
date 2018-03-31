from the_stack import Stack

BASE = 4

# BASE = 4

# n = 25
# 1*4^2 + 2*4^1 + 1*4^0
# 1       2       1
# 121

# n = 35
# 2*4^2 + 0 * 4^1 + 3 * 4^0
# 2       0         3
# 203


def dec_convert_while(n, base):
    remstack = Stack()

    while n > 0:
        rem = n % base
        remstack.push(rem)
        n //= base

    bin_str = ''

    while not remstack.is_empty():
        bin_str += str(remstack.pop())

    return bin_str


def dec_convert_rec(n, base):
    if n == 0:
        return ''
    else:
        return dec_convert_rec(n//base, base) + str(n % base)

if __name__ == '__main__':

    print(dec_convert_while(35, BASE))
    print(dec_convert_rec(35, BASE))

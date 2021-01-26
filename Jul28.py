# Find a 5 digit number which has no zeroes and no digit is repeated:

# digit 1 is prime
# digit 2 is digit 5 minus digit 1
# digit 3 is digit 1 x 2
# digit 4 is digit 3 + 3
# digit 5 is digit 4 - digit 1

if __name__ == '__main__':
    for a in [1, 3, 5, 7]:  # has to be single digit prime, so can ONLY be 1,3,5,7
        c = a * 2
        d = c + 3
        e = d - a
        b = e - a
        s = {a, b, c, d, e}
        num = f'{a}{b}{c}{d}{e}'
        if len(s) == 5 and len(num) == 5:
            print(num)

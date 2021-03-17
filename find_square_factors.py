# Returns the factors of num as a list
def find_factors(num):
    factors = []

    for i in range(1, num + 1):

        if num % i == 0:
            factors.append(i)

    return factors

# If num is square, return True. Otherwise, return False
def is_square(num):
    if num < 1:
        return False
    else:
        for i in range(2, int(num / 2) + 1):
            if (i * i) == num:
                return True
        return False

# Finds and prints the square factors of a number
def main():
    square_factors = []

    num = int(input('num: '))
    factors = find_factors(num)

    for i in range(0, len(factors)):

        if is_square(factors[i]):
            square_factors.append(factors[i])

    print(square_factors)

main()

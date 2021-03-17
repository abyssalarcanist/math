# Returns the factors of num as a list
def find_factors(num):
    factors = []

    for i in range (1, num + 1):

        if num % i == 0:
            factors.append(i)

    return factors

# If num is prime, return True. Otherwise, return False
def is_prime(num):
    if num < 1:
        return False
    else:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        return True

# Finds and prints the prime factors of a number
def main():
    prime_factors = []

    num = int(input('num: '))
    factors = find_factors(num)
    for i in range(0, len(factors)):
        if is_prime(factors[i]):
            prime_factors.append(factors[i])

    print(prime_factors)

main()

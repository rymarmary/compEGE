A_NUM_COUNT = 6


def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def sum_of_prime_divisors(num):
    sum_of_prime_num = 0
    prime_num_count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                sum_of_prime_num += i
                prime_num_count += 1

    return sum_of_prime_num, prime_num_count


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def get_a_num(num):
    prime_numbers_res = sum_of_prime_divisors(num)
    if prime_numbers_res[1] != 0:
        return int_r(prime_numbers_res[0] / prime_numbers_res[1])
    else:
        return 0


def main():
    a_count = 0
    curr_num = 310001
    while a_count != A_NUM_COUNT:
        a_res = get_a_num(curr_num)
        if a_res != 0 and a_res % 6 == 0 and a_res % 10 != 4:
            print(curr_num, a_res)
            a_count += 1
        curr_num += 1


if __name__ == "__main__":
    main()






'''def summ_count(n):
    summ = 0
    k = 0
    d = 2
    while d <= n ** 0.5:
        if n % d == 0:
            summ += d
            k += 1
            while n % d == 0:
                n //= d
        d += 1
    if k != 0:
        return summ, k
    else:
        return 0

def a(n):
    numbers = summ_count(n)
    if numbers[1] != 0:
        return int_r(numbers[0] / numbers[1])
    else:
        return 0

def int_r(n):
    num = int(n + (0.5 if n > 0 else -0.5))
    return num

def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

k = 0
for i in range(310001, 10 ** 7):
    n = a(i)
    if n != 0 and n % 6 == 0 and n % 10 != 4:
        k += 1
        print(i, n)
        if k == 6:
            break'''
    

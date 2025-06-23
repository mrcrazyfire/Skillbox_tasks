class Primes:
    def __init__(self, last_number):
        self.current_number = 2
        self.last_number = last_number

    def __iter__(self):
        self.current_number = 2
        return self

    def __next__(self):
        while self.current_number <= self.last_number:
            number = self.current_number
            self.current_number += 1
            if self.is_prime(number):
                return number
        raise StopIteration

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


prime_nums = Primes(50)

for i_elem in prime_nums:

    print(i_elem, end=' ')
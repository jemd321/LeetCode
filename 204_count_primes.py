class CountPrimes:
    # Sieve of Eratosthenes
    def countPrimes(self, n):
        if not n or n == 1:
            return 0
        nums = [True] * (n)
        nums[0] = nums[1] = False
        for i in range(2, n- 1):
            if nums[i] is True:
                j = i**2
                k = 1
                while j < n:
                    nums[j] = False
                    j = i**2 + (k*i)
                    k += 1
        return nums.count(True)



class Test:
    test = CountPrimes()
    print(test.countPrimes(3))




class PascalTriangle:
    def generate(self, numsRows):
        triangle = [[1] for x in range(numsRows)]
        for i in range(1, numsRows):
            for k in range(1, i):
                triangle[i].append(triangle[i-1][k-1] + triangle[i-1][k])
            triangle[i].append(1)
        return triangle


class Test:
    test = PascalTriangle()
    for x in range(10):
        print(test.generate(x))


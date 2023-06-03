class Degree:
    def CountDegrees(self, number, max_degree):
        i = 0
        for _ in range(max_degree):
            yield number ** i
            i += 1
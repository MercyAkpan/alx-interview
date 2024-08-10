def pascal_triangle(n):
        if n == 0:
             return [[]]
        if n == 1:
            return [[1]]
        current = [1]
        history = pascal_triangle(n - 1)
        previous = history[-1]
        for i in range(n - 2):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        # print(history + [current])
        return (history + [current])
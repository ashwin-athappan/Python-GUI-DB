class TwoNumberSum:
    def method(self, a, targetSum):
        pairs = []
        for i in range(0, len(a)):
            for j in range(0, len(a)):
                if a[i] + a[j] is targetSum and i != j:
                    if (i, j) not in pairs and (j, i) not in pairs:
                        pairs.append((i, j))

        return pairs


TNS = TwoNumberSum()

arr = [3, 5, 4, 8, 11, 4, 1, 6, 9]
s = 8

print(TNS.method(arr, s))

test_cases = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    []
]

for case in test_cases:
    if not case:
        result = 0
    else:
        sum_even_index = sum(case[i] for i in range(0, len(case), 2))
        result = sum_even_index * case[-1]
    print(case, '=>', result)

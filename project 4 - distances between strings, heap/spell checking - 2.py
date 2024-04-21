import numpy as np

def levenstein_modified(a: str, b: str):
    first = [i for i in a]
    second = [i for i in b]
    levenstein_arr = np.zeros((len(first) + 1, len(second) + 1))
    for i in range(len(b) + 1):
        levenstein_arr[0][i] = i
    for i in range(len(a) + 1):
        levenstein_arr[i][0] = i
    misclicks = [("a", "s"), ("s", "a"), ("o", "p"), ("p", "o"), ("w", "e"), ("e", "w"), ("i", "u"), ("u", "i"),
                 ("r", "e"), ("e", "r"), ("z", "s"), ("s", "z"), ("c", "v"), ("v", "c"), ("d", "f"), ("f", "d")]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if first[i - 1] == second[j - 1]:
                levenstein_arr[i][j] = levenstein_arr[i - 1][j - 1]
            else:
                error_weight = 1
                if (first[i - 1], second[j - 1]) in misclicks:
                    error_weight = 0.5
                levenstein_arr[i][j] = min(levenstein_arr[i - 1][j], levenstein_arr[i][j - 1], levenstein_arr[i - 1][j - 1]) + error_weight
    levenstein_distance = levenstein_arr[len(a)][len(b)]
    print(f"levenstein distance between {a} and {b} is {levenstein_distance}")
    return levenstein_distance

levenstein_modified("mama", "mtma")
levenstein_modified("mama", "msma")
import numpy as np
def levenstein(a: str, b: str):
    first = [i for i in a]
    second = [i for i in b]
    levenstein_arr = np.zeros((len(first) + 1, len(second) + 1))
    for i in range(len(b) + 1):
        levenstein_arr[0][i] = i
    for i in range(len(a) + 1):
        levenstein_arr[i][0] = i
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if first[i - 1] == second[j - 1]:
                levenstein_arr[i][j] = levenstein_arr[i - 1][j - 1]
            else:
                levenstein_arr[i][j] = min(levenstein_arr[i - 1][j], levenstein_arr[i][j - 1], levenstein_arr[i - 1][j - 1]) + 1
    levenstein_distance = int(levenstein_arr[len(a)][len(b)])
    # print(levenstein_arr)
    return levenstein_distance

def hamming(a: str, b: str):
    if len(a) != len(b):
        print("strings must be the same length!")
        return
    hamming_distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            hamming_distance += 1
    return hamming_distance

def indel(a: str, b: str):
    first = [i for i in a]
    second = [i for i in b]
    indel_arr = np.zeros((len(first) + 1, len(second) + 1))
    for i in range(len(b) + 1):
        indel_arr[0][i] = i
    for i in range(len(a) + 1):
        indel_arr[i][0] = i
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if first[i - 1] == second[j - 1]:
                indel_arr[i][j] = indel_arr[i - 1][j - 1]
            else:
                indel_arr[i][j] = min(indel_arr[i - 1][j], indel_arr[i][j - 1]) + 1
    indel_distance = int(indel_arr[len(a)][len(b)])
    # print(indel_arr)
    return indel_distance

a = "gracze"
b = "bracia"
print(f"levenstein distance between {a} and {b} is {levenstein(a, b)}\n")
print(f"hamming distance between {a} and {b} is {hamming(a, b)}\n")
print(f"indel distance between {a} and {b} is {indel(a, b)}\n")

c = "mama"
d = "mama"
print(f"levenstein distance between {c} and {d} is {levenstein(c, d)}\n")
print(f"hamming distance between {c} and {d} is {hamming(c, d)}\n")
print(f"indel distance between {c} and {d} is {indel(c, d)}\n")

e = "siostra"
f = "brat"
print(f"hamming distance between {e} and {f} is {hamming(e, f)}")
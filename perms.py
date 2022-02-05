import numpy as np


def permutation(lst):

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is remaining list
        remLst = lst[:i] + lst[i+1:]

        # Generating all permutations where m is first element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program
end = 10

for i in range(2, end + 2):
    arr = []
    data = list(range(1, i))

    for p in permutation(data):
        arr.append(p)
    np.savetxt('perms_' + str(i - 1) + '.csv',
               np.asarray(arr), delimiter=',', fmt='%i')

import random


def a_get(a: list[[int,int,int]], b : int) -> bool:
    valid_mat = [[b for b in range(0,9)]]
    print(valid_mat)

    return False


def validint(a: any) -> bool:
    if type(a) is not int:
        return False
    else:
        return True


def main():
    n = int(input("Enter a number :"))
    import numpy as np
    import time
    new_mat = [[0 for _ in range(n)]]*n
    for _ in range(n):
        for __ in range(n):
            
            rn = np.random.randint(0,n)
            new_mat[_][__] = rn
    print(new_mat)


main()
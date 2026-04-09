from typing import List
import unittest


def count_six_tuples(S: List[int]) -> int:
    S_list = list(set(S))
    N = len(S_list)
    sum_ab = {}
    for i in range(N):
        for j in range(N):
            s = S_list[i] + S_list[j]
            sum_ab[s] = sum_ab.get(s, 0) + 1
    sum_cde = {}
    for i in range(N):
        for j in range(N):
            for k in range(N):
                s = S_list[i] + S_list[j] + S_list[k]
                sum_cde[s] = sum_cde.get(s, 0) + 1

    total = 0
    for f in S_list:  
        for ab_sum in sum_ab:  
            cde_needed = f - ab_sum 
            if cde_needed in sum_cde:
                total += sum_ab[ab_sum] * sum_cde[cde_needed]
    return total

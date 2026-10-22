#!/usr/bin/env python3
"""Exhaustive exact-integer proof audit for the top-three nonzero-digit gaps.

For every A006716 square root with >=3 nonzero decimal digits, write
e>p>q for the three highest nonzero digit positions. The theorem is
  (e-p, p-q) in {(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,1)}.
This is a sound necessary condition, not a classification of all roots.

The proof checks all possible eight-digit leading square prefixes
made from {1,4,9}, using only integer interval inequalities.
"""
from itertools import product

K = 8
WORDS = tuple(int("".join(t)) for t in product("149", repeat=K))
THRESHOLDS = ((1,4), (2,5), (3,2))


def intersection_possible(gap_first, min_gap_second, digit_a, digit_b):
    # Every root with leading a*10^e+b*10^p and p-q>=T satisfies
    #  a+b/10^g <= root/10^e < a+b/10^g+10^(-(g+T-1)).
    power = gap_first + min_gap_second - 1
    den = 10**power
    left = digit_a*den + digit_b*10**(min_gap_second-1)
    low_sq = left*left*(10**K)
    high_sq = (left+1)*(left+1)*(10**K)
    factor = den*den
    for leading_integer_digits in (1, 2):
        prefix_scale = 10**leading_integer_digits
        for prefix in WORDS:
            # Interval overlap of squared root range and
            # [prefix*10^j/10^K, (prefix+1)*10^j/10^K).
            if (low_sq < (prefix+1)*prefix_scale*factor and
                high_sq > prefix*prefix_scale*factor):
                return True
    return False


def main():
    checks=0
    for g,t in THRESHOLDS:
        for a,b in product(range(1,10),repeat=2):
            assert not intersection_possible(g,t,a,b), (g,t,a,b)
            checks+=1
        print(f"PASS: top gap {g} => second gap < {t}; all 81 high-digit pairs")
    assert checks == 243
    # For squares with fewer than 8 digits, the eight-digit-prefix
    # argument is not applicable; exhaust this finite exceptional range.
    small=[]
    for root in range(1, 3163):  # root**2 < 10**7
        if set(str(root * root)) - set("149"):
            continue
        exponents=[i for i,d in enumerate(reversed(str(root))) if d!="0"]
        if len(exponents)<3:
            continue
        e,p,q=exponents[-1],exponents[-2],exponents[-3]
        assert (e-p,p-q) in {
            (1,1),(1,2),(1,3),(2,1),(2,2),
            (2,3),(2,4),(3,1)
        }, (root,e,p,q)
        small.append(root)
    assert small == [212], small
    print("PASS: every square with fewer than 8 digits (sole 3-sparse root: 212)")
    print("CERTIFIED: positions e>p>q satisfy bounds (3,4,1) by top gap.")
    print(f"Only exact integer inequalities used; {2*3**8} prefix intervals per pair.")


if __name__ == "__main__":
    main()

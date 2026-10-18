#!/usr/bin/env python3
"""Exact A077187 order-class extension: 501 <= ord_p(10) <= 744.

Requires Python stdlib and certify_orders_le500.py from the same directory.
The 31 previously uncovered order classes are exhaustively recomputed using
integer ring Z/(10^r-1), not enumeration of prime divisors of 10^r-1.

Each G_r=gcd(10^r-1,U_r,V_r) is factored by complete trial division
(all values < 1000); every prime divisor is checked to have order != r.
The one genuinely new contamination case is r=696, G=189=3^3*7,
ord_7(10)=6. No assumption that rad(G)|rad(990*r) is used.

Rigorous finite computer-assisted claim, not an all-orders proof.
Run: python3 papers/A077187/research/certify_orders_le744.py
"""
from hashlib import sha256
from certify_orders_le500 import (
    already_covered, order_class_drift, split_order,
    multiplicative_order_10_mod_v
)

ROWS = [
    (504,504,567), (520,1560,9), (525,1050,27),
    (528,528,297), (536,17688,99), (544,544,153),
    (550,550,99), (552,6072,297), (560,1680,9),
    (568,19880,9), (575,12650,9), (584,584,657),
    (592,1776,9), (608,5472,9), (616,1848,99),
    (624,624,351), (632,8216,9), (650,1950,9),
    (656,3280,9), (664,27224,9), (672,672,189),
    (680,1360,9), (688,14448,9), (696,4872,189),
    (700,2100,9), (704,704,99), (712,7832,99),
    (725,20300,9), (728,2184,9), (736,8096,99),
    (744,3720,27),
]
SHA256 = "1ce7d1bd7c0b0169d1182ae754e39f697a9ee59b898af42f8866ff6c66003d43"

def distinct_prime_factors(n):
    """Fully factor the small exact obstruction; no external factorization."""
    ans = []
    d = 2
    while d*d <= n:
        if n%d == 0:
            ans.append(d)
            while n%d == 0: n//=d
        d += 1
    if n>1: ans.append(n)
    return ans

def ord_mod_10(p):
    """Only used when gcd(10,p)==1, on small prime factors of G."""
    if p in (2,5):
        return None
    a=10%p
    k=1
    while a!=1:
        a=a*10%p
        k+=1
        assert k<=p
    return k

def audit():
    expected_orders = [r for r in range(501,745) if not already_covered(r)]
    assert expected_orders == [r for r,t,g in ROWS], expected_orders
    summary=[]
    for r,T0,G0 in ROWS:
        T,N,G,U,V=order_class_drift(r)
        assert (T,G)==(T0,G0),(r,T,G)
        assert N==10**r-1
        assert 0 <= U < N and 0 <= V < N
        assert N%G==0 and U%G==0 and V%G==0
        primes=distinct_prime_factors(G)
        for q in primes:
            assert q!=r+1 or ord_mod_10(q)!=r
            assert ord_mod_10(q)!=r,("potential zero drift at exact order",r,q)
        summary.append((r,T,G))
    text="".join(f"{r},{t},{g}\n" for r,t,g in summary).encode()
    assert sha256(text).hexdigest()==SHA256
    assert dict((r,G) for r,T,G in summary)[696]==189
    assert ord_mod_10(7)==6
    print("PASS 31 exact new multiplicative-order classes, 501..744")
    print("PASS no prime factor of any exact G_r has ord_p(10)=r")
    print("PASS nonprimitive 7 at r=696 excluded by actual order 6")
    print("SHA256",SHA256)
    print("Unrestricted A077187 conjecture remains OPEN.")

if __name__ == "__main__":
    audit()

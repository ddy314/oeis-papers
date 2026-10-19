#!/usr/bin/env python3
"""Experimental A006063 five-cube high-start audit; NOT a symbolic proof.

Dependencies: networkx and scipy/numpy. The mathematical launch and
twofold-cover lemmas are in HIGH_START_INTERVAL_AUDIT.md. This script is
for reproducibility only and should NOT be cited as a Tutte theorem.
"""
import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching

COLORS = (216,343,512,729,1000)


def graph(n, cubes=COLORS):
    G = nx.Graph()
    G.add_nodes_from(range(1,n+1))
    for c in cubes:
        for i in range(max(1,c-n),min(n,c-1)+1):
            j = c-i
            if i<j:
                G.add_edge(i,j,cube=c)
    return G


def involution(n, cubes=COLORS):
    G=graph(n,cubes)
    fixed=(108,) if n%2 else ()
    for i in fixed:
        assert i+i in cubes
        G.remove_node(i)
    pairs=nx.max_weight_matching(G,maxcardinality=True)
    if len(pairs)*2!=n-len(fixed):
        return None
    assert all(i+j in cubes for i,j in pairs)
    assert len({x for pair in pairs for x in pair})==n-len(fixed)
    return pairs,fixed


def has_cube_sum_permutation(n,cubes):
    row=[];col=[]
    for c in cubes:
        for i in range(max(1,c-n),min(n,c-1)+1):
            row.append(i-1)
            col.append(c-i-1)
    A=csr_matrix((np.ones(len(row),dtype=np.int8),(row,col)),shape=(n,n))
    return bool(np.all(maximum_bipartite_matching(A,perm_type="column")>=0))


def launch_window(k):
    c=k**3
    b=(c-1)//2
    a=c-1-(((k+1)**3-1)//2)
    assert a+b+2<=c<=2*b+2
    assert c-a-1==((k+1)**3-1)//2
    assert b-a+1==(((k+1)**3-k**3+1)//2)
    return a,b


def main():
    windows={9:(229,364),10:(334,499),11:(467,665),
             12:(629,863),16:(1639,2047)}
    for k,expected in windows.items():
        assert launch_window(k)==expected
    for n in range(467,666):
        deg=[sum(1<=c-i<=n for c in COLORS) for i in range(1,n+1)]
        assert min(deg)>=2,(n,min(deg))
        assert involution(n) is not None,n
    # Four colors never suffice uniformly on the whole interval:
    # Hall already fails at n=467 for four deletions, and at
    # n=569 when removing the cube 1000.
    for missed in COLORS:
        n=569 if missed==1000 else 467
        assert not has_cube_sum_permutation(
            n, tuple(c for c in COLORS if c!=missed)), (missed,n)
    # At 360/362, the lower five-color band lacks LOOPLESS
    # perfect matchings, not involutions in general. We do not
    # incorrectly assert absence of an involution with two loops.
    for n in (360,362):
        assert involution(n,(64,216,343,512,729)) is None
    print("PASS: launch-window arithmetic at five starting scales")
    print("PASS: min degree >=2 on each of 199 high-window graphs")
    print("PASS: 99 even lengths have fixed-point-free involutions")
    print("PASS: 100 odd lengths have involutions fixing only 108")
    print("PASS: every single-cube deletion has a Hall counterexample")
    print("NOT PROVED: a uniform, computation-free Tutte inequality")


if __name__=="__main__":
    main()

# Cube-sum permutations: global principles independent of the 173 cutoff

**Research note — 2026-10-18.** Companion to [main.tex](main.tex) and
[PR #13](https://github.com/dongxuelian2/oeis-papers/pull/13).

For every n >= 1, let P(n) count permutations p of [n] such that
i + p(i) is an integer cube for every i. Set P(0)=1 as a convention.
Write C={8,27,64,125,...}.

The following results put the all-length existence question inside
a wider combinatorial and algebraic theory. Some underlying results
(Hall, permutation cycle covers, determinant/permanent modulo 2)
are classical; the special cube-sum consequences and the displayed
four-interval affine construction are the objects documented here.
Nothing in Sections 1–4 assumes a computer-aided verification of the
sharp threshold 173.

## 1. Exact graph and independent-set formulations

Let G_n have vertices [n], an undirected edge ij for i != j when
i+j is a cube, and a loop at i if 2i is a cube. Define N(S) as all
vertices adjacent to at least one vertex in S, including loops.

**Perfect-2-matching/cycle cover.** Every valid permutation breaks
uniquely into fixed points (loops), transpositions (dimers) and
oriented cycles of length >= 3. In particular, existence is equivalent
to a spanning configuration of such undirected components. If F is an
unoriented configuration and c(F) counts its length>=3 cycles,

    P(n) = sum_F 2**c(F).

**Independent-set Hall criterion.** The bipartite double cover of G_n
has a perfect matching if and only if every *independent* I in G_n,
with loops also disallowed, satisfies |N(I)| >= |I|.

An elementary proof of sufficiency avoids referring to the general
perfect-2-matching theorem: suppose any S fails Hall's inequality.
Put I=S\N(S). Then I is independent, N(I) is disjoint from S and

    |N(I)| <= |N(S)\S| < |S\N(S)|=|I|.

Consequently *every* failed Hall inequality has an independent
counterpart. All 124 already archived negative witnesses for n<173
satisfy this stronger independence property.

## 2. Global near-perfect matching and boundary localization

These results hold at every length n>=7, regardless of whether
P(n) is zero.

**Near-perfect theorem.** Put k=floor(cuberoot(n+1)).
Choose the closer of k**3 and (k+1)**3 to n+1 and call it c.
Then

    J=[max(1,c-n), min(n,c-1)]

is a contiguous interval of exactly n-|c-(n+1)| positions. Reflection
i -> c-i permutes J and every index-image sum equals c. Since

    |c-(n+1)| <= ((k+1)**3-k**3)//2
              = (3*k*k+3*k+1)//2,

the maximal partial matching covers at least

    n - (3*k*k+3*k+1)//2

positions (the exact number covered by this reflection is
n-|c-(n+1)|). Thus the unmatched proportion is O(n**(-1/3)).
There is no finite base certificate in this argument.

**Boundary-localization theorem.** Put
K=floor(cuberoot(2*n)) and G=(K+1)**3-K**3.
For any S subset [n], if its diameter is at most n-G,
the integer interval

    [max(S)+1, min(S)+n]

contains a cube c. The map i -> c-i is therefore an injection
S -> N(S), proving |N(S)| >= |S|.

Indeed the candidate interval has >=G consecutive integers, and no
G consecutive integers in [2,2n] can be noncubes. Therefore every
Hall-deficient independent set I must satisfy

    max(I)-min(I) > n-G,
    min(I) < G,
    max(I) > n-G+1.

Only independent sets simultaneously reaching the *two boundary
layers of thickness O(n**(2/3))* can possibly obstruct existence.
This is a new precise target for an entirely non-computational
eventual-existence proof; it is not itself that proof.

## 3. Threshold-free affine renormalization

The length-171 involution is specified by four reflection blocks:

    [1,7]    : p(i)=8-i
    [8,19]   : p(i)=27-i
    [20,44]  : p(i)=64-i
    [45,171] : p(i)=216-i

All four sums are cubes and each interval maps bijectively to itself.

**General perfect-power identity.** For any integer d>=2, odd t,
L=t**d and A=(L-1)//2, set T_t(n)=L*n+A. Let P_d(n)
count dth-power-sum permutations. Take one valid prefix permutation
of size A and choose L independent legal permutations p_r of [n].
For each position x=A+(i-1)*L+r, define

    Q(x)=A+(p_r(i)-1)*L+(L+1-r).

Then x+Q(x)=L*(i+p_r(i)), which is a dth power, and all different
choices give different output permutations. Hence

    P_d(T_t(n)) >= P_d(A) * P_d(n)**L.
    2*T_t(n)+1 = L*(2*n+1).
    T_s(T_t(n)) = T_(s*t)(n).

With d=3 and t=7, the explicit prefix size A=171 suffices:

    T(n)=343*n+171,
    P(T(n)) >= P(n)**343,
    T**r(n)=343**r*(n+1/2)-1/2,
    P(T**r(n)) >= P(n)**(343**r).

For any n with P(n)>0, set h(n)=log(P(n))/(n+1/2).
Then h(T(n))>=h(n), and consequently

    limsup_N log(P(N))/N
       >= sup_{n>=1:P(n)>0} log(P(n))/(n+1/2).

This is a multiplicative semigroup action on the odd coordinate
2n+1, with no dependence on a sharp eventual-existence threshold.

## 4. Global parity and factorization

Let H_n be the symmetric n-by-n matrix with entries
H[i,j]=1 if and only if i+j is a cube.

    P(n) = permanent(H_n).
    P(n) mod 2 = determinant(H_n) over GF(2).
               = (number of legal involutions) mod 2.

In particular, if H_n is nonsingular over GF(2), at least one legal
involution exists. All fixed points of a legal permutation occur
at indices i=4*r**3 (because 2i=(2r)**3).

**Factorization from a single valid permutation.**
Given one legal p, form the directed graph with arcs i->j when
i!=j and i+p(j) is a cube. For each strongly connected component C,
let B_C[i,j] record the same allowed relation, *including*
the diagonal i=j. Then

    P(n) = product_{C is an SCC} permanent(B_C).

Any alternative q yields f=p^{-1}o q. The directed cycles of f
must be entirely inside SCCs, so the choices multiply exactly.
This makes multiplicity and uniqueness transparent: P(n)=1 iff
all SCCs are singleton, and a nontrivial SCC supplies a second
solution. At n=236 the nine five-cycle components yield P(236)=2**9.

Independent exact regressions:
- python papers/A006063/renormalization.py
- python papers/A006063/global_graph_audit.py
- python papers/A006063/verify_extended.py

## 5. Distinct global research questions

1. **Complete existence without a finite certificate:** prove that a
   sufficiently large cube-sum graph has no independent Hall-deficient
   set simultaneously spanning both boundary layers. The localization
   theorem reduces the question but does *not* eliminate it.
2. **Uniform exponential counts:** show P(n)>=exp(c*n) for all
   sufficiently large n, rather than only explicit infinite
   subsequences. Such a claim has **not** been proved.
3. **Entropy limit:** decide whether log(P(n))/n converges, diverges,
   or oscillates. The current limsup lower bound and affine entropy
   monotonicity along sparse orbits do not answer this.
4. **Parity/Hankel structure:** characterize when the binary Hankel
   matrix H_n=(1_{i+j is cube}) is nonsingular. This is a distinct
   arithmetic problem about the GF(2) indicator sequence of cubes.
5. **Other perfect powers:** for exponents d>=2, determine the
   existence threshold (if any), nontrivial finite seeds and their
   affine renormalization semigroup.

These questions explicitly separate what is currently a proved
global theorem from what remains a conjectural extension.

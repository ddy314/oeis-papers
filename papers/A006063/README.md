# Cube-sum permutation classifications (OEIS A006063, A096680, A096904)

**Date:** 2026-10-18  
**Status:** Complete computer-assisted proof candidate, pending independent audit and literature priority check.

We study the number `P(n)` of permutations `p` of `{1,...,n}` such that every `i+p_i` is a perfect cube. The results are mathematical theorems conditional only on fully explicit finite integer certificates, whose validation is independently reproducible. No OEIS page has yet been changed.

## Latest finite proof: 74 exceptional identities + 3 algebraic templates

**Latest primary proof (October 19, 2026):** [COMPRESSED_FINITE_PROOF.md](COMPRESSED_FINITE_PROOF.md) and [PARAMETRIC_BLOCK_TEMPLATES.md](PARAMETRIC_BLOCK_TEMPLATES.md), with the standalone [finite_base_note.tex](finite_base_note.tex), now establish `P(n)>0` for all `n>=173` using **74 explicit exceptional endpoint-multiset equalities (969 blocks)** and **three pure algebraic block-rearrangement schemes** generating eight more seed lengths (`66,85,100,103,119,122,182,254`). This accounts for the same 82 finite seeds as before, but the eight template instances no longer require separate endpoint checking. The remaining 26 sub-173 and 132 middle lengths follow by the original strictly increasing cubic suffix reflection, and the unbounded tail by a symbolic cubic-gap inequality.

- [74 exceptional rows](certificates/finite_74_exceptional_atlas.txt), with the [typeset appendix](certificates/finite_74_exceptional_atlas.tex).
- [Three algebraic formulas and affine-rigidity obstruction](PARAMETRIC_BLOCK_TEMPLATES.md).
- [Independent 74+templates audit](verify_74_plus_templates.py), not using the old 82-row table or matching.
- [Redundant 82-row complete certificate](certificates/finite_82_seed_atlas.txt), now optimized to **1,009** blocks (down from 1,009 and the original 109-row count of 1,123). Independent checker [verify_82_seed_proof.py](verify_82_seed_proof.py) remains available.

**Boundary:** Three parameterized families replace eight particular cases; they do *not* constitute a case-free construction for all the remaining 74 lengths. CI/PDF status must be confirmed after the latest workflow runs, not assumed.

## Earlier 82-row independent arithmetic certificate (October 19, 2026)

The latest self-contained proof is [COMPRESSED_FINITE_PROOF.md](COMPRESSED_FINITE_PROOF.md), with a typeset standalone paper [finite_base_note.tex](finite_base_note.tex), a complete [82-row arithmetic atlas](certificates/finite_82_seed_atlas.txt) and independent [exact checker](verify_82_seed_proof.py).

Rather than rely on 109 independent entries, the new proof uses **82 endpoint-multiset identities in 1,009 reflection blocks**: 22 seeds below 173 and 60 seeds in 173..364. An explicit grouped predecessor table certifies 26 additional smaller lengths and 49 missing lengths in 173..255 or 339..364, followed by one uniform reflection through cube 512 for all 83 lengths 256..338. The proof for every n>=365 remains purely algebraic, via the least cube >= n+174.

The prior 109-identity proof below is retained as an **independent redundant certificate**. In particular, the 82-row proof does not depend on the 109-row table, any matching algorithm, the original 191 augmenting words, or the previous JSON permutation archives. **This is still finite casework, not a parameter-free construction.** GitHub Actions must execute successfully before claiming CI verification of the updated LaTeX PDF.

## Earlier 109-identity proof: independent algebraic certificate

**This is an earlier, independently retained result.** [FINITE_INTERVAL_PROOF.md](FINITE_INTERVAL_PROOF.md) and the standalone [finite_base_note.tex](finite_base_note.tex) prove the missing finite base interval using a single elementary **boundary cancellation lemma** plus [109 explicit piecewise-reflection rows](certificates/finite_block_atlas.txt), now reproduced in the LaTeX appendix.

For each row, take endpoints `0=b_0<...<b_t=n` and cube roots `k_j`. Define `L_j=k_j**3-b_j` and `R_j=k_j**3-b_(j-1)`. The row defines a legal permutation precisely when `1<=L_j<R_j<=n+1` and

```
multiset(1,R_1,...,R_t) = multiset(n+1,L_1,...,L_t).
```

All 109 displayed rows (n=173..255 and 339..364) satisfy this integer identity: **1,123** reflected intervals in total, roots 2..8. The remaining n=256..338 follow from the single reflection `m=511-n`, `m+n+1=512`; n>=365 follows by strong induction and the existing cube-gap lemma. Thus this gives a **self-contained, paper-checkable finite arithmetic certificate** of all n>=173 without executing the 191 augmenting words or any perfect-matching solver.

**Important limitation:** this is not yet a uniform case-free derivation. The 109 explicit rows remain finite casework, albeit plain integer identities rather than computationally generated matchings. `finite_endpoint_identity.py` independently audits the list; it is optional for the proof.

## Results

1. **Exact A006063 membership.** `P(n)>0` for every `n>=173`. The 48 positive lengths below 173 are exactly those listed by OEIS; all 124 negative lengths have explicit Hall-obstruction witnesses. Therefore **`A006063(j)=j+124` for every index `j>=49`**, strengthening the formerly conjectural tail formula (which was stated for indices >=173).
2. **Exact A096680 membership.** `P(173)=P(174)=1`, and `P(n)>=3` for every `n>=175`. Exactly 13 lengths below 173 have multiple valid permutations: `112,115,116,117,119,124,125,126,127,128,129,130,133`. Thus **`A096680(j)=j+161` for every index `j>=14`**.
3. **Quantitative A096904 theorem.** Let `K(n)=floor(cuberoot(2*n))` and `q(n)=max(0,floor((K(n)-27)/6))`. For every `n>=173`,
   
   ```
   P(n) >= 3**q(n)
   ```
   
   so **`log P(n) >= ((2*n)**(1/3) * log(3)/6) - O(1)`**. This is a genuine exponential-in-cube-root lower bound on the number of distinct cube-sum permutations.

### Linear entropy on both parity-minimal subsequences

In the taxicab two-block involution, the baseline has one fixed point
from a block if and only if that block's cube sum is **even**.
Each disjoint four-vertex dimer switch changes only transpositions,
so it never creates or removes fixed points.

Restricting the cube-scaling parameter `u` to **odd** positive
integers, the two explicit taxicab identities give

```
even n = 54406*u**3:
  J_0(n) >= 2**((4913*u**3-1)//2),   zero fixed points.

odd n = 4118149*u**3:
  J_1(n) >= 2**((970299*u**3-1)//2), exactly one fixed point.
```

Here `J_0` counts fixed-point-free legal involutions at even lengths
and `J_1` counts involutions with exactly one fixed point at odd
lengths. Both are *parity-minimal*, and both admit positive linear
entropy along their explicit infinite subsequences:

```
limsup_even log J_0(n)/n >= 4913*log(2)/108812
limsup_odd  log J_1(n)/n >= 970299*log(2)/8236298.
```

These are **pure algebraic counts**, not matching search results.
They complement the earlier *all-length* parity-minimal theorem,
whose uniform proven growth remains `exp(Omega(n**(1/3)))`.
The statement that `J_min(n)>=exp(c*n)` for *every* sufficiently
large n remains **unproved**.

## Taxicab switching: exponentially many *involutions* without finite certificates

A new purely algebraic global principle produces **exponentially many legal involutions**, not merely arbitrary cube-sum permutations. For any fixed exponent `d>=2`, take four *perfect d-th powers* `A,B,C,D` with

```
A+B=C+D
(3*A)/2 <= C < B/2.
```

For every integer u>=1 put `T=u**d`, `N=(B-A)*T` and start from the two-block involution

```
p(i)=A*T-i   on [1,A*T-1]
p(i)=B*T-i   on [A*T,(B-A)*T].
```

For each `s=1,...,H=floor((A*T-1)/2)`, take four vertices

```
a=s,       b=A*T-s,
c=C*T-s,   d=(B-C)*T+s.
```

The vertex quadruples are disjoint. Their baseline dimers `(a,b)` and
`(c,d)` have perfect-power sums `A*T,B*T`, whereas the alternative
dimers `(a,c)` and `(b,d)` have perfect-power sums `C*T,D*T`.
Each switch preserves the involution property and changes exactly four
permutation entries. Switching arbitrary subsets gives

```
I_d((B-A)*u**d) >= 2**floor((A*u**d-1)/2),
limsup log(I_d(n))/n >= A*log(2)/(2*(B-A)) > 0.
```

The encoding multiplies all binary Hamming distances by exactly **4**.
A particularly small cubic example is the taxicab identity

```
17**3 + 39**3 = 26**3 + 36**3.
I_3(54406*u**3) >= 2**floor((4913*u**3-1)/2).
```

The identity `99**3+172**3=120**3+163**3` is another example,
giving the stronger optional coefficient `970299*log(2)/8236298`;
neither is asserted optimal. The general theorem does not depend on
the sharp cutoff or any finite matching certificate.

The independent `taxicab_involution_audit.py` checks both integer
identities and the disjoint dimer-switch inequalities. A separate
local implementation fully materialized and verified both original
and modified 54,406-element involutions, all sums being cubes.

### Inverse-paired tensorization: exact involution fiber count

Independent perfect-power fibers can also be paired to create genuine
**involutions**, even when some base permutations are not involutive.
In the previous tensor map, a position `(i,r)` maps to
`(p_r(i),L+1-r)`, so the lifted map is an involution exactly when

```
p_(L+1-r) = inverse(p_r)                 (r=1,...,L).
```

Since `L=t**d` is odd and the inverse of a legal power-sum permutation
is also legal, its **exact** number of involutive middle-block lifts is

```
I_d(M) * P_d(M)**((L-1)//2).
```

Consequently, **if** legal involutions exist at all sufficiently large
lengths, and some M has `I_d(M)>=1` and `P_d(M)>=2`, then

```
limsup_n log(I_d(n))/n >= log(P_d(M))/(2*M+1) > 0.
```

Complete the shifted middle interval by a legal involutive prefix of
size `A=(L-1)//2` and the shortest admissible perfect-power reflection
on the suffix. This is a general implication from finite ordinary
multiplicity to exponential involution multiplicity, conditional only
on eventual involution existence. The earlier taxicab construction
gives an **unconditional** exponential family without this assumption.

`inverse_fiber_involution_audit.py` independently verifies the
inverse-fiber equation with a legal 316-element reference involution and
a different legal, non-involutive five-cycle-switched permutation.

## Parity-optimal involutions and uniform minimal-fixed-point entropy

The previously proved eventual involution existence theorem can be
strengthened to the **minimum possible number of fixed points**, with no
reference to the sharp threshold 173:

```
odd  n>=70001:  valid cube-sum involution with exactly 1 fixed point (4)
even n>=230000: valid cube-sum involution with exactly 0 fixed points.
```

Two very small seeds suffice: `p(i)=8-i` on `[1,7]` is an involution
fixing only 4; `p(i)=27-i` on `[1,26]` is a fixed-point-free involution.
A reflection through an **odd cube** `c=k**3` preserves parity and
introduces **no new fixed point**, because its reflection center `c/2`
is nonintegral.

**Finite exact step (no matching algorithms).** Use only odd cube roots
in the recurrence `n=k**3-m-1>m`. The length-7 seed reaches all 15,001
odd lengths in `[70001,100001]`, and the length-26 seed reaches all
36,001 even lengths in `[230000,302000]`. The last unreachable
same-parity lengths before those regions are 69,601 and 228,026,
respectively. This is checked by two independent direct integer
implementations, and `parity_minimal_involutions.py` reconstructs
actual permutations and checks the involution equation and exact fixed
point sets.

This finite coverage is also certified **independently by symbolic parity-interval algebra**: `parity_interval_proof.py` encodes each parity length as `t=(n-p)/2` and performs the exact interval reflection `t -> (k**3-1-2*p)//2 - t` through odd cube roots. After **12 simultaneous rounds**, the odd/even reachable sets have 41,057/121,707 lengths in 2,997/7,047 merged intervals, respectively, and each target interval is contained in one merged interval. This avoids checking any full matching or even iterating through all individual reachable lengths during the closure step.

**Infinite step.** For odd n>100001 or even n>302000, let M be the
respective lower endpoint 70001 or 230000 and choose the least **odd**
root k with `k**3>=n+M+1`. Let `m=k**3-n-1`. Then m has the same parity
as n, m>=M, and `m<n`. The last inequality uses

```
2*n-k**3 >= 2*(k-2)**3-k**3-2*M
          = k**3-12*k*k+24*k-16-2*M.
```

The polynomial is increasing for k>=57; in the odd case k>=57 and
its value at 57 is 7555>0. For even n>302000 the minimum k is
at least 83, and its value at 83 is 31095>0. Induction finishes the
construction for every larger same-parity n.

An additional arithmetic strengthening is immediate: for **every even n>=230000**, the fixed-point-free matching can be chosen so that **every edge sum is an odd cube**, thereby pairing odd indices with even indices. For **every odd n>=70001**, exactly the original seven seed positions have the even cube sum 8; every index i>=8 has an odd cube sum. This is an exact global structural constraint, not just an asymptotic density statement.

**Uniform lower bound on the count.** Let `J_min(n)` count legal
involutions with no fixed point when n is even, or with the *sole*
fixed point 4 when n is odd. The proof also establishes

```
liminf_{n->infinity} log(J_min(n))/(2*n)**(1/3) >= log(2)/4.
```

Indeed, count odd-cube-only reflection histories from each parity
seed. For s odd roots `q,q-2,...,q-2(s-1)` and
`K(n)=floor(cuberoot(2*n))`, exact cube-gap inequalities imply
`K(m_j)>=K(n)-4(j+1)` for sufficiently large n. The s-branch
recursion has a geometric growth root `rho_s`, satisfying
`sum(rho_s**(-h) for h in 1..s)=1`, so it gives a lower bound with
exponent `(K(n)-B_s)/4`. Letting s->infinity yields the coefficient
`log(2)/4`.

These stronger global structural results need only finite
**arithmetic reachability**, not the much larger historic
perfect-matching base certificates. They do not assert sharp values of
the new eventual thresholds.

## Eventual *involution* existence, not merely general matching

The original seven-element seed `p(i)=8-i` is a legal **involution** fixing position `4`. Each later suffix reflection is an involution on a disjoint new interval. Consequently **every permutation in the entire one-seed reflection tree** remains an involution and fixes 4.

Let `I_4(n)` count legal cube-sum involutions of length n with `p(4)=4`. The seven-round eventual-existence proof and reflection-tree entropy together give

```
I_4(n) >= F(n) > 0                  (every n>=8915),
liminf(log(I_4(n))/(2*n)**(1/3)) >= log(2)/2.
```

This is a stronger **all-length involution theorem** than the previous ordinary matching statement. It also exposes a structural distinction: at n=236 there are 512 legal permutations but *no involution*, whereas every sufficiently large cube-sum graph has a spanning decomposition consisting only of allowed loops and dimers.

`involution_tail_audit.py` reconstructs sample permutations solely from the seven-term seed and exact reflection-closure data and verifies the involution equations `p[p[i]]=i`, the permanent fixed point `p[4]=4`, and the loop/dimer decomposition. The infinite theorem remains mathematical, conditional only on the previously archived finite seven-round arithmetic reachability check.

## A structural boundary: reflection entropy versus cycle entropy

The reflection method has an **intrinsic information-theoretic upper bound**. In every strictly increasing sequence of reflection extensions the cubes used are strictly increasing, since

```
c_j = n_(j-1)+n_j+1
c_(j+1)-c_j = n_(j+1)-n_(j-1) > 0.
```

Thus a reflection history from a fixed starting permutation is uniquely encoded by a subset of `{2**3,3**3,...,floor(cuberoot(2*n))**3}`. In particular, for the single-seed family `F(n)`,

```
F(n) <= 2**(K(n)-1),   K(n)=floor(cuberoot(2*n)).
```

Combined with the **previously proved** uniform reflection-tree lower bound,

```
log F(n) = Theta(n**(1/3))                (n -> infinity).
```

More generally, `S` fixed finite starting permutations generate at most `S*2**(K(n)-1)` permutations of length n by any number of strict suffix reflections. This is **subexponential in n**. By contrast, our standalone two-block three-cycle construction produces `P(681707*u**3)>=2**(148877*u**3-1)`, which is exponential in n. The contrast proves that reflection-only constructions from finitely many seeds **cannot capture the positive linear entropy supplied by disjoint alternating cycles**.

A separate *depth sparsity* theorem bounds the number of different lengths <=N reachable from one seed in <=r reflections:

```
#reachable_lengths <= sum(comb(K(N)-1,j) for j=0..r).
r<=2: o(N) lengths;
r<=3: N/3 + O(N**(2/3)) lengths.
```

Therefore **at least four** steps would be necessary to cover all sufficiently large lengths with a bounded-depth one-seed construction. In the first million lengths the actual <=3-step reflection closure from the seven-element seed reaches only 98,749 lengths, well below the upper bound. The possibility of a uniform upper bound of seven steps for all sufficiently large n remains **open**.

`reflection_entropy_barrier.py` verifies exact reflection-tree upper bounds and independently enumerates all root sequences through depth three at several finite ranges. The upper bounds themselves are elementary theorems and do not rely on such numerical tests.

## Local arithmetic expansion and macroscopic Hall obstructions

For distinct cube-sum bipartite left vertices `i!=j`, any shared right neighbor gives two cubes whose difference is `|i-j|`. The factorization

```
a**3-b**3 = (a-b)*(a*a+a*b+b*b)
```

implies at most **tau(|i-j|)** common right neighbors, since each divisor `a-b` can determine at most one solution. Here `tau(d)` is the positive-divisor-count function.

Let `delta` and `Delta` denote the minimum and maximum degrees in the cube-sum bipartite graph, and `D=max(tau(d),1<=d<n)`. An exact Cauchy-Schwarz argument gives, for *every* nonempty left vertex set `S` of size `s`,

```
|N(S)| >= s*delta**2/(Delta+(s-1)*D).
```

Since `delta >= (2**(1/3)-1)*n**(1/3)-1`, `Delta=O(n**(1/3))` and the standard divisor estimate is `D=O_epsilon(n**epsilon)`, any Hall-deficient set must have

```
|S| >= c_epsilon * n**(2/3-epsilon)
```

for **every fixed epsilon>0 and sufficiently large n**. Together with the earlier boundary-diameter theorem, any obstruction must simultaneously be a *large* independent set **and** stretch across a range of length `n-O(n**(2/3))`. This gives a two-dimensional arithmetic-geometric obstruction localization, with no use of the 173 threshold.

`arithmetic_expansion_audit.py` independently validates the codegree inequality and second-moment expansion on exact integer cube-sum graphs.

### Fibonacci upper bound: sharper than root-set counting

Let `K=floor(cuberoot(2*n))` and `F(n)` be the seven-seed strict-reflection count. A cubic identity shows that for **every predecessor** arising from cube `(K-j)**3`,

```
2*m <= (K-2*j)**3 - 6*j*j*(K-j) - 2 < (K-2*j)**3,
K(m) <= K-2*j-1.
```

Thus the possible predecessor root-height drops are at least
`1,3,5,7,...`. Define `B_2=B_3=B_4=1` and
`B_k=B_(k-1)+B_(k-2)` for `k>=5`. A strong induction using the
exact tree recurrence gives the uniform **Fibonacci majorant**

```
F(n) <= Fib_(K(n)-2)       whenever K(n)>=3,
F(n) <= 1                 when K(n)=2.
```

Consequently the known coefficients for the *single-seed* growth obey

```
(log(2))/2 <= liminf(log(F(n))/(2*n)**(1/3))
             <= limsup(log(F(n))/(2*n)**(1/3))
             <= log(phi),  phi=(1+sqrt(5))/2.
```

Unlike the earlier coarse upper estimate `2**(K(n)-1)`,
the Fibonacci bound accounts for how much cube-root height each
reflection consumes. This is a genuinely tighter global bound, and
the exact limiting coefficient remains an open problem.
The refreshed `reflection_entropy_barrier.py` verifies the
Fibonacci majorant and the strict predecessor height inequalities
at every length up to 12,000.

## A single 7-element seed: a self-contained eventual theorem and counting tree

The sharp cutoff n=173 is **not** needed for this simpler eventual-existence theorem. Starting from the sole explicit permutation `(7,6,5,4,3,2,1)`, with every sum equal to 8, take seven rounds of the elementary reflection rule

```
n=k**3-m-1,   m<n.
```

The integer closure in the finite universe `n<=10975` has exact round cardinalities `1,21,189,995,3280,6588,8533,8924`. The last round contains the entire interval `[8915,10975]`. For `n>=10976`, the **smallest** cube `c>=n+8916` always satisfies `c<=2*n` by an explicit cubic inequality, so `m=c-n-1` lies in `[8915,n-1]`, completing strong induction.

**Proved:** `P(n)>0` for every `n>=8915`. This is weaker in its cutoff than the separate exact A006063 result, but *structurally much simpler*: a single seven-term reversal, one reflection lemma, and two independent finite integer-only verifiers. Neither bipartite matching nor the 191 original augmenting words are required.

- `one_seed_eventual.py` constructs actual full permutations via the seven-round finite closure and universal cube-gap induction, with `O(log log n)` reflection layers and `O(n)` output.
- `one_seed_interval_proof.py` independently derives the same finite interval by integer interval-union reflection. The seven-round interval counts are `1,21,186,870,2077,2037,1031,770`; its final rightmost interval is exactly `[8915,10975]`.
- `reflection_tree_counts.py` counts all distinct reflection histories from the seed by the exact recurrence `F(7)=1` and `F(n)=sum(F(m) for 7<=m<n if m+n+1 is a cube)`. The final permutation value uniquely determines the predecessor, so histories are distinct permutations.

The tree itself satisfies **the same asymptotic lower bound as the general P(n)**:

```
liminf_{n->infinity} log(F(n))/(2*n)**(1/3) >= log(2)/2.
```

Thus even the explicitly constructed one-seed subfamily has universal `exp(Omega(n**(1/3)))` growth, without invoking the sharp-threshold existence certificates. The finite seven-round arithmetic check is still present and clearly distinguished from a wholly computation-free proof.

## Standalone note: global theorems, not the threshold

[GLOBAL_STRUCTURE.md](GLOBAL_STRUCTURE.md) is a self-contained companion note organizing the threshold-free results: symmetric perfect-2-matching and independent Hall criteria; explicit near-perfect matchings of size `n-O(n**(2/3))` for every `n>=7`; localization of all possible Hall obstructions to thin boundary layers; affine renormalization `P(343n+171)>=P(n)**343`; characteristic-2 parity; and exact strongly connected component factorization. It also distinguishes proven theorems from the open questions of uniform exponential counts and removing finite existence certificates.

## Global structure, beyond the sharp threshold

### Affine renormalization and semigroup action

A **pure four-interval construction** supplies a length-171 cube-sum involution:
`p(i)=8-i` on `1..7`, `27-i` on `8..19`, `64-i` on `20..44`, `216-i` on `45..171`.

Hence, with `T(n)=343*n+171`, the independent-fiber block construction gives **for every n>=1**

```
P(T(n)) >= P(n)**343
T**k(n) = 343**k*(n+1/2)-1/2
P(T**k(n)) >= P(n)**(343**k).
```

The exponentiation is literal (iterated affine action, not a computational bound). For every `n` with `P(n)>0`, its normalized entropy `h(n)=log P(n)/(n+1/2)` cannot decrease along its orbit. Therefore

```
limsup_N log(P(N))/N >= sup_{n>=1, P(n)>0} log(P(n))/(n+1/2).
```

This is an **exact, threshold-free closure property**, independent of the statement that every n>=173 is admissible.

The more general odd-perfect-power renormalization uses `L=t**d`, `A=(L-1)//2`, `T_t(n)=L*n+A` and satisfies

```
P_d(T_t(n)) >= P_d(A) * P_d(n)**L,
2*T_t(n)+1 = L*(2*n+1),
T_s(T_t(n)) = T_(s*t)(n).
```

`renormalization.py` reconstructs the explicit four-block seed and verifies two lifts, including independent choices of one 316-element cube-sum permutation fiber.

### Global graph and parity identities

Let `G_n` have an undirected edge `{i,j}` when `i+j` is a cube and a loop at `i` when `2*i` is a cube. Every cube-sum permutation decomposes into loops, transpositions (undirected dimers), and directed cycles of length at least three. Thus

```
P(n) = sum(2**number_of_long_cycles(F) for each undirected spanning cycle-cover F).
P(n) % 2 = number_of_legal_involutions(n) % 2.
P(n) % 2 = det(H_n) % 2.
```

Here `H_n[i,j]` is 1 when `i+j` is a cube, and its determinant is taken over `GF(2)`. Thus **parity is decidable in polynomial time** by binary Gaussian elimination, even though counting all permutations may be difficult.

**Independent-set criterion:** A valid permutation exists if and only if every vertex set `I` containing no internal cube-sum edges (or loops) has `|N(I)|>=|I|`. This follows by reducing any deficient Hall set `S` to `I=S\\N(S)`. All 124 negative certificates already satisfy this stronger condition. A fixed point can only occur at `i=4*r**3`. If `det(H_n)=1 mod 2`, then at least one valid involution must exist, although the reverse implication is not automatic.

For any one known valid permutation `p`, consider arcs `i->j` when `i+p[j]` is a cube. Every alternative matching decomposes independently over the directed **strongly connected components**, and `P(n)` is the product of the permanents of these component submatrices. This unifies exact counting, uniqueness and alternating-cycle multiplicity under a single graph theorem. In particular, the nine five-cycle components at `n=236` immediately give `P(236)=2**9`.

`global_graph_audit.py` independently checks the four-block unique n=171 solution, the nine components at n=236, their exact count, and binary-matrix parity at lengths 7,171,236. No large A006063 existence certificate is used.

## Reduced-computation mathematical proof

The **new primary existence certificate** uses *one* explicitly described involution at `n=173` (only seven symmetric reflection interval blocks), followed by exactly **191 short alternating-path words** for `n=174,...,364`. The words use only the cube-root alphabet `{2,3,4,5,6,7,8}` and contain **1,844 root digits total**, compared with the previous full 192-row archive of 51,552 permutation entries.

The mathematical lemma is simple: a word `r_1 ... r_t` defines a successive path from the newly free left vertex `n` by right edges `v_j=r_j^3-u_{j-1}`; when `v_j<n`, follow the unique old matching edge backwards to its left endpoint, and terminate on the newly free right vertex `n`. If no vertex repeats, flipping this alternating path makes a new perfect matching. Each row can be checked with only short integer cube-sum identities; the checker does not solve a matching problem or read the previous long certificates.

- [certificates/augmenting_cube_words.txt](certificates/augmenting_cube_words.txt): 191 locally checkable 1-digit-root words; 2,947 bytes with comments and indices.
- [certificates/augmenting_words_table.tex](certificates/augmenting_words_table.tex): identical words typeset as a compact self-contained paper appendix.
- [one_seed_eventual.py](one_seed_eventual.py): construct all sufficiently large lengths from one 7-point seed and seven exact rounds.
- [one_seed_interval_proof.py](one_seed_interval_proof.py): independent finite interval-union proof of seven-round coverage.
- [inverse_fiber_involution_audit.py](inverse_fiber_involution_audit.py): verify inverse-paired arbitrary fiber permutations produce legal involutions.\n- [taxicab_involution_audit.py](taxicab_involution_audit.py): pure algebraic two-dimer switches yielding exponentially many involutions and Hamming-distance codes.\n- [parity_interval_proof.py](parity_interval_proof.py): independent 12-round symbolic parity-interval closure certificate.\n- [parity_minimal_involutions.py](parity_minimal_involutions.py): exact odd-cube closures for seeds 7/26; parity-minimal involutions for all sufficiently large lengths.\n- [involution_tail_audit.py](involution_tail_audit.py): verify eventual cube-sum involution constructions and invariant fixed point 4.\n- [reflection_tree_counts.py](reflection_tree_counts.py): count distinct reflection histories and cross-check the recursive tree.
- [renormalization.py](renormalization.py): verify the four-block 171 seed and exact cubic affine closure.\n- [global_graph_audit.py](global_graph_audit.py): exact parity over GF(2) and alternating-SCC count factorization.\n- [audit_three_cycle_identity.py](audit_three_cycle_identity.py): verify fully algebraic two-block cubic identity and disjoint 3-cycle construction.\n- [audit_permutation_code.py](audit_permutation_code.py): exact Hamming-distance audit for 512 base masks and independently lifted fiber masks.\n- [optimize_terminal_cube.py](optimize_terminal_cube.py): verify shortest admissible cube and stronger asymptotic entropy.\n- [tensorize_fibers.py](tensorize_fibers.py): independently validate fiberwise arbitrary base matchings and injectivity.\n- [lift_exponential_subsequence.py](lift_exponential_subsequence.py): exact block-lift audit for n=200839 and n=366690 plus all independent cycles.
- [count_236.py](count_236.py): independent 15-interval, nine-five-cycle exact count and non-involution proof for n=236.
- [verify_word_paths.py](verify_word_paths.py): independent exact arithmetic checker that reconstructs 192 matchings using the mathematical path lemma and a single seven-block starting involution.

The **60-seed** reflection-only compression is a useful **methodological boundary**, *provided the empty permutation is admitted alongside the 48 earlier positive witnesses*. In particular, `n=342` requires no seed: `p[i]=343-i` is a complete reversal with constant cube sum `7**3`. Exactly 60 further seeds are unavoidable under reflection alone. The alternating-path operation is the essential new ingredient that escapes that barrier.

### Sharper counting result — reflection entropy

Using the largest `s` available cubes at once, rather than only three, gives a family of **fully mathematical** counting inequalities. Let `rho_s` be the unique real root greater than 1 of `sum(rho_s**(-h) for h in 1..s)=1`, and put `B_s=2*s**2+4*s-1`. For every fixed `s>=2` and `n>=173`,

```
P(n) >= rho_s ** ((floor(cuberoot(2*n)) - B_s) / 2)
```

As `s` increases, `rho_s` increases to 2, yielding the **new asymptotic theorem**

```
liminf_{n->infinity} log(P(n)) / (2*n)**(1/3) >= log(2)/2
```

No additional finite certificate is needed for this asymptotic bound beyond the already-established qualitative existence theorem. This coefficient is a lower bound, not an unproved claim of optimality.


### Near-critical reflection bound (new)

A variable number of reflection branches gives a stronger inequality with an **explicit loss**, rather than only a liminf statement. Let `K=floor(cuberoot(2*n))`. For every `n>=173`,

```
P(n) >= (127/K) * 2**((K-127)/2)
```

Furthermore, for **every fixed real epsilon > 0**, some constant `C_epsilon > 0` satisfies

```
P(n) >= C_epsilon * 2**(K/2) / K**epsilon
```

The proof chooses `s=floor(log2 K)` branches for the explicit `1/K` factor and `s=ceil(log2(K/epsilon))` for the arbitrary-polynomial-loss result. The crucial inequality is

```
sum(2**(-h)*K/(K-2*h) for h=1..s)
    >= 1-2**(-s)+2/K > 1
```

for `K>=128`. The $n$-dependent branch count is algebraically admissible because `2**s >= 2*s*s+4*s-1` for every `s>=7`. Neither quantitative theorem needs any new finite matching certificate.

## A new exact case: P(236) = 512 with no involution

A cube-sum permutation need not be an involution, even though the cube-sum adjacency matrix is symmetric. In fact, we have a new **exact closed count**

```
P(236) = 512 = 2**9.
```

The proof is a short, independently checkable structural calculation. An explicit solution uses only **15 contiguous interval-reflection rows**, `p[i]=c-i`. Its associated alternating digraph has **191 singleton SCCs** and exactly **nine disjoint directed 5-cycle SCCs**, indexed by

```
S_t = {10+t, 46+t, 71+t, 137+t, 198+t},  t = 0,...,8.
```

Any other solution corresponds to a directed cycle cover in that graph: all singletons are forced, and each five-cycle offers exactly two choices (keep/flip). The central set `S_4={14,50,75,141,202}` is invariant under any solution and is necessarily oriented as one of two inverse 5-cycles, never an involution.

Thus **no legal involution exists at n=236**, despite 512 valid general permutations. The verification is a finite exact graph check, but it does not call a matching or permanent solver. Run `python papers/A006063/count_236.py`.

## Universal odd-cycle gadget (new structural unification)

The three-cycle construction is a special case of a general **weighted-cube identity for any odd cycle length `2q+1`**:

```
(q+1)*X + q*Y = A + 2*q*B
D_j = ceil(j/2)*(B-X) + floor(j/2)*(B-Y), j=0,...,2q.
```

If the four constants `A,B,X,Y` are cubes, every nonzero `D_j` lies in `[A,B-2*A]`, and all offsets differ by at least `A`, then the two-block reflection on `(B-A)*u**3` positions contains `A*u**3-1` **disjoint alternating cycles of length `2q+1`**. This gives

```
P((B-A)*u**3) >= 2**(A*u**3-1)
```

with no existence certificate or matching algorithm. The case `q=1` is the large three-cycle theorem below; `q=2` explains the small identity

```
3*5**3 + 2*8**3 = 3**3 + 4*7**3
P(316*u**3) >= 2**(27*u**3-1).
```

This identifies the shared algebraic mechanism behind odd-cycle matchings of several lengths rather than treating separate numerical identities as unrelated examples.

## NEW: entirely computation-free cubic matching family (strongest rate)

The key weighted identity is:

```
53**3 + 2*94**3 = 2*87**3 + 79**3.
```

Let `T=u**3` for **any integer u>=1** and `n=681707*T`. A two-reflection permutation is given by

```
p(i)=148877*T-i,   1 <= i < 148877*T
p(i)=830584*T-i,   148877*T <= i <= 681707*T.
```

Every reference sum is either `(53*u)**3` or `(94*u)**3`. For every `s=1,...,148877*T-1`, the triple

```
(s, s+172081*T, s+509626*T)
```

is a valid directed alternating 3-cycle. The swapped sums are `(87*u)**3,(79*u)**3,(87*u)**3`, and all these translated triples are pairwise disjoint. Therefore

```
P(681707*u**3) >= 2**(148877*u**3-1),
limsup_n log(P(n))/n >= 148877*log(2)/681707.
```

This improves the asymptotic constant to about **0.15136**, and, unlike the older certificate-dependent existence and tensorization proofs, is a **pure algebraic construction** requiring only two interval formulas and one exact equality of cubes. It also yields a canonical binary code with `148877*u**3-1` independent bits and exact permutation Hamming distance `3*bit_Hamming_distance`.

An underlying general lemma applies to *any* four perfect cubes `A,B,X,Y` satisfying

```
A+2*B=2*X+Y,    A+B/2 <= X <= B-A.
```

It guarantees `P((B-A)*u**3)>=2**(A*u**3-1)`. The example above is concrete and fully explicit; no priority or optimality claim is made about this particular identity.

The independent `audit_three_cycle_identity.py` script checks the four cube constants, all endpoint inequalities, every translated three-cycle at `u=1`, and symbolic identities at larger `u`, without solving any matching problem.

## Optimized entropy: minimal terminal cube

The earlier explicit sequence `n=(551*t**3-1)//2` uses the convenient but nonminimal suffix-reflection cube `(8*t)**3`. We can shrink that redundant suffix to `O(t**2)` by taking the **least integer cube above the middle-block endpoint**.

For every odd integer `t>=9`, put `L=t**3`, take `k_t` minimal with `k_t**3>473*L`, and define

```
N_t = k_t**3 - (473*L+1)//2
P(N_t) >= P((L-1)//2)*512**L >= 3*2**(9*L).
```

Here `N_t = (473/2+o(1))*L`, so the exponential subsequence theorem improves from `18*log(2)/551` to

```
limsup(log(P(n))/n) >= 18*log(2)/473.
```

The fully general d-th-power version yields `limsup(log(P_d(n))/n) >= log(P_d(M))/(M+1/2)` whenever eventual existence and `P_d(M)>1` hold. The proof does **not** assume a universal exponential lower bound for all integers. `optimize_terminal_cube.py` checks exact full permutations for `t=9` (`N=185502`) and `t=11` (`N=321274`) and confirms all independent five-cycle switches.

## Binary permutation code with exact Hamming metric

The 9 independent five-cycle toggles of the `M=236` gadget encode each `9`-bit string as a different valid cube-sum permutation. Each toggled cycle changes exactly five positions, so for binary masks `a,b` the **exact** distance is `Hamming(p_a,p_b)=5*Hamming(a,b)`.

Independent-fiber tensorization produces a map `Phi_t:{0,1}**(9*t**3) -> cube-sum permutations of length n_t=(551*t**3-1)//2` such that

```
Hamming(Phi_t(a), Phi_t(b)) = 5*Hamming(a,b)
sum_a z**Hamming(Phi_t(a),Phi_t(0)) = (1+z**5)**(9*t**3).
```

By elementary greedy packing in the binary Hamming cube, a subfamily has at least `2**(9*t**3*(1-H_2(1/4)))` members whose minimum pairwise permutation Hamming distance exceeds `45*t**3/4`. Thus **both the logarithm of the family size and the minimum pairwise distance grow linearly with n_t**.

This codes-and-distances result is algebraic, not a brute-force search. `audit_permutation_code.py` verifies all 512 base bit masks and exact distance scaling for t=3,5,9.

## General theorem: independent-fiber tensorization

The previous odd-power block lift can be strengthened: **each fiber r=1,...,L can use a different legal base permutation p_r**. For odd `t`, `L=t**d`, `A=(L-1)//2`, and every `i=1,...,M`, define

```
x=A+(i-1)*L+r
Q[x]=A+(p_r[i]-1)*L+(L+1-r)
x+Q[x]=L*(i+p_r[i]).
```

Every constructed sum is a perfect d-th power; each output fiber remains separately bijective. The independent choices inject into the set of legal interval permutations, yielding **exactly `P_d(M)**L` constructed middle-block permutations**, without choosing or enumerating alternating cycles.

For general exponent `d>=2`, assuming eventual existence and just **one length `M` with `P_d(M)>=2`**, choose integer `b` with `b**d>2*M+1` and odd `t` sufficiently large. Then at

```
n_t=(b**d-M-1/2)*t**d-1/2
P_d(n_t) >= P_d((t**d-1)/2) * P_d(M)**(t**d)
limsup_n(log P_d(n)/n) >= log(P_d(M))/(b**d-M-1/2)>0.
```

In the specific cubic `M=236` construction (with `P(236)=512` and `b=8`), this sharpens the finite coefficient to

```
P((551*t**3-1)/2) >= P((t**3-1)/2)*512**(t**3)
                       >= 3*2**(9*t**3)   for odd t>=9.
```

`tensorize_fibers.py` independently checks distinct legal matchings on different fibers, preserves the exact cube sums, and verifies injectivity by changing a single fiber. This theorem is algebraic; the new script is a regression check.

## Exponential growth on an explicit infinite subsequence

This is the strongest purely structural counting improvement in this follow-up. For **every odd integer t>=9** define

```
n_t = (551*t**3 - 1)//2.
```

Then

```
P(n_t) >= 2**(9*t**3) = 2**((18*n_t+9)/551)
limsup(log(P(n))/n) >= 18*log(2)/551 > 0.
```

Unlike the global near-critical bounds, this is **exponential in n**, but only along the explicit infinite subsequence `n_t`. No exponential-in-n lower bound is asserted for every n.

**Odd-power block lifting lemma:** If `p` is a valid `d`th-power-sum permutation of length `M` and `L=t**d` is odd, place `M` consecutive blocks of length `L` inside the shifted interval starting at `A+1`, where `A=(L-1)//2`. For `x=A+(i-1)*L+r`, set

```
Q[x] = A+(p[i]-1)*L+(L+1-r).
x+Q[x] = L*(i+p[i]).
```

All sums remain `d`th powers, and each old alternating cycle becomes **L independent copies**. For the explicit `M=236` seed there are nine independent five-cycles, giving `9*L` switches.

To turn the shifted middle permutation into an ordinary prefix permutation, use the previously proven construction on `[1,A]` and reflect the suffix `[B+1,n_t]` through the cube `(8*t)**3`, where `B=A+236*L`; that suffix has length exactly `39*L`.

Independent integer checks:
```sh
python papers/A006063/lift_exponential_subsequence.py
python papers/A006063/verify_362.py
python papers/A006063/verify_tensor_recurrence.py
python papers/A006063/tensorize_fibers.py
python papers/A006063/audit_permutation_code.py
python papers/A006063/optimize_terminal_cube.py
python papers/A006063/audit_three_cycle_identity.py
python papers/A006063/renormalization.py
python papers/A006063/global_graph_audit.py
```

The default two cases are `t=9, n=200839` and `t=11, n=366690`. They check the full permutations and all `9*t**3` independently switchable cycles. The theorem itself is algebraic and does not rely on these finite tests. The block-lifting lemma generalizes to **every perfect-power exponent d>=2**, conditionally on eventual existence of suitable prefix permutations.

## New: power-divisor counting recurrence and stronger exponential subsequence

Let `P_d(n)` count permutations of `[1,n]` with each `i+p[i]` a perfect `d`th power; adopt `P_d(0)=1`.
For an odd `t` with `L=t**d | (2*n+1)`, define
`A=(L-1)//2`, `q=(2*n+1)//L`, and `M_b=b**d-(q+1)//2`.
Then the **power-divisor tensor recurrence** is

```
P_d(n) >= P_d(A) * sum(P_d(M_b)**L
    for b >= 2 if M_b >= 0 and b**d < q).
```

It simultaneously generalizes ordinary suffix reflection (`t=1`) and the independent-fiber block lift (`t>1`). The contributions for different `b` are **disjoint**, since the last assigned value is `(b*t)**d-n`.

A new **43-interval reflection template** for `n=362` contains **40 pairwise disjoint alternating cycles**, independently certified by [verify_362.py](verify_362.py), with 182 involved vertices and no matching solver. Hence `P(362)>=2**40`. Setting `M=362`, `b=9`, `q=733` gives the improved infinite family

```
N_t = (733*t**3 - 1)//2,  t odd >= 7
P(N_t) >= P((t**3-1)//2) * 2**(40*t**3)
limsup(log(P(n))/n) >= 80*log(2)/733 > 0.0756.
```

This strengthens the earlier `236`-gadget constant `18*log(2)/551` by more than a factor of three, without any new large-scale matching calculations.

**A precise method limitation:** A nontrivial odd cubic scale requires `t**3 | (2*n+1)` for some `t>=3`. By Möbius inclusion-exclusion, those lengths have density only `1 - 8/(7*zeta(3)) = 0.0492487...`. Therefore the centered tensor method, on its own, does **not** establish a uniform exponential-in-`n` lower bound. This is a limitation of this construction, not a no-go result for other ideas.

Artifacts:

- [certificates/forty_cycles_362.json](certificates/forty_cycles_362.json): 43 interval rows and 40 disjoint alternating cycles.
- [verify_362.py](verify_362.py): exact integer, solver-free structural audit.
- [verify_tensor_recurrence.py](verify_tensor_recurrence.py): tests two distinct cube suffixes at fixed `n`, and the new `t=7,9` amplification constructions.

## Mathematical method

**Reflection extension:** If `p` is valid on `{1,...,m}` and `m+n+1=c` is a cube, then extend by `p[i]=c-i` for `m<i<=n`. Each cube gives a disjoint image family since its last value is `p[n]=c-n`. Consequently,

```
P(n) >= sum(P(c-n-1) for cubes c with n+1 <= c <= 2*n)
```

with `P(0)=1` (the empty matching convention).

**Earlier finite certificate compression:** The old standalone archive stores 109 witnesses for `173..255` and `339..364` (not an optimal seed count once the empty permutation is allowed). Every size `256..338` is reflected from `m=511-n`, since `m+n+1=512=8^3`. Thus the earlier 192 base-case witnesses reduce to 109 stored primary witnesses; the original 192-row archive remains available for cross-checking. The elementary cube-gap lemma then reduces all sizes `n>=365` to smaller solved sizes `m>=173`.

**Negative cases:** A subset `S` of left vertices is an obstruction when its cube-sum neighbor set `N(S)` has `|N(S)|<|S|`, by Hall's marriage theorem. This certifies all 124 non-members below 173. At `n=172`, there is an explicit 27-left/26-right Hall obstruction, proving the sharpness of the 173 threshold.

**Multiplicity:** For any valid permutation `p`, a directed edge `i -> j` exists when `i != j` and `i+p[j]` is a cube. A directed cycle gives another valid permutation by rotating right partners along the cycle. The converse also holds: two distinct perfect matchings differ on alternating cycles, so acyclicity certifies uniqueness.

The 190 base lengths `175..364` have **two different** cycle witnesses each; the two additional solutions and the original establish at least three. For `365..553`, reflection through `729` preserves multiplicity; `554,555` have dedicated witnesses, and for `n>=556` the cube-gap bound provides a predecessor `m>=175`. Reflection preserves all three distinct matchings. This constant lower bound is sharp: **`P(175)=3` exactly**, certified by reducing the permanent to a 10-by-10 strongly connected component (165 vertices forced).

**Exponential count:** For `k=floor(cuberoot(2*n))>=27`, the three cubes `k^3,(k-1)^3,(k-2)^3` give disjoint extensions from `m_i>=173`, with `K(m_i)>=k-6`. Strong induction gives `P(n)>=3**q(n)`.

## Constructive algorithm

The new `construct_linear.py` algorithm chooses the **least cube** `c=k^3>=n+174` at each step and reduces to `m=c-n-1=O(n**(2/3))`. This gives **O(log log n) reflection layers** and writes the complete answer in **O(n) unit-cost operations**. Exact integer cube roots avoid floating-point rounding. The default check constructs a permutation for `n=1,000,000` and audits its entries; `--plan 1000000000000000000000000` computes a gigantic instance's block layout without allocating the output.

## Proof artifacts

- [main.tex](main.tex): full paper source; [main.pdf](main.pdf) is produced and committed by the PDF workflow.
- [certificates/core_60_with_empty.json](certificates/core_60_with_empty.json): the **minimal 60-seed** reflection-only basis, reusing the empty permutation and 48 early positives.
- [certificates/core_61_with_small.json](certificates/core_61_with_small.json): historical, slightly redundant 61-seed basis that excluded the empty permutation.
- [certificates/core_109.json](certificates/core_109.json): 109 primary existence witnesses.
- [certificates/base_permutations.json](certificates/base_permutations.json): original independent 192-row audit data.
- [certificates/exact_classification_below_173.json](certificates/exact_classification_below_173.json): 48 valid permutations and 124 Hall-deficient sets.
- [certificates/second_solutions.json](certificates/second_solutions.json): first alternative solution cycles for early multiple cases and all 192 tail-base cases.
- [certificates/third_solutions.json](certificates/third_solutions.json): second distinct alternative cycle for every tail-base case, proving sharp `P(n)>=3`.
- [verify.py](verify.py): audit original 192 base cases and recursive witnesses.
- [independent_match.py](independent_match.py): independent augmenting-path generator for the 192 base cases.
- [construct_linear.py](construct_linear.py): efficient O(n)-output constructor and huge-integer block planner.
- [verify_extended.py](verify_extended.py): audit all new certificates, uniqueness, multiplicity, compact bases, and structural numeric regression tests.

Run, from repository root:

```sh
python papers/A006063/verify.py
python papers/A006063/independent_match.py
python papers/A006063/verify_extended.py
python papers/A006063/construct_linear.py
python papers/A006063/verify_word_paths.py
python papers/A006063/count_236.py
python papers/A006063/lift_exponential_subsequence.py
```

All verifiers use Python's standard library only; certificate checks use integers, sets, and exact comparisons.

## Publication/review boundaries

These are complete mathematical arguments with finite machine-checkable premises, not computational conjectures inferred from a cutoff. However, the work **requires independent review** of the formal lemmas, finite data, and existing literature. We do not claim to have computed exact values of `P(n)` beyond the uniqueness cases, nor to have submitted any OEIS entry or journal manuscript. The draft PR is intentionally not marked ready for review.

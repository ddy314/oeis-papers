# Cube-sum permutation classifications (OEIS A006063, A096680, A096904)

**Date:** 2026-10-18  
**Status:** Complete computer-assisted proof candidate, pending independent audit and literature priority check.

We study the number `P(n)` of permutations `p` of `{1,...,n}` such that every `i+p_i` is a perfect cube. The results are mathematical theorems conditional only on fully explicit finite integer certificates, whose validation is independently reproducible. No OEIS page has yet been changed.

## Results

1. **Exact A006063 membership.** `P(n)>0` for every `n>=173`. The 48 positive lengths below 173 are exactly those listed by OEIS; all 124 negative lengths have explicit Hall-obstruction witnesses. Therefore **`A006063(j)=j+124` for every index `j>=49`**, strengthening the formerly conjectural tail formula (which was stated for indices >=173).
2. **Exact A096680 membership.** `P(173)=P(174)=1`, and `P(n)>=3` for every `n>=175`. Exactly 13 lengths below 173 have multiple valid permutations: `112,115,116,117,119,124,125,126,127,128,129,130,133`. Thus **`A096680(j)=j+161` for every index `j>=14`**.
3. **Quantitative A096904 theorem.** Let `K(n)=floor(cuberoot(2*n))` and `q(n)=max(0,floor((K(n)-27)/6))`. For every `n>=173`,
   
   ```
   P(n) >= 3**q(n)
   ```
   
   so **`log P(n) >= ((2*n)**(1/3) * log(3)/6) - O(1)`**. This is a genuine exponential-in-cube-root lower bound on the number of distinct cube-sum permutations.

## Reduced-computation mathematical proof

The **new primary existence certificate** uses *one* explicitly described involution at `n=173` (only seven symmetric reflection interval blocks), followed by exactly **191 short alternating-path words** for `n=174,...,364`. The words use only the cube-root alphabet `{2,3,4,5,6,7,8}` and contain **1,844 root digits total**, compared with the previous full 192-row archive of 51,552 permutation entries.

The mathematical lemma is simple: a word `r_1 ... r_t` defines a successive path from the newly free left vertex `n` by right edges `v_j=r_j^3-u_{j-1}`; when `v_j<n`, follow the unique old matching edge backwards to its left endpoint, and terminate on the newly free right vertex `n`. If no vertex repeats, flipping this alternating path makes a new perfect matching. Each row can be checked with only short integer cube-sum identities; the checker does not solve a matching problem or read the previous long certificates.

- [certificates/augmenting_cube_words.txt](certificates/augmenting_cube_words.txt): 191 locally checkable 1-digit-root words; 2,947 bytes with comments and indices.
- [certificates/augmenting_words_table.tex](certificates/augmenting_words_table.tex): identical words typeset as a compact self-contained paper appendix.
- [audit_permutation_code.py](audit_permutation_code.py): exact Hamming-distance audit for 512 base masks and independently lifted fiber masks.\n- [tensorize_fibers.py](tensorize_fibers.py): independently validate fiberwise arbitrary base matchings and injectivity.\n- [lift_exponential_subsequence.py](lift_exponential_subsequence.py): exact block-lift audit for n=200839 and n=366690 plus all independent cycles.
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
python papers/A006063/tensorize_fibers.py
python papers/A006063/audit_permutation_code.py
```

The default two cases are `t=9, n=200839` and `t=11, n=366690`. They check the full permutations and all `9*t**3` independently switchable cycles. The theorem itself is algebraic and does not rely on these finite tests. The block-lifting lemma generalizes to **every perfect-power exponent d>=2**, conditionally on eventual existence of suitable prefix permutations.

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

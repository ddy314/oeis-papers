# A006063: 82 arithmetic generators for the entire existence tail

**Status:** explicit finite mathematical proof with a smaller, solver-free
certificate; not a parameter-free construction or a claim about priority.
This note refines, but does not invalidate, the 109-row arithmetic atlas in
`FINITE_INTERVAL_PROOF.md`. The previously separate counting results are
unchanged. The finite base is now self-contained without any external
classification of shorter admissible lengths.

## 1. Two elementary operations

Let `P(n)>0` mean that a permutation `p:[1,n]->[1,n]` satisfies
`i+p(i)=k^3` for some positive integer `k` for every index `i`.

**Endpoint-balance lemma.** For integer breakpoints
`0=b_0<b_1<...<b_t=n` and cubes `c_j=k_j^3`, put
`L_j=c_j-b_j`, `R_j=c_j-b_(j-1)`. If
`1<=L_j<R_j<=n+1`, then the formula
`p(i)=c_j-i` for `b_(j-1)<i<=b_j` gives a legal permutation
if and only if the two **multisets** agree:

```
{1,R_1,...,R_t} = {n+1,L_1,...,L_t}.
```

Indeed, the reflected images are exactly the half-open integer intervals
`[L_j,R_j)`. Equality of the endpoint multisets says that the jump
of their covering multiplicity is `+1` at `1`, `-1` at `n+1`,
and zero elsewhere. Therefore every integer from `1` to `n` is
covered exactly once.

**Cubic suffix-reflection lemma.** Let `0<=m<n`, where `m=0`
denotes the empty permutation. If a legal permutation of length `m`
exists and `m+n+1=k^3`, retain it on `[1,m]` and append
`p(i)=k^3-i` on `[m+1,n]`. The appended images are exactly
`[m+1,n]`, so the resulting permutation is legal. This operation
requires no matching theorem or computational hypothesis.

## 2. Smaller self-contained arithmetic base

[certificates/finite_82_seed_atlas.txt](certificates/finite_82_seed_atlas.txt)
gives **82 explicit boundary-balance identities**, comprising:

- **22 seeds below 173:** `66,82,85,100,103,116,118,119,120,121,122,123,
  125,126,127,129,131,132,150,151,155,156`.
- **60 seeds between 173 and 364:**
  `173,174,175,176,177,179,180,181,182,184,185,188,194,197,198,199,
  200,201,202,203,204,205,206,228,229,231,233,234,235,236,238,
  240,241,243,245,246,247,248,249,250,251,252,253,254,339,341,
  343,344,345,346,347,348,349,350,351,353,354,357,358,363`.

Each row `n b_1:k_1 ... b_t:k_t` means
`c_j=k_j^3` on the interval `(b_(j-1),b_j]`.
These **1,030 intervals** satisfy the exact endpoint-balance
identities above. Several especially long rows have been replaced by
independently verified shorter identities; for example, the seed
`n=206` now has 15 segments, while `n=344` has 12.
The original 109-row atlas used 1,123 intervals, so the new certificate
reduces both independent row count (**109 to 82**) and explicit
interval identities (**1,123 to 1,030**). This is a reduction in
finite casework, not its elimination.

No permutation-array archive is an input to this certificate: every
identity is written out as a short, human-checkable sequence of integers.

## 3. Closure: all lengths from 173 to 364

Take the empty permutation at length `0`, the 82 displayed seeds,
and apply the cubic suffix-reflection lemma in increasing order of
the target length `n`. At each omitted `n<=364`, test whether a
cube `c` among `8,27,64,125,216,343,512` has
`m=c-n-1` already constructed with `0<=m<n`.

The exact closure yields **26 further lengths below 173** (48
constructed positive lengths below 173 in total) and **132 further
lengths in [173,364]**. Thus the 60 directly certified lengths plus
the 132 reflected lengths exhaust all 192 integers in [173,364].
The 132 comprise **49 direct reflections from smaller lengths below
173**, together with **83 reflections from lengths 173..255**, which
cover 256..338 via `m=511-n` and cube `512`.

A representative compression:

```
n = 211:  m=131, c=343, so p(i)=343-i on 132<=i<=211.
n = 340:  m=171, c=512, so p(i)=512-i on 172<=i<=340.
n = 342:  m=0,   c=343, so p(i)=343-i on 1<=i<=342.
```

In particular, length 211 no longer needs its former 53-segment
independent entry. This is an algebraic proof dependency, not a
shorter printout of that entry.

The closure does not presuppose the published list of admissible
lengths below 173: the 48 needed lower lengths are **constructed**
from the 22 printed lower seeds and the empty seed. Likewise,
this note does not assert nonexistence at any smaller lengths.

Every displayed seed is irredundant **within the stated 82-seed
system under strictly growing cubic suffix reflections**: when
processed in increasing order, no seed can be obtained from a
previously constructed shorter length by this one operation.
This is not a claim of a globally minimal basis under arbitrary
permutation constructions.

## 4. Entire infinite tail by an elementary cubic gap inequality

We now show `P(n)>0` for every `n>=365` by strong induction.
Assume the theorem for every integer `173<=m<n`.
Choose the **least integer cube** `c=k^3>=n+174`.
We need `c<=2*n`, which makes
`m=c-n-1` an integer in `[173,n-1]`.

If `365<=n<=555`, then `k=9`, `c=729` and
`729<=2*n`.

For `n>=556`, we have `k>=10`. Since the preceding
cube is strictly below `n+174`, integer arithmetic gives
`n>=(k-1)^3-173`, and hence

```
2*n-k^3 >= 2*(k-1)^3-346-k^3
          = k^3-6*k^2+6*k-348 >= 112 > 0,    k>=10.
```

The last cubic polynomial is `112` at `k=10` and
strictly increases for larger integer `k`, since its
first difference is `3*k^2-9*k+1>0` for `k>=10`.
The suffix-reflection lemma therefore completes the induction.

**Theorem.** The 82 explicitly displayed endpoint-multiset
identities, the empty permutation, and the elementary reflection
and cubic-gap lemmas prove `P(n)>0` for **every `n>=173`**.

## 5. What is checked, and what remains open

`verify_82_seed_proof.py` independently reads **only**
`finite_82_seed_atlas.txt`. It checks exact integer endpoint
multisets, segment bounds, row counts, total interval count, and
strictly increasing cubic-reflection closure through 364.
It does **not** read the older 109-row atlas, a matching certificate,
an OEIS membership file, or any prior permutation archive.

The proof can be checked on paper, row by row, without executing
the script. The script is a reproducibility aid, **not a hidden
computational premise**. The infinite-tail argument is symbolic
and is not outsourced to a numerical check.

**Unresolved:** replacing the 82 explicit rows by a small number
of parameterized constructions that are proved in a case-free
fashion. In particular, an endpoint-multiset *verification lemma*
does not itself generate the rows and should not be conflated with
a uniform analytic existence proof. The absence of a nontrivial
parameter-free base proof is stated explicitly.

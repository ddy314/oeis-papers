# A006063: 57 exceptional identities + six algebraic block families

**Current primary existence proof.** Exactly **57 independently printed
integer boundary-balance identities** (795 reflected blocks) and
**six symbolic input/output block-rearrangement families**
construct 82 independent seed lengths. The six families generate
**25** of those lengths, including the 12-block three-switch,
15-block constrained-switch, and 10-block nested-switch constructions.
The 82 expanded witnesses contain 1,009 blocks in total.

The two elementary lemmas and a completely symbolic cubic-gap
induction prove that every `n>=173` admits a permutation with all
`i+p(i)` perfect cubes. The proof does not require executing a
matching algorithm, checking 191 augmenting words, or reading an
archived permutation array. The retained 60/66/70/74/82/109-row
certificates are optional redundant cross-checks. This remains
an explicit **finite case proof**, not a case-free theorem.

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

## 2. The self-contained finite arithmetic base

The [57 exceptional rows](certificates/finite_57_exceptional_atlas.txt)
are concrete integer endpoint-multiset identities containing **795**
reflected intervals. They are also printed in the paper appendix.
The six universal algebraic block-rearrangement families provide
**25 additional base lengths**:

- [Four-, five-, six-block formulas](PARAMETRIC_BLOCK_TEMPLATES.md):
  `66,85,100,103,119,122,182,254`.
- [Twelve-block three-switch family](BINARY_BLOCK_FAMILY.md):
  `131,132,150,151,155,156,174,175`.
- [Fifteen-block constrained-switch family](FIFTEEN_BLOCK_FAMILY.md):
  `228,229,231,238,240,241`.
- [Ten-block nested-switch family](TEN_BLOCK_FAMILY.md):
  `345,351,357`.

The **82 independently justified seed lengths** are exactly:

**22 lower seeds:**
`66,82,85,100,103,116,118,119,120,121,122,123,125,126,127,129,
131,132,150,151,155,156`.

**60 middle seeds:**
`173,174,175,176,177,179,180,181,182,184,185,188,194,197,198,199,
200,201,202,203,204,205,206,228,229,231,233,234,235,236,238,
240,241,243,245,246,247,248,249,250,251,252,253,254,339,341,
343,344,345,346,347,348,349,350,351,353,354,357,358,363`.

Of the 57 explicitly printed rows, **10** are below 173
and **47** lie between 173 and 364. The other **12 lower** and
**13 middle** seeds arise by the six symbolic template families.
The full 82-row comparison atlas is retained independently
with 1,009 intervals, including the 214 template intervals.

A block-rearrangement family is not a restatement of the
endpoint criterion: for input lengths `ell_j`, output order
`pi`, and input/output prefix lengths `A_j,B_j`, the sums
`C_j=1+A_j+B_j+ell_j` are **symbolically proven cubes** for
each nonempty block. The output intervals automatically partition
`[1,n]`; an empty block imposes no cube condition.

## 3. Closure: all lengths from 173 to 364

Take the empty permutation at length `0`, the 57 exceptional rows
and the 25 symbolic outputs of the six parameter families,
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
from the 22 established lower seeds (10 printed exceptional rows
and 12 symbolic instances) and the empty seed. Likewise,
this note does not assert nonexistence at any smaller lengths.

Every selected seed length is irredundant **within the stated 82-length
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

**Theorem.** The 57 exceptional endpoint-multiset identities,
six algebraic block templates, the empty permutation, and
the elementary suffix reflection and cubic-gap lemmas prove
`P(n)>0` for **every `n>=173`**.

## 5. Verification, limitations, and next mathematical questions

[verify_57_plus_templates.py](verify_57_plus_templates.py) reads
**only the 57 exceptional rows** and regenerates 25 other base
lengths from the six algebraic formulas. It independently checks
all integer endpoint bounds and multisets, every block's cubic sum,
and the increasing finite suffix-reflection closure.

A second, independent reconstruction directly produced
the actual permutations for all **240 covered positive lengths**
(48 below 173 and all 192 lengths in 173..364) and checked
both bijectivity and the cubic-sum property. The older
60/66/70/74/82/109-row certificates remain available for
redundant audits. The **symbolic infinite-tail induction**
is not a computational assumption.

**Unresolved:** There are still **57 individually checked
finite arithmetic identities**. The six parameterized families
explain 25 specific seed lengths but do not establish a
uniform parameter-free proof of the whole middle range.
Neither a minimality statement for 57 nor an independent
peer-review or literature-priority claim is made.

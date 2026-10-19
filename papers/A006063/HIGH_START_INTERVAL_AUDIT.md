# Is A006063's avalanche starting too low? High-start interval analysis

**Status: theorem-level launch mathematics + a clearly labeled finite matching experiment.**
This note investigates whether replacing the difficult finite base
`[173,364]` by a larger, more regular interval leads to a better
*eventual* existence theorem. It does **not** claim an unconditional
case-free proof of the proposed higher base.

## 1. Exact optimal two-cube launch windows (PROVED)

Let `G(n)` mean existence of a cube-sum permutation of `[1,n]`.
The proved interval avalanche says that if `G(n)` holds for every
`n in [a,b]`, then a cube `c` with

```
a+b+2 <= c <= 2*b+2
```

extends existence through `c-a-1`.

**Launch-window theorem.** Fix `k>=6` and plan to propagate first by
`c=k^3` and then by `d=(k+1)^3` without proving any new
lengths between the two reflections. The smallest feasible upper
endpoint is

```
b_k = floor((k^3-1)/2).
```

The largest lower endpoint which guarantees that the first
reflection reaches the threshold for the next cube is

```
a_k = k^3 - 1 - floor(((k+1)^3-1)/2).
```

For the interval `[a_k,b_k]`, both launch conditions hold.
The minimum contiguous base width under this two-stage strategy is

```
w_k = b_k - a_k + 1
    = ((k+1)^3-k^3+1)/2
    = (3*k^2+3*k+2)/2.
```

**Proof.** For the first cube to touch `b+1`,
`k^3<=2b+2` implies `b>=b_k`.
It produces the new upper endpoint `k^3-a-1`.
For the next cube to touch the extended interval,
we must have
`k^3-a-1>=floor(((k+1)^3-1)/2)`,
equivalently `a<=a_k`.
Both constraints are attained simultaneously.
Also `k^3>=a_k+b_k+2` because consecutive
cubes have a positive integer gap.
Thus this interval launches the first two cube reflections.
For subsequent cubes the condition
`(j+1)^3<=2*j^3-2*a_k` only becomes easier:
the right-minus-left quantity
`2*j^3-(j+1)^3` increases for `j>=2`,
since its first difference is
`3*j^2-3*j-5>0`. QED.

Numerical examples (endpoints are exact integers):

| first cube | smallest self-propagating base | base width |
|---|---|---:|
| 9^3=729 | [229,364] | 136 |
| 10^3=1000 | [334,499] | 166 |
| 11^3=1331 | [467,665] | 199 |
| 12^3=1728 | [629,863] | 235 |
| 13^3=2197 | [825,1098] | 274 |
| 16^3=4096 | [1639,2047] | 409 |

**Tradeoff:** The width `w_k` grows approximately as
`1.5*k^2`. Raising the start therefore does *not*
automatically reduce the absolute finite proof size,
but it can improve the graph's combinatorial structure.

## 2. Why [229,364] is not an obvious simplification (PROVED)

The base `[229,364]` is shorter than `[173,364]`,
but if no previously proved lengths below 229 are allowed
(except the empty length 0), strictly increasing cubic
suffix reflection derives only **28** of these 136
lengths from smaller lengths *within the new band*.
The other **108** lengths have no available predecessor
under that restricted rule and need independent construction.

More precisely the 108 ungenerated lengths comprise
the integer ranges `[229,255]`, `[283,341]`,
and `[343,364]`. The missing length 342 itself is
trivially generated from the empty permutation using cube 343.
Thus the 29% width reduction does not remove the need
for many local constructions. Moreover it cannot
establish the skipped lengths `173..228`, which
remain necessary for the full original statement.

## 3. A genuinely more regular band: [467,665]

We found a stronger, rigorously provable structural
feature of `[467,665]`. Let the five permitted cube
sums be

```
C = {216,343,512,729,1000} = {6^3,7^3,8^3,9^3,10^3}.
```

For every `n in [467,665]`, let `H_n`
be the *undirected* cube-sum graph on
`[1,n]`, with `i--j` when `i+j in C`
(loops allowed at even half-cubes).

**Twofold-reflection coverage lemma (PROVED).** Every
vertex of `H_n` has at least **two distinct**
permitted cube-sum neighbors, for all
`467<=n<=665`.

**Proof.** At `n=467`, the reflection
domains of the first four cubes are

```
I_216=[1,215],
I_343=[1,342],
I_512=[45,467],
I_729=[262,467].
```

Each index in `[1,467]` lies in at least two
of these four intervals, by inspecting the
breakpoints `1,45,216,262,343,468`.
Every fixed cube's reflection domain only
expands as n increases. For `467<n<=511`,
each new index `468<=i<=n` has two
distinct valid partners `512-i` and
`729-i`. From `n=512` onward, every
new index `512<=i<=n<=665` has partners
`729-i in [64,217]` and
`1000-i in [335,488]`, both inside
`[1,n]`. Thus no vertex of any
`H_n` in this window is a forced leaf. QED.

This degree condition is *not by itself a
perfect matching theorem* (a graph can have
minimum degree 2 and still fail Tutte/Hall).

## 4. A striking finite observation: 199 five-cube involutions

**COMPUTATIONALLY OBSERVED, NOT YET PROVED WITHOUT CASEWORK.**
An independent maximum-cardinality general-graph matching
search (Edmonds blossom, with NetworkX) produced:

- For every **even** `n in [467,665]` (99 values),
  a fixed-point-free involution `p`, using
  **only** cube sums in `C`.
- For every **odd** `n in [467,665]` (100 values),
  an involution using only `C` and satisfying
  **`p(108)=108`**, since `108+108=216`.
- Thus all 199 lengths passed, using the **same five cubes**.
  The optional reproducibility script is
  [verify_high_start_five_cubes.py](verify_high_start_five_cubes.py).

These finite matching results are useful **experimental
evidence only**. They are not a proof that one general
Tutte inequality holds throughout the interval.

For n=360 and n=362 in the smaller comparison
window [334,499], matching with the five sums
`{64,216,343,512,729}` fails if one
*requires no fixed points*. However both
admit involutions if two fixed points are
allowed. Earlier claims that no involution
existed at those lengths were an error.

### Proposed single mathematical target

Remove the vertex 108 when n is odd, and call
the resulting *loopless* graph `F_n`.
A proof of the following **Tutte condition**, with
no 199-row matching atlas, would be sufficient:

```
For each 467<=n<=665 and each S subset V(F_n),
the number of odd components of F_n-S is <= |S|.
```

By Tutte's 1-factor theorem this implies a
perfect matching of `F_n`. Pair matched
vertices via their corresponding cubic sums;
for odd n, add the fixed point 108.
This establishes a cube-sum involution on
every n in the window by **one structural
matching principle**, not 199 numerical
matching runs.

**Conditional stronger conclusion.** Cubic
suffix reflection preserves involutions,
so the already proved interval avalanche
would then give cube-sum involutions
for **every n>=467**:

```
[467,665] --1331--> [467,863]
          --1728--> [467,1260] --2197--> ...
```

The first step follows because
`467+665+2=1134<=1331<=1332=2*665+2`.
The rest is guaranteed by the same
symbolic monotone cube-gap inequality
as in Section 1.

## 5. What moving the start can and cannot solve

**Yes:** The high window replaces many
complicated small-degree graph instances
by a regular five-cube, minimum-degree-two
involution problem, with the *same fixed point*
108 for all odd n. This is a much sharper
and more promising combinatorial statement
than arbitrary permutation existence.

**No:** Even a complete case-free proof of
the high-window Tutte condition would only
settle all `n>=467`. It would not by itself
prove the original `173<=n<=466` part.
The original finite parameter choices are
not logically removed just by raising the
starting length. A final global proof would
need a separate low-range reduction, or a
new downward/gluing theorem.

**Research verdict:** Keep [467,665] as the
main exploratory target for a generalized
five-reflection Tutte construction. Retain
[229,364] as the width-minimizing alternative,
but do not assume it is easier to prove.

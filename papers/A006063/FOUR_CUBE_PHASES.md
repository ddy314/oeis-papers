# Three four-cube phases for the [467,665] high-start problem

**Research status: completely checked finite experiments; a uniform
non-computational matching proof remains OPEN.**

The original five-cube high-start experiment found involutions
for all 199 lengths using sums
`{216,343,512,729,1000}`.
A more restrictive reanalysis shows that **no individual
length requires all five cube sums to obtain an involution**.
Three **four-cube palettes** suffice, with a uniform
fixed-point rule for each phase.

## 1. The three-phase four-cube statement

Let `P_C(n)` denote existence of an involution
`p:[1,n]->[1,n]` such that all `i+p(i)` belong
to a specified set of integer cubes `C`.

**Proposed four-cube phase theorem (experimentally verified):**

| length n | four allowed cubic sums | fixed points |
|---|---|---|
| 467 through 560 | 216,343,512,729 | none if even; exactly 108 if odd |
| 561 through 579 | 216,512,729,1000 | none if even; exactly 108 if odd |
| 580 through 665 | 343,512,729,1000 | none if even; exactly 256 if odd (500 also works) |

These three phases comprise 94, 19 and 86
lengths respectively, totaling 199.

Every one of these cases was found and checked
by an independent **general-graph Edmonds-blossom
maximum-matching computation** (not merely a
bipartite permanent/permutation check).
The experimental audit is in
[verify_high_start_four_color_phases.py](verify_high_start_four_color_phases.py).

**Not yet proved:** A single theorem establishing
all three intervals without 199 separate
matching computations. Therefore the proposed
phase theorem is **not a certified
computation-free result**.

## 2. Correct cubic fixed points for each palette

An involution with a single fixed point f must satisfy
`2*f in C`. This is a **necessary arithmetic constraint
before any graph-matching argument**.

- Phases I and II include 216, so the odd-n fixed
  point **108** is valid.
- Phase III omits 216. Its only permitted fixed points
  from even cubes are **256** (sum 512) and
  **500** (sum 1000). In particular **108 is forbidden
  at every odd Phase III length**, not only 581.
- Independent full-band general-graph matching
  checks find an involution at every odd n in
  581..665, **with either 256 or 500 as the
  sole fixed point**. Even n admit no fixed points.

**Correction to the earlier research log:** The previous
statement that Phase III could fix 108 at all odd
lengths except 581 was false. It omitted the
elementary requirement `2*f in C` and its
corresponding experimental verifier failed its
own fixed-point check. Both the verifier and the
phase theorem have now been corrected.

### A separate, stronger hybrid Tutte barrier at 581

The [31-interval Tutte certificate](TUTTE_OBSTRUCTION_581.md)
still proves a mathematically meaningful but
different assertion: if the fifth cube 216
were admitted **solely for the fixed point 108**
and every nontrivial 2-cycle were restricted to
the four cubes `{343,512,729,1000}`, then
n=581 would remain impossible. Deleting 108
and a 103-vertex set leaves 105 odd components.
Therefore any five-cube involution at 581 fixing
108 must also use cube 216 in **at least one
nontrivial 2-cycle**. This is an auxiliary
five-color restriction, not a four-color
fixed-point exception.

## 3. Why the phase structure is mathematically useful

The three palettes overlap and differ
by replacing exactly one reflection:

```
Phase I:   {216,343,512,729}        (without 1000)
Phase II:  {216,512,729,1000}       (without 343)
Phase III: {343,512,729,1000}       (without 216)
```

Each phase can be attacked using **one
four-reflection graph**, instead of
requiring all five reflections at
every n. The short middle phase
561..579 is only 19 lengths long.

The symbolic [193-path quotient theorem](ODD_CUBE_PATH_QUOTIENT.md)
applies particularly to Phases I and III,
which both retain the odd reflections
343 and 729. In those phases, the
remaining two **even** reflections
must satisfy the path-local state
constraints of the finite-state
gadget theorem. Phase II uses a
different underlying odd-cube
skeleton, with 729 as its sole
odd reflection; proving it may
require a different local reduction.

A future proof may therefore split
naturally into three shorter structural
lemmas, rather than one large
five-reflection Tutte criterion.

**Subtlety:** No single one of these three four-cube palettes
covers all 199 lengths under the proposed fixed-point rule.
The previously established Hall
certificates show that *every cube in
the five-cube union* is indispensable
to that **uniform palette**; this is
fully compatible with each n using
some four-cube subset *depending on n*.

### Exact initial forced-edge regimes (PROVED)

A separate [four-cube boundary-forcing theorem](FOUR_CUBE_BOUNDARY_FORCING.md)
classifies every **degree-one vertex** in all three
palette phases. In Phase I at 512<=n<=560,
the full suffix [512,n] must be reflected under
sum 729; at odd n, 404<->325 is also forced.
Phase II always begins with exactly two forced
edges: 256<->473 plus either 108<->404 (even)
or 404<->325 (odd). In Phase III, even n
have no initial degree-one vertices; with
fixed point 256, odd n force 87<->425
through n=641 and have no initial leaves
from n=643 onward.

All of this is proved by reflection-domain
arithmetic and checked by
[verify_four_cube_boundary_forcing.py](verify_four_cube_boundary_forcing.py)
without using any matching solver. These
are **necessary local assignments**, not
a phase-wide positive existence theorem.

## 4. Two-seed path ladders and the exact augmentation lemma

**Elementary alternating-path flip lemma (PROVED).**
Suppose an even-vertex subset has a perfect
matching M. Add two new vertices x,y.
Suppose the augmented graph admits a
simple path from x to y with edges
alternating **outside M / inside M /
outside M / ... / outside M**.
Then toggling the edge membership
along that path produces a perfect
matching of the augmented graph.

**Proof.** Every internal vertex has
exactly one incident path edge in M
and exactly one path edge outside M;
the toggle exchanges those choices.
Both unmatched endpoints x,y gain one
matching edge. No other matching
edge changes. QED.

This lemma preserves the cube-sum condition
if every path edge is permitted by its
cube sum. For odd n, removing the
chosen fixed point before applying the
lemma also preserves its single
fixed point upon extending n to n+2.

An optional two-seed experiment,
[verify_high_start_two_seed_ladder.py](verify_high_start_two_seed_ladder.py),
uses the full five-color palette,
finds initial matchings at n=467 and
468, and then performs *only*
alternating-path flips:

```
467 -> 469 -> ... -> 665   (99 verified transitions)
468 -> 470 -> ... -> 664   (98 verified transitions)
```

The largest observed alternating path
uses 47 edges on the odd ladder and
45 edges on the even ladder. This
reproduces 199 involutions with only
**two initial general-matching searches**,
but the path existence at all 197
steps is **still computationally checked,
not proved by a general expansion lemma**.
Moreover it uses five colors, so it
is independent of the pointwise
four-color phase observation.

## 5. Revised research target

The right next step is no longer
`prove one five-cube Tutte theorem over 199 lengths`.

It is more precise to ask for:

1. A uniform four-reflection matching
   argument over **467..560**, palette
   `{216,343,512,729}`.
2. A second, possibly shorter theorem
   for **561..579**, palette
   `{216,512,729,1000}`.
3. A third matching theorem for
   **580..665**, palette
   `{343,512,729,1000}`, allowing
   fixed point **256 at 581**.

All three are currently supported
by computation, not completed
symbolic matching arguments.
Proving them without numeric case
lists would yield the stronger
existence statement that every
`n>=467` has a cube-sum involution,
after applying the already proved
cubic suffix interval avalanche.
The lower range `173..466` still
requires a separate argument.

The prior mathematical theorems on
unimodular determinant shapes,
forced leaf peeling and the
infinite avalanche are unaffected.

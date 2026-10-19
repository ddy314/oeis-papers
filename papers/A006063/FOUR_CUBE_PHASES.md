# Three four-cube phases for the [467,665] high-start problem

**Research status: completely checked finite experiments; a uniform
non-computational matching proof remains OPEN.**

The original five-cube high-start experiment found involutions
for all 199 lengths using sums
`{216,343,512,729,1000}`.
A more restrictive reanalysis shows that **no individual
length requires all five cube sums to obtain an involution**.
Three **four-cube palettes** suffice, with a single
exception to the *fixed-point-108 convention*.

## 1. The three-phase four-cube statement

Let `P_C(n)` denote existence of an involution
`p:[1,n]->[1,n]` such that all `i+p(i)` belong
to a specified set of integer cubes `C`.

**Proposed four-cube phase theorem (experimentally verified):**

| length n | four allowed cubic sums | fixed points |
|---|---|---|
| 467 through 560 | 216,343,512,729 | none if even; exactly 108 if odd |
| 561 through 579 | 216,512,729,1000 | none if even; exactly 108 if odd |
| 580 through 665 | 343,512,729,1000 | none if even; exactly 108 if odd, **except 581** |
| 581 | 343,512,729,1000 | exactly 256 |

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

## 2. The apparent critical n=581 is a fixed-point artifact

At odd n, a cube-sum involution must have
an odd number of fixed points. When only
these cube sums are permitted, potential
fixed points are the halves of the
available **even** cubes:

```
216/2=108,  512/2=256,  1000/2=500.
```

The original experiment fixed 108 at
all odd lengths. Under this *additional*
constraint, n=581 was the sole length in
this phase decomposition for which
no four-cube palette worked.

At n=581, if 216 is omitted, the
remaining four cubes
`{343,512,729,1000}`
still allow an involution, provided
its unique fixed point is **256**
(or alternatively 500, as another
independent matching check shows).
Indeed `2*256=512` is cubic.

Thus it would be **false** to claim
that n=581 intrinsically requires all
five colors for a cube-sum involution.
It only requires them under the extra
`p(108)=108` normalization used in
the first search. The corrected statement
above removes that unnecessary restriction.

### Exact Tutte barrier for the excluded fixed point (PROVED)

The failure of the four-cube involution at n=581 with
**sole fixed point 108** is now a pure mathematical
theorem, not merely a blossom solver result.
See [TUTTE_OBSTRUCTION_581.md](TUTTE_OBSTRUCTION_581.md).

After deleting 108, remove an explicit union of
**31 integer intervals containing 103 vertices**.
The remaining graph with sums `343,512,729,1000`
splits into **105 odd connected components**:
60 singletons, 18 triples, 13 5-vertex,
2 7-vertex, 7 11-vertex, 3 17-vertex,
one 63-vertex and one 93-vertex component.
Thus `o(G-S)=105>|S|=103` violates
Tutte's 1-factor theorem. The component count
can be checked using only integer reflection
arithmetic; [verify_tutte_581.py](verify_tutte_581.py)
does this without any matching solver.

**Scope:** This excludes a four-cube *involution*
with only fixed point 108. It does not rule out
general cube-sum permutations or involutions
whose fixed point is 256 or 500. Existence
with those alternative fixed points remains
verified by matching computation, not
established by the negative certificate.

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

**Subtlety:** A single set of four cubes
does not cover all 199 lengths.
The previously established Hall
certificates show that *every cube in
the five-cube union* is indispensable
to that **uniform palette**; this is
fully compatible with each n using
some four-cube subset *depending on n*.

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

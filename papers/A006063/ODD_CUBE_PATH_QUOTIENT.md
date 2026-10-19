# The 193-path quotient theorem for the five-cube high interval

**Status: all main statements below are PROVED by interval arithmetic.**
This note advances the [467,665] five-cube involution question
without claiming a case-free five-cube perfect matching.
It explains both the structure of the two odd-cube reflections
and why a tiny, local patch of their partial matching cannot work.

## 1. Exact decomposition into 193 short paths

For an integer `467<=n<=665`, let `G_n^odd` be the
undirected graph on `[1,n]` with edges of the two
permitted forms

```
i + j = 343 or 729.
```

**Theorem (193-path decomposition).** Exactly **193** connected
components occur. More precisely, there are:

* **171 components indexed by x=1,...,171**, with vertex sets

  ```
  C_x(n) = {x,343-x}
           union ({386+x} if 386+x<=n)
           union ({729-x} if 729-x<=n).
  ```

* **22 further two-vertex components**, indexed by
  `j=343,...,364`, with vertex sets `{j,729-j}`.

Each component is a simple path on **2, 3, or 4 vertices**.
There are no cycles, and components never merge as n increases
within this band.

**Proof.** The 171 pairs `{x,343-x}` partition
`[1,342]`. The 22 pairs `{j,729-j}` partition
`[343,386]`. Thus the initial interval `[1,386]`
is matched by precisely 193 disjoint reflected edges.
Every subsequent integer `i in [387,n]` satisfies
`343-i<0` and `729-i in [64,342]`. Hence it
has **exactly one odd-color neighbor**, in the original
171 base pairs; it cannot connect two different base
components. Each base vertex has at most one new neighbor,
because `i+j=729` uniquely determines i from j.
Thus the 171 expanded components are paths of length at
most three edges, and the remaining 22 stay as isolated
2-vertex paths. QED.

The appearance of **386** is not a numerical accident:
the composition of the two reflection maps is
`R_729 R_343(i)=i+386`.

## 2. Exact path-size counts for all 199 lengths

Let `N_s(n)` be the number of size-s components of
`G_n^odd`. These counts admit **closed formulas**.

**Corollary (all component counts).**

For `467<=n<=557`:

```
N_2(n)=579-n,    N_3(n)=n-386,    N_4(n)=0.
```

For `558<=n<=665`:

```
N_2(n)=22,       N_3(n)=728-n,    N_4(n)=n-557.
```

**Proof.** In component `C_x`, the first optional
leaf `386+x` occurs precisely when `x<=n-386`;
the second optional leaf `729-x` occurs when
`x>=729-n`. Until n=557 only the first optional
leaf occurs. From n=558 onwards every x=1,...,171
has its first leaf, and exactly `n-557` of these
components also have the second. The 22 special pairs
are always size two. QED.

Since a path of s vertices has a maximum matching of
size `floor(s/2)`, the odd-color graph's **exact
maximum-matching deficiency** is

```
d_odd(n) = N_3(n)
          = n-386  (467<=n<=557)
          = 728-n  (558<=n<=665).
```

This formula is symbolic and contains no matching
algorithm, Hall certificate or numerical atlas.

## 3. Fixed point 108 and the even-edge lower bound

The experimental five-cube involutions have **no fixed
point for even n** and have **the sole fixed point 108
for odd n**. To study precisely this family, put

```
V_n = [1,n] \ ({108} if n is odd else empty).
```

Define `q(n)` as the number of odd-vertex components
of the graph induced by the **two odd cubes 343,729**
on `V_n`.

**Corollary (exact parity-component defect).**

If n is even, `q(n)=d_odd(n)`.

If n is odd:

```
q(n) = d_odd(n)+1  for 467<=n<=493;
q(n) = d_odd(n)-1  for 495<=n<=619;
q(n) = d_odd(n)+1  for 621<=n<=665.
```

**Proof.** In the 171-path decomposition, the only
component affected by removing 108 is `C_108`.
It initially consists of `{108,235}`. It acquires
a leaf at `494=386+108` and a second leaf at
`621=729-108`.

- Before n=494, deleting 108 turns the 2-path
  into one isolated vertex 235, adding one odd
  component.
- From 494 to 620, deleting 108 turns the 3-path
  `108--235--494` into the 2-path `235--494`,
  eliminating one odd component.
- From 621 onwards, deleting 108 turns the 4-path
  `621--108--235--494` into the 2-path
  `235--494` plus isolated vertex 621, adding
  one odd component.

All other components are unchanged. QED.

**Even-cube resource theorem.** Let p be any
fixed-point-free cube-sum involution on `V_n`
using the full five-cube palette
`{216,343,512,729,1000}`. Then **at least
`q(n)/2` of its 2-cycles** must have even
cube sum, i.e. sum in `{216,512,1000}`.

**Proof.** Every odd-cardinality component
of the two-odd-cube subgraph must be incident
to at least one matching edge that leaves that
component. Otherwise matching edges internal
to this component would cover an odd number
of vertices, which is impossible. Any edge
leaving such a component must have an *even*
cube sum because the odd-cube edges define
the components. Each even-cube edge can
supply boundary incidence to at most **two**
odd components. Thus their number is at least
`q(n)/2`. QED.

This yields a sharp structural warning for
a proposed "few-edge local repair":
at **n=556,557,558**, the formula gives
`q(n)=170`, so **at least 85 even-cube
2-cycles are indispensable** for the
uniform involution pattern. Across the
entire high band `q(n)>=64`, so at least
32 such 2-cycles are always necessary.

These bounds do not contradict the observed
existence of involutions; they show that
repairing the two odd-cube skeleton is
necessarily a **macroscopic rearrangement**,
not a constant-size local gadget.

## 4. Why a one-bridge-per-odd-component quotient fails

An initially attractive scheme would internally match
all 2- and 4-vertex odd-cube paths and, for each
3-vertex path, leave exactly one endpoint exposed.
One could then pair exposed endpoints from *different*
odd paths with edges of even cube sum.

This naive quotient scheme **fails**, even though
the full five-cube matching exists experimentally.
For example, at n=467, the 3-vertex component

```
C_1 = {1,342,387}
```

has permissible exposed endpoints `1,387`
under its internal odd-color matching.
No exposed endpoint of **another odd component**
forms a permitted even-cube edge with these endpoints:

```
216-1=215, 512-1=511, 1000-1=999;
216-387<1, 512-387=125, 1000-387=613.
```

Among these only 215 and 125 are in `[1,467]`,
but they lie in even-sized base components or
are interior vertices, not exposable endpoints
of odd 3-path components. Hence the naive
odd-component quotient has an isolated vertex.

**Consequence.** A correct uniform five-color
matching construction must sometimes modify
**even-size odd-cube path components**, rather than
merely pairing one exposed endpoint per odd path.
This is an exact combinatorial obstruction to the
most natural small-component reduction; it is
not an obstruction to a perfect matching in the
original five-cube graph.

## 5. Status and next mathematical target

This theorem provides a **complete parameterized
decomposition of all 199 odd-reflection skeletons
and an exact lower bound on the even-reflection
matching budget**. No finite matching computation
is a premise of these results.

A possible successful proof of the [467,665]
five-cube involution conjecture must control
how the even-cube reflections connect and
reconfigure the 193 small components. In
particular, proving minimum degree two or
pairing only the odd-size components is
insufficient.

A separate, clearly experimental analysis
finds alternating augmenting paths from an
involution of length n to one of length n+2
through the full palette. Their observed
lengths are not uniformly tiny; the path
existence still needs a non-computational
lemma. Such an extension lemma would give a
different route to the full high-band theorem.

The high-band claim **remains computationally
supported but not yet proved case-free**.

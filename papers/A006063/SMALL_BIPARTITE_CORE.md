# A006063: the four-color graphs are bipartite after only 10–16 edge deletions

**Status: PROVED by three finite, explicit edge-deletion certificates.
This is a new structural theorem, not a complete matching-existence theorem.**

Throughout, graph vertices are integers in `[1,n]`.
Distinct vertices `i,j` are connected if `i+j`
belongs to the relevant four-cube palette. Any permitted
fixed point is deleted *after* forming this graph.

## 1. Uniform 14/10/16 bipartization

**Theorem (bounded nonbipartite core).** For every
`n` in each of the following intervals, remove from
the four-cube graph every edge in the indicated
phase-specific finite set `D` whose endpoints are
present. The resulting graph is bipartite.

| length interval | four cube sums | |D| |
|---|---|---:|
| 467..560 | 216,343,512,729 | **14** |
| 561..579 | 216,512,729,1000 | **10** |
| 580..665 | 343,512,729,1000 | **16** |

The three edge-deletion certificates are **independent
of n within each interval**:

```
Phase I, D_560 (14 edges):
(166,177), (98,118), (70,146), (149,194),
(101,115), (163,180), (84,132), (60,156),
(139,204), (91,125), (170,173), (94,122),
(142,201), (63,280).

Phase II, D_579 (10 edges):
(29,483), (24,192), (453,547), (197,532),
(39,473), (66,150), (17,199), (180,549),
(490,510), (431,569).

Phase III, D_665 (16 edges):
(358,371), (460,540), (221,508), (339,390),
(224,288), (457,543), (355,374), (205,524),
(280,449), (347,382), (213,516), (468,532),
(363,366), (465,535), (216,296), (181,331).
```

Every displayed edge has one of the specified cube
sums; no two endpoints are equal.

**Proof.** At the three maximum lengths
`N=560,579,665`, delete the listed finite sets
`D_N`. Each remaining graph admits a proper
2-coloring; this is an exact finite integer
certificate, reproducible by the deterministic
breadth-first parity propagation described below,
which checks the color of *every surviving edge*
using the four arithmetic reflection formulas.

For an arbitrary smaller n in the same phase,
its graph is the induced subgraph of the maximum
graph on `[1,n]`. Restricting the same proper
2-coloring to these vertices proves the theorem
for all n simultaneously. Deleting an allowed
fixed vertex preserves bipartiteness. QED.

This is only **three bounded finite checks**;
it is not an independent graph search for
every one of the 199 lengths.

## 2. A sharp dual interpretation using the four odd faces

The [uniform planar rotation theorem](THREE_ROTATION_PLANARITY.md)
has exactly **four odd faces** at each maximum
length. Label these odd faces `f1,f2,f3,f4`
in any fixed order.

To make a connected plane graph bipartite,
it is necessary and sufficient to delete
primal edges whose associated **dual edges**
form a `T`-join with odd dual-degree at
exactly these four odd faces. Equivalently,
the deletion merges the four odd faces in
pairs along dual paths; all remaining face
boundaries then have even length.

For four odd faces, the shortest `T`-join
has size equal to the minimum over the
three pairings of four terminals of the
sum of the corresponding unweighted dual
shortest-path lengths.

The three pairwise-distance sums, listed
in **increasing order** (independent of
how the four odd faces are labeled), are
reproduced by
[verify_small_bipartite_core.py](verify_small_bipartite_core.py):

| maximum n | smallest pairing | middle pairing | largest pairing |
|---|---:|---:|---:|
| 560 | **14** | 15 | 21 |
| 579 | **10** | 13 | 16 |
| 665 | **16** | 18 | 24 |

The three edge sets above realize the minimum
values **14,10,16**. Hence these are the
*minimum numbers of edges which must be
deleted to make the respective **maximum
graphs** bipartite*, not just ad hoc
upper bounds.

**Proof of the dual criterion.** A connected
plane graph is bipartite iff every face
boundary walk is of even length. Deleting
a primal edge merges its two incident
faces; in the dual this toggles the
parity of the endpoints of the
corresponding dual edge. Therefore
the chosen deleted edges must have odd
dual degree at precisely the original
odd faces and even degree elsewhere.
Such a set is a `T`-join. A minimum
nonnegative-weight `T`-join for four
terminals is the minimum of the three
pairings of shortest dual paths. QED.

Note that **optimality is claimed only
for the three maximum graphs**. The
minimum number of deletions for a
smaller induced graph may be lower.

## 3. The exact bounded-deviation Hall reduction

Let `G` be one of the (optionally
fixed-point-deleted) four-cube graphs,
and let `D` be its subset of surviving
listed exceptional edges. Put
`B=G-D`. By Theorem 1, B is bipartite.

**Theorem (necessary and sufficient bounded
exceptional-edge test).** The graph G has
a perfect matching **if and only if**
there exists a set `Q subset D` such
that

1. `Q` is itself a matching (its
   endpoints are all distinct);
2. the bipartite graph `B - endpoints(Q)`
   has a perfect matching.

The latter is exactly the ordinary
bipartite **Hall condition** on each
component of B after the endpoints
of Q have been deleted.

**Proof.** Given a perfect matching
M of G, take `Q=M intersect D`.
The other matching edges are wholly
inside B and cover every vertex not
incident to Q. Conversely, any
perfect matching of `B-endpoints(Q)`
can be united with Q to obtain
a perfect matching of G. QED.

Thus a full existence theorem could be
proved by selecting from **at most
14, 10 or 16 exceptional edges** and
establishing a structured bipartite
Hall condition on the remaining graph.
The number of possible subsets is
bounded above by `2^16=65536`,
**independently of n**. This is a
structural finite branching bound,
not a claim that enumerating branches
would be a computer-free proof.

## 4. Why the reduction is promising but not complete

The complete four-color graph is planar
and of maximum degree four; its entire
obstruction to bipartiteness is
confined to 10–16 explicitly identified
edges. This is much stronger than
planarity and complements the two
193/245-path decompositions.

The **crucial missing theorem** is
to choose Q *uniformly in n* and
prove Hall for the resulting
bipartite remainder. Plain
bipartiteness and planar minimum degree
do **not** imply a perfect matching.

An exploratory maximum bipartite-matching
audit found that the bipartite backbone
may have a small deficiency (at most
three matched pairs short throughout
the three proposed ranges), but this
is **not proved by the present
certificate** and is not used as a
logical premise.

The optional [independent integer-only
certificate checker](verify_small_bipartite_core.py)
reconstructs the three graphs using
only arithmetic cube reflections,
verifies all deleted edge colors,
computes the canonical rotation
faces and the four-face dual distance
sums, checks proper bipartite coloring
at the three maxima, and verifies
inheritance by induced subgraphs.
It does not call an external
matching solver.

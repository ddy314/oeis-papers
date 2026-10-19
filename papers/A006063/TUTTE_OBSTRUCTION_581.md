# A direct Tutte obstruction at n=581 when the fixed point is 108

**PROVED: the four-cube palette `{343,512,729,1000}` cannot
support a cube-sum involution on `[1,581]` whose only fixed point
is 108.** The proof uses a small explicitly defined set of
integer intervals, reflection arithmetic, and Tutte's 1-factor
theorem, not a general-graph matching algorithm.

This explains why the proposed four-cube phase construction
at n=581 changes the lone fixed point to 256 (or 500).
Those positive existence claims remain separately supported
by computation, not by this negative theorem.

## 1. The graph and its 31-interval obstruction set

Remove vertex 108 from `[1,581]`. On the remaining
580 vertices, define an **undirected, loopless** graph G
by placing an edge between distinct x,y exactly when

```
x+y in {343,512,729,1000}.
```

Let S be the union of these **31 closed integer intervals**:

```
[148,151], {156}, [161,162], [165,167], {170},
[174,175], [179,180], [184,186], [203,204],
[209,210], [215,217], [263,271], [276,277],
[281,282], [286,287], [298,301], [305,306],
[311,320], [324,325], [329,330], [334,336],
[432,441], [445,446], [450,451], [455,457],
[467,470], [474,475], [480,489], [493,494],
[498,499], [503,505].
```

The intervals are disjoint, none contains 108, and
their lengths sum to exactly

```
|S| = 103.
```

## 2. All remaining connected components are odd

Direct interval/reflection arithmetic for the four maps
`x -> 343-x, 512-x, 729-x, 1000-x`, restricted to

```
T = [1,581] \ ({108} union S),
```

gives the following **complete component-size table**:

| component size | number of components | covered vertices |
|---:|---:|---:|
| 1 | 60 | 60 |
| 3 | 18 | 54 |
| 5 | 13 | 65 |
| 7 | 2 | 14 |
| 11 | 7 | 77 |
| 17 | 3 | 51 |
| 63 | 1 | 63 |
| 93 | 1 | 93 |
| **Total** | **105** | **477** |

The total number of surviving vertices is indeed
`581-1-103=477`. All eight possible component
sizes shown are **odd**.

For a self-contained integer check of this table,
take any vertex `v in T` and repeatedly include
`c-v in T` for each of the four cubes c. Repeat
to closure. That constructs **exactly the
connected component** of v; remove it and
continue with the smallest remaining vertex.
This algorithm is only the definition of
connected components, not a matching solver.
An independent short [standard-library verifier](verify_tutte_581.py)
reproduces all sizes from the 31 displayed
intervals, without NetworkX, SciPy, optimization
or any archived cube-sum permutations.

## 3. Tutte's theorem rules out the fixed-108 involution

Tutte's 1-factor theorem states that a finite
loopless undirected graph H has a perfect
matching if and only if **for every**
`S subset V(H)`, the number `o(H-S)`
of odd-order components is at most `|S|`.

For our explicit S,

```
o(G-S) = 105 > 103 = |S|.
```

Consequently G **has no perfect matching**.

A cube-sum involution on `[1,581]` with
exactly one fixed point at 108 would restrict
to a perfect matching on G: its 2-cycles are
undirected edges of G and they cover all
other vertices. This contradicts Tutte.
Therefore no such involution exists. QED.

The obstruction is *not* a bipartite Hall
obstruction for ordinary permutations:
the corresponding directed cube-sum
adjacency matrix can still support a
complete cycle cover, which may include
cycles longer than two. It also does
not rule out an involution with fixed point
256 or 500, since deleting a different
fixed vertex produces a different graph.

## 4. Consequences for the high-start proof strategy

The proposed palette for Phase III is
`{343,512,729,1000}`. An auxiliary
matching experiment finds a valid
involution at n=581 with only fixed point
256; by contrast, the theorem above
**rigorously proves that keeping 108 as
the sole fixed point is impossible**.

Thus the change of fixed point is not
merely a normalization preference:
under the specified Phase III palette,
the proposed fixed-108 normalization
has a concrete Tutte barrier.

This is a **negative structural theorem**,
not a uniform proof of the three four-color
existence phases. It sharpens the
boundary condition for any future
case-free construction on [580,665].

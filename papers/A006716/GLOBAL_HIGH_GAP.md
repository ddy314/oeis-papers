# A006716: a new universal upper-to-lower zero-gap lemma

**Research note, 2026-10-22.** Qichao Wang (Hebei University of Technology); Daoyu Dong (University of Electronic Science and Technology of China). A necessary condition for true ordinary integer squares, independent of modular tests or fixed support. This does not settle the A006716 finiteness conjecture; literature novelty is not claimed.

## Theorem (upper-span gap restriction)

Let `x` be a positive integer with `x^2` having **no zero decimal digit**. Write the nonzero root positions in decreasing order as

```
e_1 > e_2 > ... > e_r >= 0,  r>=3.
```

For **every** `2<=j<r`,

\[
\boxed{e_j-e_{j+1}\ \le\ e_1-e_j+3.}
\]

Furthermore, if the highest nonzero root digit is one of `1,2,3`, the improved inequality holds:

\[
\boxed{e_j-e_{j+1}\ \le\ e_1-e_j+2.}
\]

These bounds hold for **any zero-free square**; they do not use the stronger restriction that its digits belong to `{1,4,9}`.

### Proof

Fix a split directly after position `q=e_j`, and put `s=e_{j+1}<q` and `e=e_1>q`. Write

```
x = H+L,
H = sum of the root digits at positions >=q,
L = sum of all lower digits.
```

Because q is the lowest occupied position of H, `H^2` is divisible by `10^(2q)`. Furthermore

```
0<H<10^(e+1),  0<L<10^(s+1).
```

Hence

\[
0<2HL+L^2<2\cdot10^{e+s+2}+10^{2s+2}.
\]

Suppose `q-s >= e-q+4`. Then `e+s<=2q-4`, and in particular `s<=q-4`. It follows that

\[
2HL+L^2 < 2\cdot10^{2q-2}+10^{2q-6}
       =0.020001\cdot10^{2q}
       <10^{2q-1}.
\]

As `x^2=H^2+(2HL+L^2)` and `10^(2q)|H^2`, the decimal digit of `x^2` at position `2q-1` must be zero. Contradiction. Therefore `q-s<=e-q+3`.

For the refinement, suppose the leading nonzero decimal digit is `a<=3`. Then `H<(a+1)10^e<=4*10^e`, and

\[
2HL+L^2<8\cdot10^{e+s+1}+10^{2s+2}.
\]

If `q-s >= e-q+3`, then `e+s<=2q-3`, and `s<=q-3`. Consequently

\[
2HL+L^2 <8\cdot10^{2q-2}+10^{2q-4}
       =0.0801\cdot10^{2q}<10^{2q-1},
\]

again forcing a zero in the square at `2q-1`. Therefore `q-s<=e-q+2`. QED.

## Corollary: new fourth-highest-digit bound

For an A006716 root with top four nonzero positions `e>p>q>s`, set `g=e-p`, `h=p-q` and `t=q-s`. Then

\[
\boxed{t\le g+h+3.}
\]

If the leading nonzero root digit is `1,2,3`, then `t<=g+h+2`.

The [previous top-three theorem](SUPPORT15_TOP_THREE.md) limits `(g,h)` to

```
(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,1).
```

Thus **the fourth gap `t` is at most 9**, since the maximum allowed `g+h` is 6. This new restriction is valid for *every* A006716 square with at least four nonzero root digits, no matter how long the root is.

It is stronger than imposing the older low-position gap bound alone, and can be implemented as a provably sound additional prune in support-17 and later exact searches.

## Reproduction and boundaries

The argument above is an elementary inequality proof, so no calculation is required for its infinite-range validity. [verify_high_gap.py](verify_high_gap.py) independently checks the claimed forbidden square-digit position for thousands of constructed splittings and all small A006716 roots. This test is auxiliary evidence, not the proof.

The theorem **does not prove the general A006716 sequence finite**. The root-support <=16 classification is certified separately in [SUPPORT16.md](SUPPORT16.md), while the support-17 search is an additional finite computation.

# A006716: complete classification of roots with at most 11 nonzero digits

**Authors:** Qichao Wang (Hebei University of Technology); Daoyu Dong (University of Electronic Science and Technology of China).

**Status:** A global, finite-certificate result for a precisely defined infinite class of roots. The theorem does **not** settle whether all of OEIS [A006716](https://oeis.org/A006716) is finite, and literature priority is not claimed. This independent research note does not change the existing paper or PDF.

## Theorem 1: decimal gap restriction on the square root

Suppose the *positive integer square* \(x^2\) has no decimal digit zero. Write the nonzero decimal positions of \(x\) as

\[
0=e_1<e_2<\cdots<e_r
\]

and its corresponding nonzero digits as \(c_i\in\{1,\ldots,9\}\).

Then

\[
\boxed{e_{j+1}\le 2e_j+2\quad(1\le j<r),\qquad e_r\le 2^r-2.}
\]

**Proof.** Because \(x^2\) has no zero digit (indeed, all A006716 digits are 1, 4 or 9), \(x\) cannot be divisible by 10, so \(e_1=0\). For consecutive nonzero positions \(e_j<e_{j+1}\), write

\[
x=t+10^{e_{j+1}}h,\qquad
0<t<10^{e_j+1}.
\]

The digits in positions between \(e_j+1\) and \(e_{j+1}-1\) in the root vanish. Therefore

\[
x^2\equiv t^2\pmod{10^{e_{j+1}}}.
\]

If \(e_{j+1}>2e_j+2\), then \(t^2<10^{2e_j+2}\), so the digit of \(x^2\) in position \(2e_j+2\) is zero. That position is below \(e_{j+1}\) and below the length of \(x^2\), a contradiction. Thus \(e_{j+1}\le2e_j+2\). Starting with \(e_1=0\), induction gives \(e_r\le2^r-2\). □

**Global consequence:** for every fixed integer \(r\), only finitely many A006716 squares can have a square root with at most \(r\) nonzero decimal digits. This is a genuine integer-square obstruction, not a modular-residue test. It excludes all arbitrarily spaced sparse-root patterns with bounded support size.

## Theorem 2: independent digit-sum bound

Let \(s_{10}(x)\) be the sum of the decimal digits of \(x\), and let \(\nu_{10}(x)\) be the number of its nonzero digits. If \(x^2\) is an \(n\)-digit member of A006716 and \(\nu_{10}(x)=r\), then

\[
\boxed{n\le s_{10}(x)^2\le81r^2,\quad
r\ge\left\lceil\frac{\sqrt n}{9}\right\rceil.}
\]

Indeed, the usual carry operation in base 10 cannot increase digit sum. Expanding the product of the two decimal digit polynomials yields the standard inequality \(s_{10}(ab)\le s_{10}(a)s_{10}(b)\), so \(s_{10}(x^2)\le s_{10}(x)^2\). As every output digit is at least one, \(n\le s_{10}(x^2)\), while \(s_{10}(x)\le9r\). □

This proves an asymptotic lower bound on root digit density (at least order \(\sqrt n\) nonzero root digits). The gap theorem gives sharper structural bounds for small fixed \(r\).

## Theorem 3: complete sparse-root classification through support 11

**Claim (finite, machine-verifiable certificate):** If \(x^2\) has only digits in \(\{1,4,9\}\) and \(x\) has **at most 11 nonzero decimal digits**, then and only then \(x\) belongs to the following list.

| \(\nu_{10}(x)\) | All possible integer roots \(x\) |
|---:|---|
| 1 | 1, 2, 3, 7 |
| 2 | 12, 21, 38, 107 |
| 3 | 212, 70107 |
| 4 | **none** |
| 5 | 31488 |
| 6 | 387288 |
| 7 | 95610729 |
| 8 | **none** |
| 9 | 446653271, 3148717107, 21081079479 |
| 10 | **none** |
| 11 | **none** |

Thus this infinite class of roots yields **exactly 16 distinct A006716 squares**. All correspond to already recorded OEIS terms; this is a *new form of completeness certificate for the bounded-root-support problem*, not discovery of new sequence terms.

### Why the exhaustive calculation is globally complete

For a root with exactly \(r\) nonzero digits, its least significant digit must be nonzero, and every next nonzero position must satisfy Theorem 1. This produces a *finite* tree of positional supports, regardless of root magnitude, with maximum position \(2^r-2\).

At a partial root \(t=\sum_{i=1}^j c_i10^{e_i}\), before adding a higher digit at exponent \(e\), every decimal digit of \(t^2\bmod10^e\) must lie in \(\{1,4,9\}\). That is because all subsequent root terms start at position \(e\) or higher, so they cannot change any digit of the square **below** position \(e\).

The verifier checks this necessary condition using exact integer arithmetic and prunes only a subtree whose low square digits are already invalid. When the chosen support reaches \(r\), it tests every digit of the **entire** exact integer square.

Accordingly the pruning is sound, the support bound exhausts all roots for the stated \(r\), and no assumption that the root is numerically small is used.

**Exact search audit:** for \(r=11\), the finite search visits 6,319,638 complete candidate roots after low-digit pruning and finds no square. Smaller depths are independently checked by the same verifier. A second Python search explicitly enumerates and verifies the complete \(r\le4\) classification (171 candidates with \(r\le2\), 269,001 raw four-digit-support candidates).

### Reproduce

```sh
g++ -std=c++17 -O3 papers/A006716/verify_sparse_roots.cpp -o /tmp/a006716_sparse
/tmp/a006716_sparse
python papers/A006716/verify_sparse_roots.py
```

The C++ certificate relies on Boost.Multiprecision arbitrary-precision *integer* arithmetic; it does not use floating point or probabilistic tests.

### Limitation and significance

The theorem rules out every **bounded-support** strategy for constructing infinitely many A006716 squares, including irregular, nonperiodic distributions of nonzero root digits. It does not bound the number of nonzero root digits in the general conjecture, and so does **not** prove A006716 finite. The known 36-digit term has a square root with 14 nonzero decimal digits and therefore lies outside the classification above.

The digit-sum inequality itself is standard. The computation is a self-contained classification for this particular digit set, not a claim of priority over OEIS computational literature.

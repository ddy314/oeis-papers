# A077187: positive-density stable witnesses and a scalar drift question

**2026-10-18. PROVED quantitative theorem for nonzero drift; a separate
scalar-gcd observation remains CONJECTURAL.** This continuation uses
the reduced stable period in the updated HANDOFF; it does not claim the
unrestricted OEIS problem is solved or that a zero-drift orbit must
contain a witness.

## 1. Exact half-of-all-phases theorem for singular digit windows

Let \(p\ge7,\ p\ne11\) be prime,
\(r=\operatorname{ord}_p(10)\),
\(v=r/(2^{v_2(r)}5^{v_5(r)})\),
\(t=v/\gcd(v,9)\), and
\[
T=\operatorname{lcm}(r,\operatorname{ord}_t(10)).
\]
The updated short-period theorem shows that the stable boundary states
\(S_{jT}=(C_{10^{jT}-1},Y_{10^{jT}-1})\) obey
\[
S_{jT}=S_T+(j-1)(U,V)\quad (j\ge1).
\]
Set \(\sigma=U+V\) and \(K=C_T+Y_T\).

**Theorem A (singular square law).** If \(\sigma\ne0\), then among
the \(p\) residue classes \(j\bmod p\), **exactly**
\[
\boxed{\frac{p+1}{2}}
\]
are such that the entire \(jT\)-digit window contains some
\(k\) with \(p\mid M(k)\). Across all \(p\) classes, there are
**exactly \(p\)** pairs \((j,x)\in\mathbb F_p^2\)
with \(x=k\bmod p\) satisfying this window condition.
For each successful residue pair, infinitely many distinct decimal
mountains occur by choosing \(j\mapsto j+mp\), \(m\ge0\).

If \(\sigma=0\), either all \(p\) classes succeed or none do in
these same singular windows, according as \(-K\) is a square
(including zero) or a nonsquare.

**Proof.** In a \(d\)-digit window with \(d=jT\), we have
\(10^d=1\pmod p\), \(10^{d-1}=1/10\pmod p\).
The exact singular-layer identity from \`zero_drift.md\` is
\[
\frac{M(k)}{10^{D(k-1)}}=k^2+C_d+Y_d
          =k^2+K+(j-1)\sigma .
\tag{1}
\]
Every such window is long enough to contain *all* residues
\(x=k\bmod p\); indeed \(d\ge T\ge r\),
\(9\cdot10^{d-1}>p\) since \(p\mid10^r-1\)
(and for \(p\ne3\), \(p\le(10^r-1)/9\)).
For \(\sigma\ne0\), the values
\(-K-(j-1)\sigma\) run bijectively through \(\mathbb F_p\)
as \(j\) runs through any complete residue system modulo \(p\).
The set of squares including 0 has \((p+1)/2\) elements.
There is one solution \(x\) for zero, two for each nonzero square,
and none for nonsquares. Summing gives
\(1+2(p-1)/2=p\) solution pairs. The states repeat after
\(p\) stable blocks in the field, establishing recurrence for
\(j\mapsto j+p\). If \(\sigma=0\), the square condition is
independent of \(j\). QED.

This theorem makes no claim about all digit windows, only the specific
\(jT\)-digit windows. It is a **quantitative** strengthening of the
earlier two-offset existence theorem whenever \(\sigma\ne0\).

## 2. The anti-diagonal drift cannot defeat all next-window phases

**Theorem B (anti-diagonal alternative).** Suppose
\((U,V)\ne(0,0)\) but \(\sigma=U+V=0\). Let
\(\varepsilon_r=0\) for even \(r\) and \(1\) for odd \(r\).
For offsets \(n=0,\ldots,r-1\), consider
\[
k=10^{jT}+n,\quad j\ge1.
\]
Exactly \(r-\varepsilon_r\) of these offsets have a
**nonzero affine slope** as a function of \(j\). For each such
offset there is a unique solution class \(j\bmod p\).
Furthermore at least
\[
\boxed{\left\lceil\frac{r-\varepsilon_r}{2}\right\rceil}
\tag{2}
\]
**distinct** solution classes \(j\bmod p\) occur among these offsets;
each yields infinitely many mountain witnesses.

**Proof.** As established in the earlier many-witness theorem,
the normalized residue at \(k=10^{jT}+n\) is affine in \(j\),
with slope
\[
s_n=10^{n+1}U+10^{-n}V.
\]
Here \(V=-U,\ U\ne0\), so
\[
s_n=U10^{-n}(10^{2n+1}-1).
\tag{3}
\]
It vanishes exactly if \(r\mid(2n+1)\).
For even \(r\) there is no such \(n\); for odd \(r\)
there is exactly one modulo \(r\).
Thus every other offset yields a unique phase \(j\in\mathbb F_p\).

At a fixed phase \(j\), the entire first post-boundary window
has the exact nonsingular form
\[
A_jz+B_jz^{-1}+H,\quad z=10^n,\qquad
H=-20/81\ne0\pmod p
\]
(the characteristic is neither 2,3 nor 5).
Multiplication by \(z\ne0\) gives a **nonzero**
polynomial of degree at most two. It therefore has at most
two roots in the order-\(r\) subgroup.
Consequently no phase \(j\) can account for more than two of
the \(r-\varepsilon_r\) good offsets; (2) follows.
Periodicity in \(j\bmod p\) again makes infinitely many witnesses.
QED.

**Combined consequence.** Every target prime with **nonzero**
drift admits not merely one but many distinct successful block phases:
exactly \((p+1)/2\) through the singular-window square law if
\(U+V\ne0\), or at least (2) through the next-window
construction when \(U+V=0\).
This does not exclude \((U,V)=(0,0)\).

## 3. A new scalar-rank observation — CONJECTURAL, not a theorem

Define the **repunit-ring** drift for each formal \(r\ge2\)
over \(N_r=10^r-1\) using the exact stable-period algorithm in
\`certify_orders_le500.py\`, but with the updated shorter phase
period \(T=\operatorname{lcm}(r,\operatorname{ord}_{v/\gcd(v,9)}(10))\).
The following striking equality survived exact independent ring
calculations for every \(2\le r\le300\), and separate spot tests
at \(r=312,336,408,432,496,552,696\):
\[
\boxed{
\gcd(N_r,U_r+V_r)\ \stackrel{?}{=}\
\gcd(N_r,U_r,V_r).
}\tag{4}
\]
The equality is **NOT PROVED for arbitrary \(r\)**. A finite
computation, even when exact and extensive, cannot establish it.
In particular (4) must **not** be substituted for a proven
nonzero-drift theorem or a zero-drift witness construction.

A proof of (4) would show that the global drift can only lie on
the anti-diagonal modulo a prime divisor of \(N_r\) if it is
actually the zero vector. But it would not exclude true zero drift.
A potentially weaker primitive-order target is
\[
p\mid \Phi_r(10),\ p\nmid r,\ p\mid U_r+V_r
\quad\Longrightarrow\quad p\mid U_r,V_r.
\tag{5}
\]
This is equivalent to testing whether a scalar drift zero forces
simultaneous zero at exact order \(r\), and could admit an
independent proof using the whole-period twisted-reflection
identity already in the repository.

The key open problem remains:
\[
(U,V)=0\quad\Longrightarrow\quad
\text{some stable window has orbit norm zero}
\]
(or alternatively to rule out true zero drift altogether).
Neither Theorem A, Theorem B, nor (4) settles this implication.

## 4. Reproducibility

\`audit_quantitative_witness_density.py\` independently verifies
Theorems A and B on selected finite fields, including **synthetic**
anti-diagonal affine states to exercise the second theorem without
pretending a genuine zero-drift prime has been found.
The finite scalar observation is recorded separately, with
a reproducible C++17/GMP trial program.

These checks are falsification aids, not the proofs of the
unbounded results. The exact algebraic arguments above establish
Theorems A and B. OEIS A077187 in its unrestricted all-primes
form remains **OPEN**.

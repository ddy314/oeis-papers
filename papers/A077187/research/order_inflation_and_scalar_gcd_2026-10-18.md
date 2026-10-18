# A077187: order inflation, scalar drift, and a possible universal GCD law

**18 October 2026.** Continuation of PR #8. The order-inflation theorem
below is **PROVED**. The exact GCD identity below is **CONJECTURAL** for
unbounded orders and **must not be presented as a proof of A077187**.
All numerical tests have finite, explicitly stated ranges.

## 1. Notation

For any integer \(r\ge1\), let \(N_r=10^r-1\). Split
\[
r=2^a5^c v,\qquad \gcd(v,10)=1,\qquad
T_r=\operatorname{lcm}(r,\operatorname{ord}_v(10)),
\quad\operatorname{ord}_1(10)=1.
\]
Let \(F_d^{(n)}\) denote the *actual* full \(d\)-digit-layer affine map
on \((C,Y)\) modulo any \(n\) coprime to 10, with
\(Y_k=10^{-D(k)}R_k\). Recall the exact recurrence:
\[
F_d(C,Y)=\left(A C+(q-1)S-J,\ A^{-1}(Y+LS+J)\right),
\]
where \(L=10^{d-1}\), \(q=10^d\),
\(m=9L\), \(A=q^m\), \(S=\sum_{j=0}^{m-1}q^j\),
and \(J=\sum_{j=0}^{m-1}jq^j\).
We use \(S_d=(C_{10^d-1},Y_{10^d-1})\) for the endpoint state.

For \(p\ge7\) prime, \(p\ne11\), let
\(s=\operatorname{ord}_p(10)\).
The established stable-period lemma says that
\(F_{d+T_s}^{(p)}=F_d^{(p)}\) for \(d\ge E_s\), with
\(E_s=1+\max(v_2(s),v_5(s))\);
every \(T_s\)-layer stable product has diagonal linear part identity,
and hence is a **translation** in \(\mathbb F_p^2\).
Write
\[
\delta_s=S_{2T_s}-S_{T_s}\pmod p.
\]
For a **larger** integer \(r\) divisible by \(s\), write
\[
\delta_r=S_{2T_r}-S_{T_r}\pmod p.
\]
Here \(T_r\) is defined from the formal integer \(r\); it is not
necessarily the *minimal* prime-field period.

## 2. Universal order-inflation lemma — PROVED

**Theorem.** If \(p\ge7\), \(p\ne11\), and
\(s=\operatorname{ord}_p(10)\mid r\), then
\[
\boxed{T_s\mid T_r,\qquad
\delta_r=(T_r/T_s)\,\delta_s\pmod p.}
\]

**Proof.** Write \(r=2^a5^cv\) and \(s=2^{a'}5^{c'}w\),
with \((vw,10)=1\). Since \(s\mid r\), we have \(w\mid v\) and
\(\operatorname{ord}_w(10)\mid\operatorname{ord}_v(10)\).
Thus \(T_s\mid T_r\).

All digit-layer indices \(d\ge T_s+1\) are in the stable range for the
actual order \(s\). Therefore the \(T_s\) consecutive maps
\(F_{T_s+1},\ldots,F_{2T_s}\) form a single affine translation
\(P(x)=x+\delta_s\) (the displacement does not depend on the state).
Periodicity means the same *ordered* \(T_s\) maps repeat beginning at
every layer congruent to \(T_s+1\bmod T_s\), including \(T_r+1\).
Consequently, the \(T_r/T_s\) consecutive blocks from \(T_r+1\)
through \(2T_r\) apply \(P^{T_r/T_s}\). Since
\(P^m(x)=x+m\delta_s\) in characteristic \(p\),
the net displacement of the *actual* state \(S_{T_r}\) is
\((T_r/T_s)\delta_s\), which is precisely \(\delta_r\). QED.

**Exact consequence.** For every prime \(p\mid N_r\), with actual
order \(s\mid r\), the simultaneous zero-drift condition is equivalent
to
\[
\boxed{\delta_r=0
\iff p\mid (T_r/T_s)\ \text{or}\ \delta_s=0.}
\]
The equivalence here is in \(\mathbb F_p^2\); multiplying a nonzero
vector by a nonzero scalar cannot annihilate it.

This explains why the *full repunit* GCD can have primes that
are not valid obstructions at the **exact** target order \(r\).
The proposed support-on-\(990r\) property was already refuted in
earlier research notes; the order-inflation law is a rigorous
explanation of this phenomenon, not a repair of that false claim.

Eight checks computed the original two-state recurrence directly:

| Actual order \(s\) | Formal order \(r\) | \(p\) | \(T_r/T_s\) | \(\delta_s\) modulo \(p\) | \(\delta_r\) |
|---:|---:|---:|---:|---|---|
| 6 | 174 | 7 | 406 | (0,1) | (0,0) |
| 6 | 258 | 7 | 301 | (0,1) | (0,0) |
| 6 | 696 | 7 | 812 | (0,1) | (0,0) |
| 16 | 272 | 17 | 17 | (8,13) | (0,0) |
| 2 | 88 | 11 | 44 | (9,0) | (0,0) |
| 4 | 808 | 101 | 202 | (80,12) | (0,0) |
| 3 | 888 | 37 | 296 | (33,20) | (0,0) |
| 6 | 936 | 13 | 156 | (8,6) | (0,0) |

The last two coordinates are zero in all eight cases because each
\(p\) divides the displayed ratio. This does not establish any
nonzero-drift claim for a different prime of exact order \(r\).

## 3. Unexpected exact scalar-GCD pattern — NOT PROVED universally

Use the *composite-ring* single-period translation from the preceding
note to form
\[
(U_r,V_r)=
\left(F_{2T_r}\circ\cdots\circ F_{T_r+1}\right)(0,0)
\in(\mathbb Z/N_r\mathbb Z)^2 .
\]
Define
\[
G_r=\gcd(N_r,U_r,V_r),\quad
H_r=\gcd(N_r,U_r+V_r).
\]
Direct integer arithmetic gives the stronger empirical identity
\[
\boxed{\quad G_r=H_r=\gcd(N_r,9T_r).\quad}\tag{C}
\]

**Verified data, not a theorem for arbitrary \(r\):**
- Every \(2\le r\le180\), by a reference full-\(2T\) Python
  implementation working in \(\mathbb Z/N_r\mathbb Z\).
- Separate exact single-period C++/GMP cross-checks at
  \(r=174,258,272,504,584,696,808,856,936,1000,1008,1056,
  1080,1112,1152,1200\).
- The 112 certified non-elementary orders \(r\le1000\) in PR #8
  supply further exact \(G_r\) values; the full *scalar* identity
  is not claimed to have been independently recomputed for all
  \(r\le1000\).

For example:
\[
\begin{array}{r|r|r|r}
r&T_r&G_r=H_r&\gcd(N_r,9T_r)\\\hline
174&2436&189&189\\
258&1806&189&189\\
272&272&153&153\\
504&504&567&567\\
584&584&657&657\\
696&4872&189&189\\
808&808&909&909\\
856&45368&9&9\\
936&936&1053&1053\\
1008&1008&567&567\\
1112&25576&9&9\\
1200&1200&27&27
\end{array}
\]

**Conditional consequence (rigorous implication, not a proof).**
Suppose merely that
\[
\gcd(N_r,U_r+V_r)\mid 9T_r
\quad\text{for every }r\ge2.\tag{S}
\]
If a prime \(p\ge7,\ p\ne11\) has exact order \(r\) and zero drift,
then \(p\mid N_r\) and \(p\mid U_r+V_r\), so (S) gives
\(p\mid9T_r\). But \(\operatorname{ord}_v(10)\le\varphi(v)\le v-1<r\)
for \(v>1\) (and \(\operatorname{ord}_1(10)=1\)), so
every prime divisor of \(T_r=\operatorname{lcm}(r,\operatorname{ord}_v(10))\)
is at most \(r\). Exact order \(r\) implies \(r\mid p-1\), hence
\(p\ge r+1\). It follows that \(p\nmid T_r\); also \(p\nmid9\).
Contradiction. Therefore **even the weaker uniform divisibility (S)
would imply nonzero drift for all primes** and, by the two-offset
construction, solve the unrestricted positive-prime part of A077187.

The **missing proof is (S)**, or any equally strong universal
nonvanishing relation. No inference from finite data to all \(r\)
is legitimate here.

## 4. Next mathematical target

The finite identity (C) suggests replacing the 2-dimensional
simultaneous-zero problem by the scalar \((U_r+V_r)\).
This is a genuine simplification of what must be proved, but
**not** a proved bound on its gcd for unbounded \(r\).
Potential strategies:
1. derive a Bézout identity for \(U_r+V_r\) and \(10^r-1\), with
   right-hand side supported on \(9T_r\);
2. analyze the periodic affine cocycle in
   \(\mathbb Z[1/10]/(10^r-1)\) and its behavior at primitive
   \(r\)-th roots;
3. search for the first failure of the scalar identity before trying
   to prove it in general.

The GitHub scripts are intended to distinguish each verified
finite fact from the open global claim.

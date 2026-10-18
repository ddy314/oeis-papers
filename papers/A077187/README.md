# OEIS A077187 — decimal mountain concatenations (partial results)

**Author:** Qichao Wang. **Date:** 2026-10-17.
**Status:** computer-assisted, not externally peer reviewed. **The unrestricted A077187 conjecture remains OPEN.**

Let
\[
M(k)=1\Vert2\Vert\cdots\Vert k\Vert(k-1)\Vert\cdots\Vert1
\]
be the decimal mountain concatenation. This folder collects the current *partial* existence theorems and reproducible exact-integer certificates.

## Proven subfamilies (subject to independent manuscript and code review)

For primes \(p\ge7\), let \(r=\operatorname{ord}_p(10)\).
Our cumulative result is the smooth-order family
\[
\boxed{r=2^a3^b5^c,\qquad a,c\ge0,\ 0\le b\le8
\quad\Longrightarrow\quad \exists k\ge1:\ p\mid M(k).}
\]
This folder's new result specifically treats **\(b=8\)**, assuming the earlier affine-monodromy lemma and lower-stage certificates. It does not prove existence for arbitrary prime-order structures, does not compute least \(k\), and does not update OEIS directly.

For \(b=8\), all **486 primitive phases modulo 729** were checked using exact cyclotomic norms and a GMP one-shot gcd sieve. Six phases had nontrivial gcd, with prime factors 52489, 328051, and 839809. Each factor's actual order phase differs from the phase at which the gcd appears; its actual-phase gcd is 1. Therefore no admissible prime makes both affine-drift coordinates vanish in this order class.

The novel computational simplification is the **cubic relative norm tower** reducing cyclotomic norm degrees
\[
486\to162\to54\to18\to6\to2\to1.
\]
For a cubic relative extension, the core identity is
\[
\operatorname{Norm}(A+xB+x^2C)=A^3+yB^3+y^2C^3-3yABC,\qquad x^3=y.
\]
The next stage would address \(b=9\) or develop a general mechanism for multiplicative orders with prime factors beyond \(2,3,5\).

## Materials

- [main.pdf](main.pdf) — two-page English partial-theorem paper (compiled from [main.tex](main.tex)).
- [candidate_table.tex](candidate_table.tex) — complete list of the six nontrivial gcd rows, typeset in the paper.
- [exact_b8_fast.py](exact_b8_fast.py), [tower_norm.py](tower_norm.py), [generate_norms_parallel.py](generate_norms_parallel.py) — exact formula and 486-norm computation.
- [norm_gamma_*.txt](.) — all 486 full integer norms (approximately 5,800 digits each).
- [one_shot_gmp_b8.cpp](one_shot_gmp_b8.cpp), [all_486_gmp.tsv](all_486_gmp.tsv) — full-range one-shot GMP gcd checks.
- [audit_all_b8.py](audit_all_b8.py), [check_direct_b8.py](check_direct_b8.py), [verify_all.py](verify_all.py) — exact audits, independent finite-field checks and full digit-layer recurrences.

The source scripts use Python 3, SymPy and NumPy. The gcd program uses GMP and a C++17 compiler.

Reproducibility steps (from this directory):
1. `python generate_norms_parallel.py`
2. `c++ -O3 -std=c++17 one_shot_gmp_b8.cpp -lgmpxx -lgmp -o one_shot_gmp_b8`
3. `bash run_sieves.sh`
4. `python verify_all.py`
5. Compile `main.tex` twice with `pdflatex`.

All computational evidence supports the specified infinite subfamily only. The underlying formulas, software and final claims await external mathematical audit. No all-primes proof is claimed.


## Unrestricted-order research continuation (October 18, 2026)

The separate research notes do **not** extend the fully certified b=8 result
to all primes. They develop a general-order finite-defect transfer and
two-offset drift criterion, then prove the exact elementary invariant
\[
\Delta_C+\Delta_Y=9/100\pmod p\ne0
\]
for every prime \(p\ge7,\ p\ne11\), whose \(\operatorname{ord}_p(10)\)
has no prime factors outside \(2,3,5\) and has \(v_3\le2\).
This gives a proof of the low-\(3\)-adic-order class independent of any
cyclotomic norm certificates.

- [Elementary invariant and refined zero-drift decision](research/elementary_drift_and_zero_drift_decision_2026-10-18.md)
- [Exact finite scan, no floating point](research/drift_scan_general.cpp):
  compile with \`g++ -O3 -std=c++17\` and run with argument \`5000\`.
- [Independent within-window and subgroup-root audit](research/window_quadratic_audit.py):
  run \`python research/window_quadratic_audit.py\`.

Finite evidence: 665 checked primes below 5000 (excluding \(p=11\)) all
had nonzero drift. The square-root/subgroup test rigorously decides any
individual zero-drift prime, if encountered; **the universal existence
conjecture remains open.**


## Exact repunit-ring order certificates, October 18 continuation

A second **independent computational theorem** now covers all primes whose
multiplicative order of 10 belongs to 42 specific previously uncovered
order classes \(r\le500\). For each such \(r\), arithmetic is performed
directly modulo \(N_r=10^r-1\), without factoring that integer. The
difference of two exact digit-layer states gives \((U_r,V_r)\); the full
gcd \(G_r=\gcd(N_r,U_r,V_r)\) has prime factors dividing \(990r\).
Since a prime of exact multiplicative order \(r\) must exceed \(r\),
none of those primes can have zero drift, so the general two-offset
witness theorem applies.

Together with earlier proved smooth-order / \(u\mid20\) classes, this
gives the **cumulative** existence result for all primes satisfying
\(\operatorname{ord}_p(10)\le500\), subject to those earlier certificates'
independent review. The new 42-class result itself does not depend on
their validity.

- [Mathematical proof, full class list and exact gcd table](research/order_bound_500_certificate_2026-10-18.md).
- [Self-contained standard-library Python certifier](research/certify_orders_le500.py).
- Run \`python3 papers/A077187/research/certify_orders_le500.py\` from repository root.
- GitHub Actions: \`.github/workflows/a077187-order-bound.yml\`.

The unrestricted all-primes OEIS problem remains **open**: certification
for all \(r\le500\) is a finite order-bound theorem, not a proof for
unbounded multiplicative orders.


### Cyclotomic refinement and negative controls

The tempting extension
\(\operatorname{rad}(G_r)\mid\operatorname{rad}(990r)\) for *all*
\(r\) is false: at \(r=174,258\), one finds \(G_r=189=27\cdot7\),
although \(7\nmid990r\). These are not counterexamples to the mountain
conjecture because \(\operatorname{ord}_7(10)=6\), not 174 or 258.

Working modulo \(\Phi_r(10)\) filters such lower-order prime factors.
For ten independent check cases, the refined gcd
\(\gcd(\Phi_r(10),U_r,V_r)\) is 1 except at \(r=272\), where it is 17,
a divisor of \(r\). See
[cyclotomic spot checker](research/audit_cyclotomic_spots.py) and
[mathematical explanation](research/order_bound_500_certificate_2026-10-18.md).
This is a finite observation, not an all-order theorem.


## Improved self-contained bounded-order theorem: \(\operatorname{ord}_p(10)\le744\)

The earlier cutoff of 500 is now superseded by an **independently
certifiable cutoff of 744**, using 77 exact-order gcd certificates
together with two elementary infinite-family lemmas (\(u\mid20\)
and \(v\mid9\), where \(r=u\,v\) is split into its \(2,5\)-smooth
and coprime-to-10 parts). Thus the bounded-order result **no longer
depends on the high-\(3\)-power cyclotomic norm tower**.

- [Bounded-order theorem, full proof and results](research/order_bound_744_theorem_2026-10-18.md).
- [Typeset research note source](research/order_bound_744.tex);
  [compiled PDF](research/order_bound_744.pdf) (generated by CI).
- [35 additional exact GCD rows](research/certify_orders_le744.py)
  (31 genuinely new classes + four former norm-dependent cases).
- [Independent direct prime-field audit](research/audit_order_744_prime_field.py)
  at exact orders 584, 664, 696.
- [Original 42-row certificate](research/certify_orders_le500.py).

Reproduce with Python 3 and no third-party packages:
\`\`\`sh
python3 papers/A077187/research/certify_orders_le500.py
python3 papers/A077187/research/certify_orders_le744.py
python3 papers/A077187/research/audit_order_744_prime_field.py
\`\`\`

The apparent obstruction at \(r=696\), \(G_r=189=3^3\cdot7\),
is not a counterexample: \(\operatorname{ord}_7(10)=6\ne696\).
The computational certificate checks the exact multiplicative order of
*every* prime factor of *every* small gcd, not merely whether the
factor divides \(990r\).

**The unrestricted all-primes existence conjecture is still open.**
This finite-order result is conditional on mathematical review of
the two elementary arguments and on independent reproduction of
the exact-arithmetic programs.


## Latest bounded-order theorem: \(\operatorname{ord}_p(10)\le1000\)

**Supersedes the earlier cutoffs of 500 and 744.**
We certify every prime \(p\ne2,5\) with
\(\operatorname{ord}_p(10)\le1000\) using two previously established
elementary infinite-family lemmas and **112** complete, exact
order-class certificates. The 35 newly added classes are
\(745\le r\le1000\). The unrestricted all-primes problem remains OPEN.

New theoretical ingredient: the \(T\)-layer stable affine product has
identity linear part over \(\mathbb Z/(10^r-1)\), so its translation
(the two-coordinate drift) can be computed from a zero initial state in
**one stable period**, without running all \(2T\) layers.

More strongly, for every one of the 35 new classes,
\[
\gcd(\Phi_r(10),U_r,V_r)=1.
\]
This is verified by a separate standard-library Python program,
after exact C++/GMP computation of
\(G_r=\gcd(10^r-1,U_r,V_r)\).
It **does not** assert universal cyclotomic coprimality: \(r=272\)
is an existing exception with cyclotomic gcd 17.

- [Detailed theorem and proof](research/order_bound_1000_theorem_2026-10-18.md)
- [New LaTeX manuscript](research/order_bound_1000.tex) and
  [PDF](research/order_bound_1000.pdf) (generated by GitHub Actions)
- [Single-period GMP exact certifier for 35 new classes](research/single_period_order_1000.cpp)
- [Independent field-level audit](research/audit_order_1000_prime_field.py)
- [Independent cyclotomic-coprimality audit](research/audit_cyclotomic_order_1000.py)

Commands from \`papers/A077187/research\`:
\`\`\`sh
python3 certify_orders_le500.py
python3 certify_orders_le744.py
g++ -O3 -std=c++17 single_period_order_1000.cpp -lgmpxx -lgmp -o order1000
./order1000 > order1000_rows.tsv
python3 audit_order_1000_prime_field.py
python3 audit_cyclotomic_order_1000.py order1000_rows.tsv
\`\`\`

All 35 exact new tuples are embedded in the certifier, and its
SHA-256-pinned output is validated in CI. As before, this finite
computer-assisted theorem is subject to independent code and
mathematical review; **nothing here proves A077187 for unbounded
multiplicative orders**.


## New unrestricted-order structural work (18 October)

The finite cutoff of 1000 remains valid, but the latest work targets
an **unbounded-order mechanism** rather than further extending the
cutoff. See
[order-inflation and scalar-GCD note](research/order_inflation_and_scalar_gcd_2026-10-18.md)
and [exact reference auditor](research/audit_scalar_gcd_and_inflation.py).

**Proved for every formal order \(r\):** if \(p\mid10^r-1\), its
actual multiplicative order is \(s\mid r\), and
\(T_t=\operatorname{lcm}(t,\operatorname{ord}_{v_t}(10))\), then
\[
\Delta_r=(T_r/T_s)\Delta_s\pmod p .
\]
In particular,
\[
\operatorname{rad}\gcd(10^r-1,3T_r)
\mid\operatorname{rad}\gcd(10^r-1,U_r,V_r),
\]
and both drift coordinates are divisible by 9 over the full
integer repunit ring. The note proves these assertions and an
equivalence between the **missing reverse radical inclusion** and
nonzero true-order drift for all primes.

**New conjecture, NOT a theorem:** exact finite computations
for all \(2\le r\le180\), plus selected higher orders through
\(r=4624\), give
\[
\gcd(10^r-1,U_r,V_r)
=\gcd(10^r-1,U_r+V_r)
=\gcd(10^r-1,9T_r).
\]
If the weaker global bound
\(\gcd(10^r-1,U_r+V_r)\mid9T_r\) could be
proved for arbitrary \(r\), it would imply that the drift
is nonzero for every prime of exact order \(r\), and hence
settle the existence conjecture. **This implication is proved;
its hypothesis is not.**

Reproduce the finite scalar and inflation tests via
\`python3 papers/A077187/research/audit_scalar_gcd_and_inflation.py\`.
A separate GitHub Actions workflow runs the test automatically.


The same finite audit also confirms the **stronger single-offset slope**
identity \(\gcd(10^r-1,10U_r+V_r)=\gcd(10^r-1,9T_r)\)
for \(2\le r\le180\), with selected higher-order samples.
A universal proof of even its weaker divisibility form
would force the \(k=10^{jT_r}\) (no \(+1\)) construction
to work for all primes \(p\ge7\) except \(11\), which already
has the short witness \(M(2)=121\).
This remains a conjectural route, not a claimed theorem.


## Exact primitive-order cyclotomic obstruction (October 18)

A new *unbounded-order structural equivalence* sharpens the zero-drift
problem. For each \(r\ge2\), let \((U_r,V_r)\) be the stable-period
translation modulo \(10^r-1\), and put
\[
H_r=\gcd\bigl(\Phi_r(10),U_r,V_r\bigr).
\]
Then **all primes of exact order \(r\) have nonzero drift if and only if**
\[
\boxed{\operatorname{rad}(H_r)\mid\operatorname{rad}(r).}
\]
This follows from the cyclotomic primitive-order property: the primes
dividing \(\Phi_r(10)\) but not \(r\) are precisely the primes
with \(\operatorname{ord}_p(10)=r\). Repeated gcd removal against \(r\)
decides the criterion without factoring \(10^r-1\).

This is a **reduction**, not proof that the criterion holds at all \(r\).
If it fails, the surviving prime factors would be genuine zero-drift
primes, but might still divide other mountain concatenations.

- [Full theorem and proof](research/cyclotomic_exact_obstruction_2026-10-18.md)
- [Exact primitive-order decision and nine test cases](research/exact_cyclotomic_obstruction.py)
- [Dedicated CI](../../.github/workflows/a077187-exact-obstruction.yml)

No claim of an unrestricted A077187 proof is made.


## Structural continuation: two-way block words and integrable windows

[Global structure and proofs (October 18)](research/global_block_hyperbola_structure_2026-10-18.md)
reframes the unbounded-order research **without extending the finite
order cutoff**:

- The exact stable drift over \(\mathbb Z/(10^r-1)\) is simply the
  pair of residues of all integers \(10^T,\dots,10^{2T}-1\)
  concatenated in *increasing and decreasing* order. True-order
  zero drift is equivalent to simultaneous divisibility of these two
  explicit block words.
- Inside each fixed-width digit layer, polynomial centered coordinates
  obey \(X\mapsto qX,\ Z\mapsto q^{-1}Z\) and preserve \(XZ\).
  The normalized mountain condition becomes the intersection
  \(qX+Z=2q\) with that invariant hyperbola (with \(q=1\)
  treated as a separate unipotent layer).
- Reflection of a full consecutive-number block cancels the weighted
  first moment exactly:
  \(C'+AY'-AC-Y=(L+q-1)\sum_{i<m}q^i\).
  This explains the earlier \(9/100\) invariant when the layer
  multipliers are all 1, **without** assuming that the varying twists
  cancel for arbitrary multiplicative orders.
- A nonzero drift gives **at least \(r-\gcd(r,2)\) distinct fixed-offset
  witness families**, each containing infinitely many divisible
  mountains. This strengthens the former two-offset sufficient
  criterion quantitatively but does not rule out zero-drift primes.

A deliberately small independent check is in
[structural audit](research/audit_global_block_geometry.py), with
dedicated [GitHub Actions workflow](../../.github/workflows/a077187-global-geometry.yml).
A further **exact whole-period identity** (Theorem E in the same note)
decomposes, for any scalar \(\lambda\), the drift combination
\(\lambda U_r+V_r\) into a reflected-block baseline and an explicit
position-phase mismatch:
\[
\lambda U_r+V_r=\sum_d P_d\bigl[
(L_d+q_d-1)\Sigma_d+(\lambda\Theta_d^{-1}-1)B_d\bigr],
\qquad \Theta_d=P_d^2A_d .
\]
This is valid for **every** \(r\), over the composite ring.
The earlier \(v\mid9\) proof is exactly the case where
the \(\lambda=1\) mismatch vanishes. The general mismatch is
**uncontrolled**, not tacitly zero. The new
[short twisted-flux audit](research/audit_twisted_reflection.py)
checks it independently on five small orders.

The principal remaining mathematical gap is the **global interaction
of layer interfaces and the position-phase mismatch**, not the
locally integrable within-layer recurrence. The all-primes conjecture
remains open.


## Latest: fixed-coprime-order spectral compression and two new INFINITE families

A new **general structural theorem** shows that for any fixed coprime
part \(v\) of \(r=\operatorname{ord}_p(10)=2^a5^cv\),
the full stable drift, despite spanning
\(T=\operatorname{lcm}(r,\operatorname{ord}_v(10))\) digit layers,
reduces to at most
\[
\ell=\operatorname{lcm}(v,\operatorname{ord}_v(10))
\]
cyclotomic phase classes. Both drift coordinates are polynomials
of degree at most two in \(m=r/\gcd(r,\ell)\), with coefficients in
a cyclotomic field of degree at most \(\varphi(\ell)\) **independent
of unbounded \(a,c\)**. The formulas include all \(q=1\) singular
layers exactly, whose two reflected block contributions equal \(9/200\).

The new **computer-assisted infinite-order-class theorems** assert
\[
\boxed{\operatorname{ord}_p(10)
=7\cdot2^a5^c\ \text{or}\ 11\cdot2^a5^c
\quad\Longrightarrow\quad p\mid M(k)\text{ for some }k.}
\]
These are **not** merely finite \(r\le1000\) checks. For \(v=7\),
twelve fixed degree-six quadratic resultants and 4532
factorization-free cyclotomic exclusions close the class. For \(v=11\),
twenty fixed degree-ten *linear* resultants (the quadratic coefficients
vanish exactly) and 3943 phase-aware exclusions close the class.
Each norm is pinned; no target primes are enumerated or giant
repunit factorizations used.

- [Unified typeset paper](research/fixed_v_spectral_families.tex)
  and [compiled PDF](research/fixed_v_spectral_families.pdf)
  (produced by GitHub Actions).
- [Generic spectral derivation and complete \(v=7\) theorem](research/fixed_v_spectral_compression_v7_2026-10-18.md).
- [Linear-degeneracy derivation and complete \(v=11\) theorem](research/fixed_v11_linear_spectral_theorem_2026-10-18.md).
- [Exact quadratic norms and elimination](research/certify_fixed_v7.py).
- [Exact linear norms and elimination](research/certify_fixed_v11.py).
- [Independent field-level checks: \(v=7\)](research/audit_fixed_v7.py)
  and [\(v=11\)](research/audit_fixed_v11.py).

Independent GitHub Actions workflows
\`.github/workflows/a077187-fixed-v7.yml\` and
\`.github/workflows/a077187-fixed-v11.yml\`
have passed both symbolic proofs and direct field cross-checks.
The unrestricted all-primes conjecture is **still OPEN**, as the
uniform elimination has not been proved for arbitrary coprime part \(v\).

# A077187 — universal finite-defect multiplier reduction

**October 18, 2026. PROVED algebraic lemma; NOT an all-primes proof.**
This is a continuation of the arbitrary-order finite-defect transfer and
the later order-inflation analysis in PR #8.

## Setup

Let \(p\ge7\) be prime, \(p\nmid10\), and write
\[
r=\operatorname{ord}_p(10)=uv,\qquad
u=2^a5^c,\quad(v,10)=1,\quad(u,v)=1.
\]
Let \(E=1+\max(a,c)\),
\[
T=\operatorname{lcm}(r,\operatorname{ord}_v(10)),
\quad\operatorname{ord}_1(10)=1.
\]
For the original full \(d\)-digit layer and its stable continuation
in the same phase, define the respective diagonal multipliers
\[
A_d=10^{e_d},\quad e_d=9d10^{d-1},
\quad\widehat A_d=10^{\widehat e_d},\quad
\widehat e_d=9(T+d)10^{T+d-1}\pmod p.
\]
Since \(r\mid T\), the other digit-layer parameters
\(L=10^{d-1}\) and \(q=10^d\) agree modulo \(p\) between
the original layer \(d\) and the later layer \(T+d\).
Thus the discrepancy between their maps is controlled by
\(\rho_d=\widehat A_d A_d^{-1}\).

## New theorem: all finite-defect ratios lie in a fixed smooth-order group

Put \(\zeta=10^v\pmod p\), of exact multiplicative order \(u\),
and \(\gamma=v^{-1}\bmod u\) when \(u>1\).

**Theorem (finite-defect multiplier reduction).** For **every**
\(d\ge1\), when \(u>1\),
\[
\boxed{\rho_d=\zeta^{-\gamma\,9d10^{d-1}}\pmod p.}\tag{FD}
\]
The exponent on the right is reduced modulo \(u\). For all
\(d\ge E\), \(\rho_d=1\). In particular, all genuine multiplier
defects in the transient range \(1\le d<E\) belong to the group
\(\mu_u=\langle\zeta\rangle\), and their exponents depend on \(v\)
only through \(v^{-1}\pmod u\).

If \(u=1\), there are no transient multipliers:
\(\rho_d=1\) for every \(d\ge1\).

**Proof.** We work with exponents modulo \(r=uv\).
Since \(T\) is divisible by \(v\) and
\(10^T\equiv1\bmod v\),
\[
\widehat e_d
=9(T+d)10^{T+d-1}
\equiv9d10^{d-1}=e_d\pmod v.
\]
Since \(T\ge E\) and \(u\mid10^{T+d-1}\), we also have
\(\widehat e_d\equiv0\pmod u\). Therefore
\[
\widehat e_d-e_d\equiv0\pmod v,\qquad
\widehat e_d-e_d\equiv-e_d\pmod u.
\]
By the Chinese remainder theorem, the exponent difference modulo
\(uv\) is \(vt\), where
\(t\equiv-v^{-1}e_d=-\gamma e_d\bmod u\).
Exponentiating 10 gives (FD). For \(d\ge E\),
\(u\mid10^{d-1}\), so \(e_d\equiv0\bmod u\) and \(\rho_d=1\).
When \(u=1\), the difference is zero modulo \(v=r\), proving
the last assertion. QED.

**Importance and limitation.** For each *fixed* smooth part \(u\),
the relative multipliers of every early defective layer are drawn
from a finite cyclotomic group, **independently of how many or how
large the coprime-order factors \(v\) are**. This is a structural
reduction for pursuing new infinite families with a fixed \(u\),
not a proof that their stable translation has nonzero drift.
The full state \(S_T\) can still depend on the large, unbounded
coprime factor \(v\).

## Corollary: all primes with smooth part \(u=8\)

Let \(r=8v\), with \(v\) odd and coprime to 10, and let
\(\gamma=v^{-1}\bmod8\), \(\zeta=10^v\bmod p\).
Now \(E=4\) and
\[
(e_1,e_2,e_3)=(9,180,2700)\equiv(1,4,4)\pmod8.
\]
Since \(\gamma\) is odd and \(\zeta^4=-1\),
\[
\boxed{
(\rho_1,\rho_2,\rho_3)
=(\zeta^{-\gamma},-1,-1).
}\tag{8}
\]
In particular, only \(\rho_1\) varies, through the four primitive
eighth roots of unity. Both of the remaining early layers have the
same exact multiplier defect \(-1\) for **every** such prime, no
matter how large \(v\) is.

This does **not** immediately force a divisible mountain:
the stable full-period translation still needs an independent
nonvanishing theorem or a subgroup-root argument.

## Exact modular checks

The separate script \`audit_finite_defect_multipliers.py\` reproduces
the multiplier formula for selected primes and multiple smooth parts,
without invoking the large integer-ring GCD routine.

For \(u=8\) it checks:

| \(p\) | \(r\) | \(v\) | \((\rho_1,\rho_2,\rho_3)\bmod p\) |
|---:|---:|---:|---|
| 73 | 8 | 1 | (22,72,72) |
| 137 | 8 | 1 | (96,136,136) |
| 7841 | 56 | 7 | (2725,7840,7840) |
| 617 | 88 | 11 | (435,616,616) |
| 233 | 232 | 29 | (97,232,232) |
| 313 | 312 | 39 | (5,312,312) |
| 2393 | 184 | 23 | (58,2392,2392) |

The final two entries in each row are \(-1\bmod p\), as
predicted. These finite checks audit the algebraic formula but do
not substitute for its general proof above.

## Next research direction

For \(u=8\), use the fixed relative multipliers (8) in the
finite-defect transfer and study the resulting first-window
polynomial jointly with the stable one-period drift. The variable
\(\rho_1\) obeys \(\rho_1^4=-1\) and has at most four phases.
This may permit a degree-four cyclotomic elimination without
enumerating the arbitrarily large coprime factor \(v\), **but the
required nonvanishing or subgroup-root conclusion has not been
established**.

# A077187 research handoff

Updated 2026-10-18. The user resumed the research and explicitly requested
**no further subagents**. Work proceeds in the existing PR #8. The unrestricted
all-primes existence problem is **NOT SOLVED**.

## Version and audit provenance

- Checkout: `E:/oeis/a077187`.
- Branch: `research/a077187-smooth-order-v3-le8-20261017`.
- PR: <https://github.com/dongxuelian2/oeis-papers/pull/8>.
- Original paused checkpoint: `5e5265c` (full prior handoff retained in Git).
- First updated PR merged at `bff7e96`; next update inspected and integrated
  through `dea3a4d`, whose source parent is `19af679`.
- Local pre-integration checkpoint: `1cfefd2`.
- The spectral audit was completed before the no-subagent instruction;
  all later integration, tail derivation and checks were done by the primary
  agent alone. No new agent was started or assigned work after that instruction.

## Closed results and proof boundaries

PROVED means a written algebraic proof; COMPUTATION_CERTIFIED means a
finite exact computation with a sufficient coverage bound. CONDITIONAL
and EXPERIMENTAL statements are not promoted to theorems.

1. **PROVED: arbitrary-order stable affine dynamics.** A valid period is
   `T=lcm(r,ord_v(10))` for `r=u*v`, `u=2^a*5^c`, `(v,10)=1`. Nonzero
   drift implies a witness at `10^(jT)` or `10^(jT)+1`, `1<=j<=p`.
   Small exceptions 3 and 11 are handled directly.
2. **PROVED: reduced spectral phase.** Put `delta=gcd(v,9)`, `t=v/delta`,
   `ell=lcm(t,ord_t(10))`, `g=gcd(r,ell)`, `m=r/g`. A stable block of
   length `m*ell` compresses into `ell` cosets in `Q(zeta_g)`. Stable
   multipliers generate exactly `mu_t`; the cumulative phase has period
   `ell`. This generalizes the updated PR's nine-torsion lift.
3. **PROVED: all u dividing 20, with arbitrary v.** Only the first layer
   differs from its stable continuation. After p blocks the drift cancels
   and the first-window equation is a square with a root in `<10>`.
   The explicit witness is `k=10^(pT)+n`,
   `n=(9*10^T-10) mod r`. This is now integrated in the spectral paper.
4. **PROVED: all v dividing 9.** Elementary invariant `U+V=9/100`.
5. **PROVED / COMPUTATION_CERTIFIED: all v dividing 99.** For
   `r=11*3^b*2^a*5^c`, `b<=2`, odd a=0 has an explicit nonzero invariant
   `11*z*U-9*V=909*(z+1)/100`. Even a>=1 reduces to ten fixed quadratic
   norms and 11385 exhaustive index checks, all raw gcds 1. The earlier
   remote certificate is retained as an independent computation; its
   counts 3850 and 3757 include the odd branches, explaining the difference.
6. **PROVED: exact higher-b boundary.** The updated PR proves
   `ord(A_(d+22*3^t)/A_d)=3^max(b-2-t,0)`. Thus for b>=3 the existing
   22-phase mechanism cannot be reused unchanged. This is not an OEIS
   counterexample.
7. **PROVED: tail-gauge reduction.** After cancelling the current layer
   multiplier, only later defect phases remain. The first window depends
   on phase order `u/gcd(u,20)`; a general d-th window has the exact
   tail order given in `zero_drift_continuation_2026-10-18.md`.
8. **COMPUTATION_CERTIFIED obstruction to three fixed windows.** For u=8,
   all three models are rational. Exact squareclass independence plus
   Chebotarev supplies a set of primes of density 1/128 for which their
   discriminants are all nonsquares. At p=617 this is checked directly.
   This concerns the first three windows after p blocks; it does not
   refute a statement conditional on actual zero drift or the all-primes
   conjecture. The written proof states all these restrictions.

## Integration and checks

The current paper is `fixed_v_spectral_families.tex` and its PDF. It includes
reduced phases, explicit Fourier sums, odd/even proof separation, the u|20
witness, the existing v=7 theorem, and the new sharp 3-adic boundary.
README now leads with the audited current scope instead of an unsupported
cumulative lower-stage claim. `main.tex` remains the historical stage-8 paper.

Completed local checks:

- `certify_involutive_families.py`: all 20 explicit coordinate identities,
  ten quadratic norms, complete counts `[3887,3796,3702]`, every gcd 1.
- `audit_reduced_spectral.py`: 20 selected independent phase/coset/full-layer
  identities; these are consistency checks, not an infinity proof.
- Updated PR `certify_fixed_v33_v99.py`: all 3850+3757 indices, every gcd 1.
- Updated PR `audit_fixed_v33_v99.py`: 15 full-layer comparisons and
  252 exact 3-adic defect checks.
- `zero_drift_tail_gauge_2026_10_18.py --examples --symbolic`: seven specified
  prime comparisons in all three windows, the p=617 obstruction, and all
  56 rational squareclass tests.
- The existing v=7/v=11 norm scripts and independent field audits passed
  the separate spectral audit; no large stage-8 rerun was needed.
- Updated manuscript compiled twice with pdflatex and its rendered pages
  were visually inspected. No unresolved references or overfull boxes.

The updated PR source commit `19af679` has successful nine-torsion and PDF
jobs (runs 39101285574 and 39101285587). Its PDF bot head `dea3a4d` has
`action_required` PR runs, which are not mathematical test failures.
A new reduced-phases CI workflow reproduces the new scripts. Later CI
status must be checked on the actual pushed revision.

## Remaining mathematical task

No proof yet establishes nonzero drift for arbitrary v, nor subgroup-root
existence conditional on actual zero drift when u does not divide 20.
The first-window phase reduction does not force a root, and using three
fixed windows is now provably insufficient without additional structure.
A successful continuation must use a relation imposed by actual zero drift,
a uniform phase-cancellation mechanism, or a different witness construction.
Do not default to b=9, larger prime scans, or additional numerical cutoffs.

The original stage-8 arithmetic audit is in `audit_certificates.md`.
The b<=7 certificate package is still absent; the local coefficient bridge
in `general_dynamics.md` repairs the derivation but not those missing data.
The historical cumulative claim is therefore not a closed proof supplied
by this checkout. Earlier counterexamples and failed routes remain recorded
in `zero_drift.md` and the new tail note.

Reproduction uses Python 3 with SymPy; the tail checks use only the standard
library. See README for exact commands. A final all-primes theorem has not
been claimed, and the goal must not be marked complete.

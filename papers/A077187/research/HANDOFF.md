# A077187 research checkpoint

**Status: PAUSED at the user's explicit request, 2026-10-17 (Asia/Shanghai).**
The unrestricted all-primes existence problem is **NOT SOLVED**. This checkpoint
preserves completed mathematics and the exact outstanding work; it is not an
all-primes theorem or a replacement for the existing paper.

## Location and provenance

- Repository checkout: `E:/oeis/a077187` (a separate Git worktree).
- Branch: `research/a077187-smooth-order-v3-le8-20261017`.
- Audited baseline: `a77866a4a34e83d6ad7c4f17c9ee07184864c31d`.
- Existing PR: <https://github.com/dongxuelian2/oeis-papers/pull/8>.
- Mission file: `C:/Users/29848/.codex/attachments/e2328e7e-cc1c-4585-84aa-917b50841382/goal-objective.md`.
- The existing `main.tex`, `main.pdf`, README and certificates are unchanged.
  The new work is saved under `research/`; manuscript integration was interrupted
  before it began. No new PR, push, or publication was performed.

## Completed mathematical results

Use the proof-status vocabulary requested in the mission: PROVED means a
written mathematical derivation, COMPUTATION_CERTIFIED means a finite exact
certificate with its coverage argument, CONDITIONAL means an unproved
hypothesis remains, EXPERIMENTAL means finite tests only, and REFUTED means an
exact counterexample is supplied.

1. **PROVED: general eventual affine period.** Write
   `r=ord_p(10)=u*v`, `u=2^a*5^c`, `gcd(v,10)=1`, and set
   `T=lcm(r,ord_v(10))`, with `ord_1(10)=1`. The full digit-layer maps
   repeat after T beyond the initial transient, and their T-layer product is
   a translation. This gives the correct general replacement for the former
   smooth-order period r. See `general_dynamics.md`, Sections 1-3.

2. **PROVED in the research notes, pending manuscript integration: a new
   unrestricted-odd-part subfamily.** Every prime with
   `v_2(ord_p(10)) <= 2` and `v_5(ord_p(10)) <= 1` has a divisible mountain.
   No restriction is imposed on any other prime factor or exponent of the
   order. The crucial fact is `20 | 9*e*10^(e-1)` for every `e>=2`:
   only the first layer differs from its periodic continuation. If rho is
   the ratio of the continued and actual first-layer multipliers, repeating
   the periodic translation p times leaves the explicit state
   `((rho^(-1)-1)*10/81, (rho-1)/81)`. In the following window,

   \[
   M(10^{pT}+n)/H_n
     =\frac{(10z-\rho)^2}{81\rho z},\qquad z=10^n,
   \]

   where `H_n` denotes the nonzero power of 10 used to normalize that
   mountain. Since `rho` belongs to `<10>`, choose
   `n = (9*10^T-10) mod r`, `0 <= n < r`. This is an explicit witness.
   The argument using 81 is for `p!=3`; `M(3)=12321` handles 3.
   This proof was independently examined by the dynamics and certificate
   audit agents. Consult their final notes for exactly which finite checks
   were completed; the saved witness self-test initially covered `u|10`,
   while the independent audit also checked 75 primes below 500 covering
   all six smooth parts `1,2,4,5,10,20` before the pause.

3. **PROVED: the entire smooth-order family with `v_3(r)<=2`.** Once the
   transient ends, all layer multipliers are 1. The sum of the two drift
   coordinates in one r-block is `9/100`, nonzero for `p!=3`.
   The exceptional small primes have direct witnesses. No old certificate
   package is needed for this result.

4. **PROVED: the missing smooth-order coefficient bridge.** The complete
   derivation from digit-layer recurrences to the quadratic drift formulas
   used by `scalar_reference.py` and the integer group-ring coefficients is
   now in `general_dynamics.md`, Section 4. This repairs a missing proof
   dependency in the baseline stage-8 manuscript at the research-note level.

5. **PROVED: exact window criteria.** For `q=10^e!=1`, the normalized
   mountain is `a*z+b/z-2q/(q-1)^2`, `z in <q>`. The apparent independent
   parameter `n mod p` cancels. For `q=1`, it is `k^2+C_e+Y_e` when
   expressed in the layer's end state. These formulas expose the actual
   zero-drift obstruction; a long window alone does not force a solution.

## Audited computation and exact counterexamples

- Stage-8 certificate arithmetic: no error was found. All 486 files and row
  conditions were inspected; five norms, one full one-shot GCD, three direct
  decimal drift vectors, and 30 small independent cyclotomic resultants
  were recomputed successfully. The full 486 expensive computations were
  not repeated in this session. Details are in `audit_certificates.md`.
- The committed `verify_all.py` alone does not recompute all GCDs or norms.
  The complete workflow does regenerate them before running that script.
- `independent_relative_check.py`, linked by the baseline README, is absent.
- The cumulative baseline `b<=7` claim has no complete prior-stage proof
  package in this checkout. Do not silently promote it to a closed proof.
- **REFUTED:** period r for arbitrary orders. At `p=43,r=21`, successive
  r-block increments differ; the correct T is 42. This does not refute
  period r for smooth orders.
- **REFUTED:** every `q=1` window contains a zero. For `p=11,e=2`, the
  normalized polynomial is `k^2+9`, which has no root modulo 11. This does
  not refute the conditional assertion about a genuine zero-drift orbit.
- **REFUTED:** all possible initial states are covered by one stable
  period's zero lines. At `p=37,r=T=3`, at most 25 affine lines are available,
  too few to cover the 37-by-37 affine plane. Actual reachable states matter.
- **EXPERIMENTAL:** no genuine zero drift was found among primes from 7
  through 1000. This was not used as a universal proof, and the bound was
  not continually increased.

## CI state verified during this session

- Dedicated certificate workflow:
  <https://github.com/dongxuelian2/oeis-papers/actions/runs/39037140817>
  **success**, on source commit `51c5b046a44e470ef578e15efa480d2a4d8e0460`.
  Its listed steps regenerated all norms, ran the GMP sieve and verifier,
  compiled the PDF, and committed the output as the audited baseline.
- Latest PR-triggered generic workflow:
  <https://github.com/dongxuelian2/oeis-papers/actions/runs/39037822180>
  **action_required**, with no jobs. This workflow targets a different
  paper, `papers/A075000-A075002`, and must not be described as an A077187
  mathematical check.
- The new research notes and checks have not been run on GitHub Actions.

## Files and reproduction

- `general_dynamics.md`: complete recurrence, period and coefficient proofs.
- `general_dynamics_check.py`: independent binary geometric-moment checks,
  direct window checks, and the exact p=43 counterexample.
- `zero_drift.md`: new subfamily construction, failed routes and remaining
  obstruction; `zero_drift_probe.py` preserves its completed checks.
- `audit_certificates.md`: independent arithmetic and new-theorem audit.

The available Python with SymPy 1.14.0 and NumPy 2.2.5 is
`C:/Users/29848/AppData/Local/Programs/Python/Python313/python.exe`.
From `papers/A077187/research`, the completed checks can be rerun with:

```text
python general_dynamics_check.py
python zero_drift_probe.py --selftest
```

## Outstanding work when the user resumes

1. Consolidate and review the u-divides-20 theorem and its precise explicit
   witness in a single manuscript proof; record the independent audit.
2. Integrate the already derived smooth-order bridge and correct the README
   scope, dead link and standalone-verifier description. Recompile and
   visually review the paper only after those edits.
3. The all-primes gap remains for orders whose 2/5 part does not divide 20,
   outside the separately established smooth subclasses. Multiple initial
   exceptional layers no longer yield the single square factorization
   automatically. Neither universal nonzero drift nor universal solvability
   of a periodic window has been proved for those cases.
4. Preserve the user's priority: seek a general mechanism or a strictly
   smaller obstruction, not another finite b-layer or a larger prime scan.

**Stop reason:** the user explicitly requested a pause and a saved checkpoint.
No mathematical success claim should be inferred from ending this session.

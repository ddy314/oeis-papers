# OEIS A069862: universal existence and exact least-length families

**Authors:** Qichao Wang (Hebei University of Technology); Daoyu Dong / 董道豫 (University of Electronic Science and Technology of China).

## Proven theorems

For A069862, let a(n) be the **minimum** k for which n divides the decimal concatenation (n+1)||...||(n+k).

1. **For every n>=1, infinitely many lengths k work.** The self-contained prime-power lifting proof gives an explicit bound and a deterministic witness algorithm.
2. For D = digits(n+1), if n divides 10^D, then **a(n)=n**. In particular a(10^r)=10^r for every integer r>=0.
3. For every j>=0 and n=(10^(6j+3)+1)/7, **a(n)=2n-1**. In particular a(143)=285.
4. If n>1 is an odd prime power, n divides 10^digits(n+1)-1, and 10^digits(n+1)>=2*n, then **a(n)=n-1**.

All-index **existence is proved**, with the uniform bound **a(n) < 10^n - n for n>=2** and an exact algorithm for every minimum (at most n^3 modular transitions plus n binary block jumps). Exact minimality is proved for the specified families; no general closed form for the minimum is claimed. The lifting method extends the repository's A075002 proof, with the missing shifted-prefix 3-adic step proved explicitly.

## Existing work (not claimed as original)

The complete classification of n with a(n)=2 is equivalent to OEIS [A069860](https://oeis.org/A069860), whose formula was recorded by **David Wasserman in 2005**. The original draft had inadvertently treated that characterization as new; the revised article now credits the earlier work and excludes it from novelty claims.

## Reproducibility

- [main.tex](main.tex) — fully typeset mathematical paper.
- [main.pdf](main.pdf) — earlier compiled article; **not rebuilt for this continuation**, in this source-only continuation. The TeX source and proof below contain the new results.
- [existence.tex](existence.tex) — self-contained all-index theorem, local shift lemmas and capacity bound.
- [least.py](least.py) — exact all-index minimum algorithm with a proved stopping bound.
- [verify_existence.py](verify_existence.py) — constructive witnesses and independent exact evaluation.
- [verify.py](verify.py) — exact-integer regression checks (finite checks are only corroborative).

Run `python3 verify.py`, `python3 verify_existence.py`, and `python3 least.py --audit`. Compute any term with `python3 least.py 37 451`.

The minimum algorithm agrees with every entry in the [OEIS table for n=1..10000](https://oeis.org/A069862/b069862.txt), downloaded October 22, 2026 (SHA-256 `3ec25d25a94e401eb722ffaf92c878409afa8a330fb7f4fbe6867f524e628f0b`). Its first 1000 outputs are additionally compared with direct, unskipped concatenation.

The existence audit checks 12,510 direct recurrence cases, all n=1..250, and nine additional prime-power/mixed-modulus cases. All 259 constructed witnesses are independently recomputed by an exact geometric-derivative formula; the largest endpoint has 343 decimal digits. These finite checks validate the implementation, while the written proof establishes the universal claim.

Compile: pdflatex -interaction=nonstopmode -halt-on-error main.tex (twice).

## Suggested OEIS formula, not yet posted

a(n)=n if n divides 10^digits(n+1). Also a((10^(6j+3)+1)/7)=2*(10^(6j+3)+1)/7-1 for j>=0. - Wang and Dong (2026).

No claim of journal acceptance or exhaustive prior-art review is made.

# OEIS A069862: two infinite exact least-length families

**Authors:** Qichao Wang (Hebei University of Technology); Daoyu Dong / 董道豫 (University of Electronic Science and Technology of China).

## Proven theorems

For A069862, let a(n) be the **minimum** k for which n divides the decimal concatenation (n+1)||...||(n+k).

1. For D = digits(n+1), if n divides 10^D, then **a(n)=n**. In particular a(10^r)=10^r for every integer r>=0.
2. For every j>=0 and n=(10^(6j+3)+1)/7, **a(n)=2n-1**. In particular a(143)=285.
3. If n>1 is an odd prime power, n divides 10^digits(n+1)-1, and 10^digits(n+1)>=2*n, then **a(n)=n-1**.

These results prove both **existence and exact minimality** for the specified families. They do **not** prove existence or a closed form for all n.

## Existing work (not claimed as original)

The complete classification of n with a(n)=2 is equivalent to OEIS [A069860](https://oeis.org/A069860), whose formula was recorded by **David Wasserman in 2005**. The original draft had inadvertently treated that characterization as new; the revised article now credits the earlier work and excludes it from novelty claims.

## Reproducibility

- [main.tex](main.tex) — two-page, fully typeset mathematical paper.
- [main.pdf](main.pdf) — compiled article, built and checked by the repository workflow.
- [verify.py](verify.py) — exact-integer regression checks (finite checks are only corroborative).

Run: python3 verify.py

Compile: pdflatex -interaction=nonstopmode -halt-on-error main.tex (twice).

## Suggested OEIS formula, not yet posted

a(n)=n if n divides 10^digits(n+1). Also a((10^(6j+3)+1)/7)=2*(10^(6j+3)+1)/7-1 for j>=0. - Wang and Dong (2026).

No claim of journal acceptance or exhaustive prior-art review is made.

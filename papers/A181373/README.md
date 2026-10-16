# A181373: circular Champernowne divisibility

**Author:** Qichao Wang (Hebei University of Technology)  
**Date:** 2026-10-16  
**Status:** complete constructive proof, submitted for code/math review; not yet independently refereed or submitted to OEIS.

## Result

Let (C(m)) be the decimal concatenation of (1,2,ldots,m). For every prime (p\notin\{2,5\}) there exist **infinitely many** (m) such that (p\mid C(m)) and every cyclic **digit** rotation of (C(m)) is divisible by (p). No such (m) exists when (p=2) or (5). Therefore the conjecture in [OEIS A181373](https://oeis.org/A181373) is proved: **A181373(n) > 0 if and only if n is not 1 or 3**.

For every prime (p\ge7) the paper gives the explicit bound

[
m\le 10^{p-1}+p(p-1)-1,
]

with an optional bound in terms of (r=\operatorname{ord}_p(10)):

[
m\le 10^{2r}+pr-1.
]

The statements concern existence, **not** a closed formula for each minimum.

## Constructing a witness

Given prime (p\ge7), set (r=p-1), (L=10^{p-1}), (H=D(L-1)), where (D(k)) counts the digits in (1\Vert\cdots\Vert k). Let (\delta\in[0,r-1]) satisfy (\delta\equiv-H-1\pmod r), and put (m_0=L+\delta). Choose

[
j\equiv-9C(m_0)\pmod p,\qquad0\le j<p.
]

Then (m=m_0+jr) is a witness. The key identity is

[
C(m+r)-C(m)\equiv-r/9\pmod p
]

for the relevant constant-digit-length block. All (p) candidate residues are distinct, while the total digit count of each candidate is a multiple of (p-1).

## Files and validation

- [main.tex](main.tex): self-contained LaTeX article, including bibliographic references and complete proof. Runs with standard `pdflatex` (no BibTeX dependency).
- [verify.py](verify.py): independent modular matrix evaluator and published-term cross-check.
- A compiled three-page PDF is supplied with the associated ChatGPT response; it is reproducible from `main.tex`.

To verify:

```sh
python verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Verification covers 12 published minimal terms, independent literal concatenation comparisons, and the formula and witness for the 23 primes in the range 7 to 101. Finite checks are supplemental; the unconditional proof is in the paper.

## Sources

- [A181373](https://oeis.org/A181373), [A007908](https://oeis.org/A007908), [A058183](https://oeis.org/A058183).
- [Ripà--Dalmasso (2012)](https://nntdm.net/volume-18-2012/number-1/29-48/), *Patterns related to the Smarandache circular sequence primality problem*.
- [Ripà (2025)](https://doi.org/10.5281/zenodo.17382562), a subsequent note on modular patterns.
- [Earlier OEIS paper](../A075000-A075002/), which addresses different divisibility questions; the A181373 proof is independent.

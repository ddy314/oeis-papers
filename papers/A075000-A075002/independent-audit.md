# Independent audit: A075000, A075001, and A075002

## Audit verdict

**FULLY CLOSED mathematically.**

The existence claims for A075001 and A075000 are valid. The stated
A075002 prime-power theorem is valid, including the exceptional cases
3 and 9. The remaining \(3^a\) and arbitrary-composite frontier is
closed by a new block-shift and ordered-prime synchronization proof.

## v1.0.2 literal-statement follow-up

The v1.0.1 source had two local statements whose intended fixed-block
context was not part of their literal hypotheses: Lemma 4.2 called
\(p^e\operatorname{ord}_{p^e}(B)\) a global state period, and Corollary
4.4 stated the \(3\)-adic period and three-way lift without explicitly
covering every candidate interval.  The theorem proof was not invalidated,
because it already chose one sufficiently long block, but those local
statements were under-specified across digit boundaries.

Version v1.0.2 repairs them by making the fixed-block condition explicit,
quantifying the \(3\)-adic period exponent, applying the block-shift lemma
to every \(tL\), and writing the first and higher \(p\)-adic affine sweeps
explicitly.  The fresh literal audit found no additional false or
under-hypothesized proposition, theorem, lemma, or corollary.  The
temporary checklist used for that audit is not part of the release.

## Source-artifact limitation

The requested file Divisibility_of_Concatenated_APs_A075001_A075000.pdf
was not present in the workspace or attachment directory. The only supplied
artifacts were two 247 by 1280 JPEG montages, each containing four reduced
pages. They are not legible enough for a line-numbered textual audit.
Therefore this report audits every mathematical claim and edge case specified
in the task from first principles, but does not pretend to certify
word-for-word fidelity to an unavailable PDF.

## A075001 / A075000 audit

### Simultaneous choice of digit length

Pass. With

\[
n=2^\alpha5^\beta m,\qquad(m,10)=1,
\]

choose \(d\) simultaneously:

1. divisible by \(\operatorname{ord}_m(10)\) when \(m>1\);
2. at least \(\max(\alpha,\beta)\);
3. large enough that the common-digit window contains a complete
   residue system modulo \(2^\alpha5^\beta\).

The admissible multiples of the order are unbounded, so no circular
dependence occurs.

### Digit-window existence of k

Pass. The exact legal interval is

\[
[10^{d-1},10^d-n],
\]

not \([10^{d-1},10^d-1]\). Requiring at least
\(2^\alpha5^\beta\) consecutive integers guarantees a representative
of \(k\equiv1-n\) modulo the decimal-smooth part.

### q=1, m=1, and parity edges

Pass with explicit conventions. When the coprime factor \(m=1\), the
order condition is vacuous. When the smooth factor is 1, the endpoint
residue condition is vacuous. For
\(m\mid n(n-1)/2\), the proof must split parity:

- if \(n\) is odd, \((n-1)/2\) is integral and \(m\mid n\);
- if \(n\) is even, odd \(m\mid n/2\).

The case \(n=1\) is separately witnessed by \(k=1\).

### The 2-adic and 5-adic step

Pass after making the base-smooth factor explicit. Once
\(d\ge\max(\alpha,\beta)\), every positive power of \(10^d\)
vanishes modulo \(2^\alpha5^\beta\); only the rightmost block remains.
This yields exactly \(k+n-1\), with no reversed exponent.

### Concatenation convention

Pass under equation (1) of the result note: the newest/rightmost term has
exponent zero. Reversing this convention changes the smooth-part
congruence and is not harmless.

### Does A075000 follow exactly?

Yes. Existence alone is insufficient unless minimality is addressed.
For fixed \(n\), the concatenation \(C_n(k)\) is strictly increasing
in \(k\), including across powers of ten. Thus the smallest divisible
concatenation is attained at A075001(n), and division by \(n\) gives
the smallest positive multiplier in A075000.

## A075002 prime-power theorem audit

### 2-powers and 5-powers

Pass by the terminal-block argument. They are not part of the unit affine
orbit because 10 is not invertible modulo these primes.

### p^a for p not in {2,3,5}

Pass. Write

\[
\operatorname{ord}_{p^a}(10)=p^s h,\qquad p\nmid h,
\]

and choose \(d=p^s(1+t\operatorname{ord}_{p^a}(10))\). Then
\(10^d\) has order \(h>1\); hence both \(10^d-1\) and \(h\)
are units modulo \(p^a\). For the translation increment \(T\),

\[
(10^d-1)T\equiv-h\pmod {p^a},
\]

so \(T\) is invertible. The digit-block bound is obtained by taking
\(t\) sufficiently large. This checks the order reduction,
translation invertibility, and block capacity separately.

### 3 and 9

Pass directly: \(P(2)=12\) and the digit sum of \(P(8)=12345678\)
is 36.

## New closure of the old frontier

### Powers 3^a

The failed unit-translation argument is genuinely structural:
\(10^d\equiv1\pmod3\) for every \(d\). The replacement is the
block-shift congruence

\[
P(k+L)-P(k)
\equiv Lk+\frac{L(L+1)}2
\pmod {3^{v_3(L)+1}}.
\]

Taking \(v_3(L)=a\) turns a root modulo \(3^a\) into a three-choice
unit lift modulo \(3^{a+1}\). This proves every \(3^a\), not merely
an additional infinite subclass.

### Arbitrary composites and one common k

A single global order can fail: the verifier finds the first failure at
689. The successful construction processes odd primes increasingly.
Each completed smaller prime power supplies an explicit state period;
all prime factors of that period are no larger than the completed prime.
Consequently period multiplication preserves previous roots and remains
a unit at the next prime. Prime roots and all lifts are therefore
installed at the same endpoint. The endpoint is kept divisible by the
2-5 part throughout.

This is synchronization of one actual representative, not CRT applied
to unrelated local witness indices.

## Imported-method review

The two imported repositories concern a different exact-lift problem,
so none of their local theorems can be transplanted as a premise. Their
methodological lessons were used as follows:

- Euclidean block folding and circular radix phase: normalize a long
  decimal recurrence to a fixed-block transition before using orders.
- Exact representative / inverse locks: retain one endpoint throughout;
  do not confuse compatible residue classes with a realized digit-window
  representative.
- Hensel and valuation ledgers: separate the exceptional 3-adic
  non-unit branch from the unit orbit.
- Synchronization records: require a state period preserving the whole
  previously installed state, not separate local witnesses.

Floor-sum certificates were inspected as a possible way to control digit
boundaries but were unnecessary after the one-block capacity argument.

## Computational audit

Command:

    python verification/verify_concatenation_divisibility.py

Scope:

- 2730 matrix jumps cross-checked against a separate literal recurrence;
- A075002 OEIS regression for n=1..60;
- A075001 constructive witnesses for n=1..2000;
- 85 exceptional 3-adic congruence cases;
- 63 unit-translation lift cases;
- 34 direct checks of the paper's prime-power construction;
- an exhaustive naive-global-orbit obstruction scan for Q<5000,
  gcd(Q,30)=1;
- full constructive A075002 witnesses for n=1..500;
- explicit composite synchronization tests at
  689, 1027, 1673, 3403, and 4823.

The checker uses modular 3 by 3 transition matrices and does not trust
decimal big-integer concatenation.

## External novelty audit

Checked 2026-09-10:

- OEIS A075000 still says its nonzero existence is conjectural.
- OEIS A075001 still says existence of k is conjectural.
- OEIS A075002 still says well-definedness for every n is conjectural.
- The current arXiv record for Luca--Teguia Tabuguia,
  Concatenations of Terms of an Arithmetic Progression (v3, 2025),
  describes explicit formulae and non-holonomicity, not these
  divisibility closures.

Searches also found older recreational literature on periodic
concatenation divisibility, but no proof of A075002 for every modulus.
This supports potential novelty but is not a claim of exhaustive
literature priority.

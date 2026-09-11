# Mathematical audit record: A075000, A075001, and A075002

Release reviewed: a075000-a075002-v1.0.3

Review date: 2026-09-11

## Verdict

No fatal mathematical error was found in the current proof after literal-statement
and computational regression review.  This record is a cautious audit of the
published statements and their supporting checks; it does not claim that
undiscovered errors are impossible or that the review was an external human
certification.

## Release history

The v1.0.1 source had two local statements whose intended fixed-block context
was not part of their literal hypotheses: Lemma 4.2 called
\(p^e\operatorname{ord}_{p^e}(B)\) a global state period, and Corollary 4.4
stated the \(3\)-adic period and three-way lift without explicitly covering
every candidate interval.  The main theorem's construction already selected
one sufficiently long block, but those local statements were under-specified
across digit boundaries.

Version v1.0.2 repaired those statements by making the fixed-block condition
explicit, quantifying the \(3\)-adic period exponent, applying the block-shift
lemma to every candidate shift, and writing the first and higher \(p\)-adic
affine sweeps explicitly.

Version v1.0.3 makes the remaining release-facing distinctions explicit:
the abstract restricts unit translations to \(p\notin\{2,3,5\}\), Proposition
2.1 distinguishes an integer congruence from finite-window admissibility,
Corollary 2.4 gives a digit-length and lexicographic monotonicity proof, and
the audit record and provenance language use neutral names.

## A075001 and A075000

For the even-base arithmetic-progression theorem, write
\(n=qm\), where \(q\) contains exactly the prime factors of \(n\) that
divide the even base and \((m,\beta)=1\).  The digit length can be chosen
simultaneously large enough for the base-smooth part, a multiple of the
coprime multiplicative order, and a nonempty common-digit window.  In the
decimal consecutive case the legal starting interval is
\([10^{d-1},10^d-n]\), and a window containing a complete residue system
modulo \(q\) supplies the required endpoint residue.

The cases \(q=1\), \(m=1\), and \(n=1\) are covered by the stated
conventions.  The reduction modulo \(m\) is valid after separating the
parity of \(n\): for odd \(n\), \(m\mid n\), while for even \(n\) the
full \(2\)-part of \(n\) lies in \(q\), so \(q/2\) is integral.  The terminal
block handles the base-smooth factor because \(B\equiv0\pmod q\).

The quotient assertion for A075000 also needs minimality, not only
existence.  For \(k_2>k_1\), the corresponding terms of the two ordered
tuples are strictly increasing, so their digit lengths are coordinatewise
nondecreasing.  If the total concatenated lengths differ, the second string
is longer and hence larger.  If the totals agree, all corresponding block
lengths are equal by those coordinatewise inequalities; the first differing
digit is therefore in an equal-length decimal block and is larger for
\(k_2\).  Thus \(C_n(k_2)>C_n(k_1)\), including digit-boundary crossings,
and division by \(n\) preserves the ordering.

## Local lifting

For \(p\notin\{2,3,5\}\), the unit-translation and fixed-block state-period
lemmas apply because \(p\nmid B(B-1)\).  With
\(h=\operatorname{ord}_p(B)\), the geometric identity gives
\((B-1)T_h\equiv-h\pmod p\), so the translation coefficient is a unit.
The period \(p^e\operatorname{ord}_{p^e}(B)\) preserves both the prefix state
and the endpoint modulo \(p^e\) inside one fixed digit block, and all its
prime divisors are at most \(p\).

The primes \(2\) and \(5\) are handled by the terminal block.  The prime
\(3\) is excluded from the unit argument because \(10^d\equiv1\pmod3\);
the separate block-shift lemma and Corollary 4.4 handle \(3\)-power lifting.
The direct witnesses \(P(2)=12\) and \(P(8)=12345678\) cover \(3\) and \(9\).

The two unrestricted-period regression examples remain intentionally negative:
the \(p=7\) period \(42\) from \(k=1\), and the \(3^3\) shift \(54\) from
\(k=2\), cross a decimal digit boundary.  They therefore do not satisfy the
fixed-block hypotheses and do not contradict the corrected conditional lemmas.

## Explicit \(3\)-adic period recheck

Let \(e\ge1\) and \(L=m(2\cdot3^e)\) with arbitrary \(m\ge1\).  Then
\(a=v_3(L)=e+v_3(m)\ge e\), so Lemma 4.3 applies whenever the entire
appended interval stays in the fixed block and gives
\[
P(k+L)-P(k)\equiv Lk+\frac{L(L+1)}2\pmod{3^{a+1}}.
\]
Both terms on the right are divisible by \(3^e\): \(Lk\) is immediate, and
\[
\frac{L(L+1)}2=(m3^e)(L+1)
\]
because \(L=2m3^e\).  Since \(L\equiv0\pmod{3^e}\) as well, the deduction
\(P(k+L)\equiv P(k)\pmod{3^e}\) and \(k+L\equiv k\pmod{3^e}\) is valid for
every \(m\ge1\).  This also verifies the claimed positive-multiple state
period, not only the base period \(2\cdot3^e\).

The three-way lift uses \(L=\operatorname{lcm}(2\cdot3^a,R)=2c3^a\)
with \(3\nmid c\).  For \(t=1,2\), \(v_3(tL)=a\), and division of the
block-shift congruence by \(3^a\) gives the unit coefficient
\(tc(2k+1)\pmod3\).  A root modulo \(3^a\) forces
\(k\equiv0\) or \(2\pmod3\), so \(2k+1\) is a unit; the three choices
therefore give exactly one lift modulo \(3^{a+1}\).

## Capacity and state invariant recheck

The construction uses
\[
H_0=
\begin{cases}
2\cdot3^e,&e>0,\\
1,&e=0,
\end{cases}
\qquad
H_i=\operatorname{lcm}\!\left(H_{i-1},
p_i^{e_i}\operatorname{ord}_{p_i^{e_i}}(10)\right),
\]
and
\[
J_{i,0}=\operatorname{lcm}\!\left(\operatorname{ord}_{p_i}(10),H_{i-1},R\right),
\quad
J_{i,a}=\operatorname{lcm}\!\left(
\operatorname{ord}_{p_i}(10)p_i^a,H_{i-1},R\right).
\]
Here \(H_i\) is formed after prime \(p_i\) is processed, so \(H_{i-1}\)
is the state period already available before \(p_i\) is processed.  Every
quantity in these definitions depends only on \(n\).

The bound
\[
W(n)=
2\sum_{a=1}^{e-1}\operatorname{lcm}(2\cdot3^a,R)
+\sum_{i=1}^r(p_i-1)\sum_{a=0}^{e_i-1}J_{i,a}
\]
includes the largest possible displacement at every three-way and
\(p_i\)-way stage.  Consequently it bounds every candidate endpoint,
not only the branch ultimately selected.

With \(D\) the least common multiple of the relevant
\(\operatorname{ord}_{p_i^{e_i}}(10)\), the choice \(d\equiv1\pmod D\)
gives
\[
10^d\equiv10\pmod{p_i^{e_i}},
\]
so the orders of \(B=10^d\) are exactly the corresponding orders of \(10\).
The choice \(d\ge\max(\alpha,\beta)\) gives \(B\equiv0\pmod R\).
Finally, with \(M_0=R3^{\min(e,1)}\), the strict inequality
\[
9\cdot10^{d-1}>M_0+W(n)
\]
and the least multiple \(k_0\ge10^{d-1}\) imply
\[
10^{d-1}\le k_0\le k_0+W(n)<10^d.
\]
All shifts are forward, so no candidate falls below \(10^{d-1}\).  Thus
every appended interval used by Lemmas 4.1, 4.2, 4.3, and Corollary 4.4
stays in the one fixed digit block, and the terminal-block congruence modulo
\(R\) has its stated hypothesis.

## Literal-statement audit

The Abstract, Proposition 2.1, Theorem 2.2, Corollaries 2.3 and 2.4,
Lemmas 4.1--4.3, Corollary 4.4, Theorem 5.1, and Remark 5.2 were read
with their quantifiers and hypotheses made explicit.  The review attacked
the words “every”, “exactly”, “all”, “period”, “unique”, “arbitrary”,
“away from”, “complete”, “common”, “fixed”, “global”, and “resolves”.

The boundary cases checked were \(n=1\), \(m=1\), \(q=1\), \(R=1\),
\(e=0\), \(e=1\), \(r=0\), pure powers of \(2\), \(3\), and \(5\),
mixed \(2\)-\(3\)-\(5\) moduli, the first odd-prime stage, and higher
\(p\)-adic stages.  No additional fatal or mathematical error was found.
The phrase “endpoint indices” was made explicit in Corollary 4.4 to avoid
confusing divisibility of the indices with divisibility of the prefix values.

## Computational regression

From this directory, run:

    python verify_concatenation_divisibility.py

The recorded checks cover:

- 2730 matrix jumps cross-checked against a literal recurrence;
- the two negative unrestricted-period examples;
- fixed-block state periods and conditional multiples;
- fixed-block \(3\)-adic periods and conditional multiples;
- \(3\)-adic and \(p\)-adic candidate sweeps;
- OEIS A075002 terms for \(n=1,\ldots,60\);
- the A075001 construction for \(n=1,\ldots,2000\);
- the paper's prime-power construction;
- the exhaustive naive-global-orbit obstruction scan for \(Q<5000\);
- the common-index construction for \(n=1,\ldots,500\), including the five
  recorded global-orbit failure moduli.

The two negative unrestricted-period tests are retained deliberately.  Their
shifts cross decimal digit boundaries, so they test the exact scope of the
fixed-block hypotheses rather than weakening those hypotheses.

The verifier is a reproducibility check and is not a premise of the proofs.
No claim of literature-wide priority is made.

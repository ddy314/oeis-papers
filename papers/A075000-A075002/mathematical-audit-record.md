# Mathematical audit record: A075000, A075001, and A075002

Current release: a075000-a075002-v1.0.4

Audit date: 2026-09-11

## Status

No fatal mathematical error was found in the current proof after literal-statement
and computational regression review. This record is a cautious audit of the
published statements and their supporting checks; it does not claim that
undiscovered errors are impossible or that the review is an external human
certification.

## What was checked

The literal statements and quantifiers of the abstract, Proposition 2.1,
Theorem 2.2, Corollaries 2.3--2.4, Lemmas 4.1--4.3, Corollary 4.4,
Theorem 5.1, and Remark 5.2 were reviewed. Particular attention was given
to the words "every", "exactly", "all", "period", "unique", "arbitrary",
"away from", "complete", "common", "fixed", and "global". Boundary cases
included \(n=1\), \(m=1\), \(q=1\), \(R=1\), \(e=0\), \(e=1\), \(r=0\),
pure powers of \(2\), \(3\), and \(5\), mixed \(2\)-\(3\)-\(5\) moduli, the
first odd-prime stage, and higher \(p\)-adic stages.

## A075001 and A075000

For the even-base arithmetic-progression theorem, write \(n=qm\), where
\(q\) contains exactly the prime factors of \(n\) that divide the even base
and \((m,\beta)=1\). The digit length can be chosen simultaneously large
enough for the base-smooth part, a multiple of the coprime multiplicative
order, and a nonempty common-digit window. In the decimal consecutive case
the legal starting interval is \([10^{d-1},10^d-n]\), and a window containing
a complete residue system modulo \(q\) supplies the required endpoint residue.

The cases \(q=1\), \(m=1\), and \(n=1\) are covered by the stated
conventions. The reduction modulo \(m\) is valid after separating the parity
of \(n\): for odd \(n\), \(m\mid n\), while for even \(n\) the full \(2\)-part
of \(n\) lies in \(q\), so \(q/2\) is integral. The terminal block handles
the base-smooth factor because \(B\equiv0\pmod q\).

The quotient assertion for A075000 also needs minimality, not only existence.
For \(k_2>k_1\), the corresponding terms of the two ordered tuples are
strictly increasing, so their digit lengths are coordinatewise nondecreasing.
If the total concatenated lengths differ, the second string is longer and
hence larger. If the totals agree, all corresponding block lengths are equal
by those coordinatewise inequalities; the first differing digit is therefore
in an equal-length decimal block and is larger for \(k_2\). Thus
\(C_n(k_2)>C_n(k_1)\), including digit-boundary crossings, and division by
\(n\) preserves the ordering.

## Local lifting and known failure modes

For \(p\notin\{2,3,5\}\), the unit-translation and fixed-block state-period
lemmas apply because \(p\nmid B(B-1)\). With
\(h=\operatorname{ord}_p(B)\), the geometric identity gives
\((B-1)T_h\equiv-h\pmod p\), so the translation coefficient is a unit.
The period \(p^e\operatorname{ord}_{p^e}(B)\) preserves both the prefix state
and the endpoint modulo \(p^e\) inside one fixed digit block, and all its
prime divisors are at most \(p\).

The corrected local statements require the entire appended interval to remain
in one fixed digit block. The primes \(2\) and \(5\) are handled by the
terminal block. The prime \(3\) is excluded from the unit argument because
\(10^d\equiv1\pmod3\); the separate block-shift lemma and three-way lift
handle powers of \(3\). The direct witnesses \(P(2)=12\) and
\(P(8)=12345678\) cover \(3\) and \(9\).

The verifier retains two intentionally negative regression examples:
\(p=7,d=1,k=1,H=42\), and \(3^3,k=2,\text{shift}=54\). In both cases
the indicated shift crosses a decimal digit boundary. These examples do not
satisfy the fixed-block hypotheses and therefore do not contradict the
conditional lemmas.

## Capacity and state invariant review

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
Here \(H_i\) is formed after \(p_i\) is processed, so \(H_{i-1}\) is the
state period available before the next prime is processed. Every prime
divisor of a completed state period is at most the prime already processed;
this is the invariant that keeps the next translation coefficient a unit.

The displacement bound
\[
W(n)=
2\sum_{a=1}^{e-1}\operatorname{lcm}(2\cdot3^a,R)
+\sum_{i=1}^r(p_i-1)\sum_{a=0}^{e_i-1}J_{i,a}
\]
includes every candidate endpoint examined during the three-way and
\(p_i\)-way sweeps, not only the selected trajectory. With
\(d\equiv1\pmod D\), \(d\ge\max(\alpha,\beta)\), and
\(9\cdot10^{d-1}>M_0+W(n)\), all such endpoints remain in one fixed digit
block. This supplies the hypotheses required by the local lemmas and the
terminal-block congruence.

## Explicit \(3\)-adic recheck

For \(e\ge1\) and \(L=m(2\cdot3^e)\) with arbitrary \(m\ge1\),
\(a=v_3(L)=e+v_3(m)\ge e\). Lemma 4.3 therefore applies whenever the
entire appended interval stays in the fixed block and gives
\[
P(k+L)-P(k)\equiv Lk+\frac{L(L+1)}2\pmod{3^{a+1}}.
\]
Both terms on the right are divisible by \(3^e\): \(Lk\) is immediate, and
\[
\frac{L(L+1)}2=(m3^e)(L+1)
\]
because \(L=2m3^e\). Since \(L\equiv0\pmod{3^e}\) as well, this gives
\(P(k+L)\equiv P(k)\pmod{3^e}\) and
\(k+L\equiv k\pmod{3^e}\) for every \(m\ge1\).

The three-way lift uses \(L=\operatorname{lcm}(2\cdot3^a,R)=2c3^a\)
with \(3\nmid c\). For \(t=1,2\), \(v_3(tL)=a\), and division of the
block-shift congruence by \(3^a\) gives the unit coefficient
\(tc(2k+1)\pmod3\). A root modulo \(3^a\) forces
\(k\equiv0\) or \(2\pmod3\), so \(2k+1\) is a unit; the three choices
therefore give exactly one lift modulo \(3^{a+1}\).

## Computational regression and current verification

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

The two negative unrestricted-period tests are retained deliberately. Their
shifts cross decimal digit boundaries, so they test the exact scope of the
fixed-block hypotheses rather than weakening those hypotheses.

The verifier is a reproducibility check and is not a premise of the proofs.
The current recorded status is **ALL CHECKS PASSED**. This is not an external
human certification and does not claim that undiscovered errors are impossible.

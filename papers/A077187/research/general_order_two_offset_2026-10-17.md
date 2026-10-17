# A077187 — arbitrary-order two-offset criterion (2026-10-17)

**Status: PROVED conditional reduction; unrestricted all-primes existence remains OPEN.** This extends the finite-defect transfer in `finite_defect_transfer_2026-10-17.md`, and does not replace the current PR's smooth-order manuscript.

Define (M(k)=1|2|\cdots|k|(k-1)|\cdots|1). For a prime (p\ge7), (p\ne11), put
[
r=\operatorname{ord}_p(10)=2^a5^cv,quad (v,10)=1,quad
E=1+\max(a,c),quad T=\operatorname{lcm}(r,\operatorname{ord}_v(10)).
]
Use (\operatorname{ord}_1(10)=1). For the usual forward and normalized-reverse endpoint state (S_e=(C_{10^e-1},Y_{10^e-1})), let
[
W=S_{pT},\qquad (U,V)=S_T-W.
]
The affine full-layer maps have period (T) after the initial (E-1) layers. The product of any (T) stable maps has diagonal multiplier 1, so
[
S_{tT}=W+t(U,V)\pmod p\qquad(t\ge1).
]
The finite-defect transfer computes (W) using only (2(E-1)) initial/continued maps, and (S_T) requires only (T) actual layers.

## Theorem: explicit witness from nonzero drift, for arbitrary order

If ((U,V)\ne(0,0)), then for some (1\le t\le p) and (j\in\{0,1\}),
[
\boxed{p\mid M(10^{tT}+j).}
]
**No restriction on prime factors of (r)** is made.

**Proof.** Write (W=(C,Y)), (X=81C+10), (Z=81Y+1), (z=10^j). The normalized residue at (k=10^{tT}+j), multiplied by the invertible (81z), is
[
10Xz^2-20z+Z+81t(10Uz^2+V).
]
The two (t)-slopes for (j=0,1) are proportional to (10U+V) and (1000U+V). Both could vanish only if (990U=0), forcing (U=V=0), since (p\nmid990). With a nonzero slope, solve uniquely for (t\pmod p); choose the representative (1\le t\le p). QED.

## Exact finite criterion in the zero-drift branch

If ((U,V)=(0,0)), then
[
\boxed{\exists k\ge1:p\mid M(k)\iff\exists 1\le k<10^{2T}:p\mid M(k).}
]
Proof: all endpoint states repeat with period (T) once (e\ge T). For any later digit window (k=10^e+j) with (q=10^{e+1}\ne1\pmod p), the normalized residue is (az+bz^{-1}-2q/(q-1)^2) with (z=q^j), periodic in (j) with period dividing (r). For (q=1), the normalized residue equals ((10^e+j)^2+C+Y+10^e-10^{2e}), periodic in (j) modulo (p). Every representative window with (T\le e<2T) has at least (p) offsets, since (p\mid10^r-1) and (T\ge r). Thus every later zero residue appears below (10^{2T}). In both branches any existing witness can be bounded by (10^{pT}+1).

## Resolved negative-control example

For (p=313),
[
r=T=312,quad W=(154,94),quad (U,V)=(198,283),
]
and ((X,Z)=(277,103)). The first (pT)-window quadratic has no root in (\langle10\rangle); nevertheless, at (j=1), the constant is (211) and the slope is (267\pmod{313}), so (t=-211/267=25\pmod{313}). Hence
[
\boxed{313\mid M(10^{7800}+1).}
]
The witness was checked by iterating all 7,800 full digit layers. Numerical cross-checks covered 97 primes below 550, including 74 independent full-layer traversals, and 1,748 generic-window comparisons.

**Remaining gap:** prove nonzero drift for every prime, or prove the existence of a zero residue in all genuine zero-drift periodic orbits. Neither is currently established. The full A077187 conjecture remains open.

# A006063: cube-sum permutations for every n >= 173

**Status:** Computer-assisted complete-proof candidate; requires independent mathematical and certificate review.  
**OEIS:** https://oeis.org/A006063  
**Date:** 2026-10-18.

## Result

For every integer n >= 173, there is a permutation p of {1,...,n} for which i+p[i] is a perfect cube at every index. This resolves the 2018 existence conjecture recorded in OEIS A006063, subject to independent validation of the included certificate. OEIS had already reported computational verification through n=1000; the new ingredient here is an induction that turns a finite verification into an all-n statement.

## Core mathematical argument

**Interval-reflection extension.** If m<n admits a cube-sum permutation and m+n+1 is a cube c, keep the old permutation on 1..m and set p[i]=c-i for i=m+1..n. The latter is a permutation of the new interval and every new sum equals c.

**Cube-gap bound.** For every n>=365, there exists a cube c with n+174<=c<=2n.

* For 365<=n<=555, use c=729.
* For n>=556, choose the first cube k^3>=n+174 (k>=10). From n >= (k-1)^3-173 and the inequality 2((k-1)^3-173)>=k^3, it follows that k^3<=2n.

Consequently m=c-n-1 satisfies 173<=m<n. Strong induction reduces all n>=365 to the 192 finite base cases n=173,...,364.

## Files

- main.tex: self-contained LaTeX research note with three lemmas and the full induction.
- certificates/base_permutations.json: all 192 explicit permutation witnesses, 51,552 integers (ordered by n=173,...,364).
- verify.py: independently checks every witness by exact integer arithmetic; additionally constructs and checks larger examples recursively.
- independent_match.py: separate augmenting-path solver for all 192 base cases; does not read the archived certificates.

## Reproduce

From this directory, with any recent Python 3:

    python verify.py
    python independent_match.py

Both are standard-library-only. The archived permutations, not the matching algorithm, are the finite proof certificate. The second program checks the base family via an independent implementation. No numerical bound on n is imposed by the mathematical induction.

## Qualifications

This is an existence theorem, not a count of permutations or proof of their uniqueness. Novelty relative to non-OEIS literature has not been established. The exact code and finite witnesses are provided for independent scrutiny; this is not a peer-reviewed result. No OEIS entry has been edited.

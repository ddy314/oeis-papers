# Cube-sum permutation classifications (OEIS A006063, A096680, A096904)

**Date:** 2026-10-18  
**Status:** Complete computer-assisted proof candidate, pending independent audit and literature priority check.

We study the number \`P(n)\` of permutations \`p\` of \`{1,...,n}\` such that every \`i+p_i\` is a perfect cube. The results are mathematical theorems conditional only on fully explicit finite integer certificates, whose validation is independently reproducible. No OEIS page has yet been changed.

## Results

1. **Exact A006063 membership.** \`P(n)>0\` for every \`n>=173\`. The 48 positive lengths below 173 are exactly those listed by OEIS; all 124 negative lengths have explicit Hall-obstruction witnesses. Therefore **\`A006063(j)=j+124\` for every index \`j>=49\`**, strengthening the formerly conjectural tail formula (which was stated for indices >=173).
2. **Exact A096680 membership.** \`P(173)=P(174)=1\`, and \`P(n)>=2\` for every \`n>=175\`. Exactly 13 lengths below 173 have multiple valid permutations: \`112,115,116,117,119,124,125,126,127,128,129,130,133\`. Thus **\`A096680(j)=j+161\` for every index \`j>=14\`**.
3. **Quantitative A096904 theorem.** Let \`K(n)=floor(cuberoot(2*n))\` and \`q(n)=max(0,floor((K(n)-27)/6))\`. For every \`n>=173\`,
   
   \`\`\`
   P(n) >= 3**q(n)
   \`\`\`
   
   so **\`log P(n) >= ((2*n)**(1/3) * log(3)/6) - O(1)\`**. This is a genuine exponential-in-cube-root lower bound on the number of distinct cube-sum permutations.

## Mathematical method

**Reflection extension:** If \`p\` is valid on \`{1,...,m}\` and \`m+n+1=c\` is a cube, then extend by \`p[i]=c-i\` for \`m<i<=n\`. Each cube gives a disjoint image family since its last value is \`p[n]=c-n\`. Consequently,

\`\`\`
P(n) >= sum(P(c-n-1) for cubes c with n+2 <= c <= 2*n)
\`\`\`

with \`P(0)=1\` (the empty matching convention).

**Finite certificate compression:** Only the 109 sizes \`173..255\` and \`339..364\` need their own explicit witness. Every size \`256..338\` is reflected from \`m=511-n\`, since \`m+n+1=512=8^3\`. Thus the earlier 192 base-case witnesses reduce to 109 stored primary witnesses; the original 192-row archive remains available for cross-checking. The elementary cube-gap lemma then reduces all sizes \`n>=365\` to smaller solved sizes \`m>=173\`.

**Negative cases:** A subset \`S\` of left vertices is an obstruction when its cube-sum neighbor set \`N(S)\` has \`|N(S)|<|S|\`, by Hall's marriage theorem. This certifies all 124 non-members below 173. At \`n=172\`, there is an explicit 27-left/26-right Hall obstruction, proving the sharpness of the 173 threshold.

**Multiplicity:** For any valid permutation \`p\`, a directed edge \`i -> j\` exists when \`i != j\` and \`i+p[j]\` is a cube. A directed cycle gives another valid permutation by rotating right partners along the cycle. The converse also holds: two distinct perfect matchings differ on alternating cycles, so acyclicity certifies uniqueness.

The 190 base lengths \`175..364\` have explicit cycle witnesses. For \`365..553\`, reflection through \`729\` preserves multiplicity; \`554,555\` have dedicated witnesses, and for \`n>=556\` the cube-gap bound provides a predecessor \`m>=175\`.

**Exponential count:** For \`k=floor(cuberoot(2*n))>=27\`, the three cubes \`k^3,(k-1)^3,(k-2)^3\` give disjoint extensions from \`m_i>=173\`, with \`K(m_i)>=k-6\`. Strong induction gives \`P(n)>=3**q(n)\`.

## Proof artifacts

- [main.tex](main.tex): full paper source; [main.pdf](main.pdf) is produced and committed by the PDF workflow.
- [certificates/core_109.json](certificates/core_109.json): 109 primary existence witnesses.
- [certificates/base_permutations.json](certificates/base_permutations.json): original independent 192-row audit data.
- [certificates/exact_classification_below_173.json](certificates/exact_classification_below_173.json): 48 valid permutations and 124 Hall-deficient sets.
- [certificates/second_solutions.json](certificates/second_solutions.json): alternating-cycle witnesses for 13 early cases, all sizes 175..364, and exceptional sizes 554 and 555.
- [verify.py](verify.py): audit original 192 base cases and recursive witnesses.
- [independent_match.py](independent_match.py): independent augmenting-path generator for the 192 base cases.
- [verify_extended.py](verify_extended.py): audit all new certificates, uniqueness, multiplicity, compact bases, and structural numeric regression tests.

Run, from repository root:

\`\`\`sh
python papers/A006063/verify.py
python papers/A006063/independent_match.py
python papers/A006063/verify_extended.py
\`\`\`

All verifiers use Python's standard library only; certificate checks use integers, sets, and exact comparisons.

## Publication/review boundaries

These are complete mathematical arguments with finite machine-checkable premises, not computational conjectures inferred from a cutoff. However, the work **requires independent review** of the formal lemmas, finite data, and existing literature. We do not claim to have computed exact values of \`P(n)\` beyond the uniqueness cases, nor to have submitted any OEIS entry or journal manuscript. The draft PR is intentionally not marked ready for review.

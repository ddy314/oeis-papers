# A075000-A075002

This paper proves the existence assertions underlying OEIS A075001 and A075000 for every
positive integer, and proves the main result that for every positive integer `n` there is an
index `k` with `n | 123...k`, establishing that OEIS A075002 is well-defined for every `n`.

The proof uses a fixed-digit arithmetic-progression construction, a separate 3-adic block-shift
lift, and increasing-prime state synchronization for the remaining prime powers.

## Reproduction

From this directory, run:

```text
python verify_concatenation_divisibility.py
```

The verifier performs modular transition checks, OEIS regression checks, prime-power checks,
and the common-index construction checks described in `verification.txt`.

The frozen release is [`a075000-a075002-v1.0.0`](https://github.com/dongxuelian2/oeis-papers/releases/tag/a075000-a075002-v1.0.0).

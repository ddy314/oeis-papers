"""Independent verifier for the A075000/A075001/A075002 proofs.

The program never constructs a concatenated decimal integer.  It evaluates
prefixes and fixed-length blocks modulo the requested modulus, using a 3 by 3
transition matrix for fast jumps across long digit blocks.
"""

from __future__ import annotations

from math import gcd, lcm


OEIS_A075002_1_TO_60 = [
    1, 2, 2, 2, 5, 2, 11, 6, 8, 10, 106, 2, 11, 22, 5, 6, 21, 8,
    27, 20, 11, 106, 33, 6, 25, 30, 26, 24, 31, 20, 46, 6, 113, 64,
    45, 36, 21, 64, 11, 20, 3, 24, 19, 128, 35, 68, 8, 6, 53, 50,
    21, 120, 83, 26, 135, 128, 27, 82, 104, 20,
]


def factor(n: int) -> dict[int, int]:
    result: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def order_mod(base: int, modulus: int) -> int:
    assert gcd(base, modulus) == 1
    value = 1
    for h in range(1, modulus + 1):
        value = value * base % modulus
        if value == 1:
            return h
    raise AssertionError("multiplicative order bound failed")


def mat_mul(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
    modulus: int,
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(
            sum(left[i][t] * right[t][j] for t in range(3)) % modulus
            for j in range(3)
        )
        for i in range(3)
    )


def mat_pow(
    matrix: tuple[tuple[int, ...], ...], exponent: int, modulus: int
) -> tuple[tuple[int, ...], ...]:
    result = ((1 % modulus, 0, 0), (0, 1 % modulus, 0), (0, 0, 1 % modulus))
    while exponent:
        if exponent & 1:
            result = mat_mul(result, matrix, modulus)
        matrix = mat_mul(matrix, matrix, modulus)
        exponent >>= 1
    return result


def advance(x: int, k: int, steps: int, digits: int, modulus: int) -> tuple[int, int]:
    """Advance P(k) to P(k+steps), assuming all appended terms have digits digits."""
    if steps == 0:
        return x % modulus, k
    base = pow(10, digits, modulus)
    transition = ((base, 1, 1), (0, 1, 1), (0, 0, 1))
    power = mat_pow(transition, steps, modulus)
    vector = (x % modulus, k % modulus, 1 % modulus)
    out = tuple(
        sum(power[i][j] * vector[j] for j in range(3)) % modulus
        for i in range(3)
    )
    return out[0], k + steps


def prefix_mod(k: int, modulus: int, digits: int | None = None) -> int:
    """Return the residue of 123...k modulo modulus in O(log(k)^2) operations."""
    if modulus == 1:
        return 0
    if k <= 0:
        return 0
    if digits is None:
        digits = len(str(k))
    x = 0
    current = 0
    lower = 1
    for width in range(1, digits + 1):
        start = 1 if width == 1 else lower
        stop = min(k, lower * 10 - 1)
        if stop >= start:
            assert current == start - 1
            x, current = advance(x, current, stop - current, width, modulus)
        if current == k:
            return x
        lower *= 10
    raise AssertionError("incorrect digit count")


def direct_first_witness(modulus: int, limit: int) -> int | None:
    residue = 0
    next_power = 10
    for k in range(1, limit + 1):
        if k == next_power:
            next_power *= 10
        residue = (residue * next_power + k) % modulus
        if residue == 0:
            return k
    return None


def block_residue(start: int, length: int, digits: int, modulus: int) -> int:
    base = pow(10, digits, modulus)
    residue = 0
    for j in range(length):
        residue = (base * residue + start + j) % modulus
    return residue


def verify_transition_engine() -> None:
    """Cross-check matrix jumps against a separate literal recurrence."""
    tests = 0
    for modulus in range(2, 80):
        for digits in range(1, 4):
            lower = 1 if digits == 1 else 10 ** (digits - 1)
            for offset in (0, 1, 3):
                k = lower + offset
                if k >= 10**digits:
                    continue
                x = (17 * modulus + k) % modulus
                for steps in (0, 1, 2, 7):
                    if k + steps >= 10**digits:
                        continue
                    literal = x
                    base = pow(10, digits, modulus)
                    for j in range(1, steps + 1):
                        literal = (base * literal + k + j) % modulus
                    jumped, endpoint = advance(x, k, steps, digits, modulus)
                    assert endpoint == k + steps
                    assert jumped == literal
                    tests += 1
    print(f"PASS matrix engine vs literal recurrence ({tests} cases)")


def a075001_witness(n: int) -> tuple[int, int]:
    if n == 1:
        return 1, 1
    fs = factor(n)
    smooth = 2 ** fs.get(2, 0) * 5 ** fs.get(5, 0)
    coprime = n // smooth
    period = 1 if coprime == 1 else order_mod(10, coprime)
    minimum_digits = max(1, fs.get(2, 0), fs.get(5, 0))
    digits = period
    while digits < minimum_digits:
        digits += period
    while True:
        low = 10 ** (digits - 1)
        high = 10**digits - n
        if high >= low and high - low + 1 >= smooth:
            start = low if smooth == 1 else low + ((1 - n - low) % smooth)
            if start <= high:
                return start, digits
        digits += period


def choose_shift(
    x: int,
    k: int,
    step: int,
    choices: int,
    target: int,
    digits: int,
    modulus: int,
    upper: int,
) -> tuple[int, int] | None:
    for choice in range(choices):
        if x % target == 0:
            return x, k
        if choice + 1 == choices or k + step > upper:
            return None
        x, k = advance(x, k, step, digits, modulus)
    raise AssertionError("unreachable")


def construct_a075002(n: int) -> tuple[int, int]:
    """Construct one common prefix index using the proof's ordered-prime lifts."""
    if n == 1:
        return 1, 1
    fs = factor(n)
    smooth = 2 ** fs.get(2, 0) * 5 ** fs.get(5, 0)
    exponent3 = fs.get(3, 0)
    odd_primes = sorted(p for p in fs if p not in (2, 3, 5))

    digit_period = 1
    for p in odd_primes:
        digit_period = lcm(digit_period, order_mod(10, p ** fs[p]))

    minimum_digits = max(1, fs.get(2, 0), fs.get(5, 0))
    digits = 1
    while digits < minimum_digits:
        digits += digit_period
    if (digits - 1) % digit_period:
        digits += digit_period - ((digits - 1) % digit_period)

    for _attempt in range(30):
        lower = 10 ** (digits - 1)
        upper = 10**digits - 1
        start_modulus = smooth * (3 if exponent3 else 1)
        k = lower + ((-lower) % start_modulus)
        if k > upper:
            digits += digit_period
            continue
        x = prefix_mod(k, n, digits)
        assert k % smooth == 0 and x % smooth == 0
        state_period = 1
        failed = False

        if exponent3:
            assert k % 3 == 0 and x % 3 == 0
            for a in range(1, exponent3):
                step = lcm(2 * 3**a, smooth)
                chosen = choose_shift(
                    x, k, step, 3, 3 ** (a + 1), digits, n, upper
                )
                if chosen is None:
                    failed = True
                    break
                x, k = chosen
            if not failed:
                state_period = lcm(state_period, 2 * 3**exponent3)

        if failed:
            digits += digit_period
            continue

        completed = smooth * (3**exponent3)
        for p in odd_primes:
            exponent = fs[p]
            h = order_mod(10, p)
            step = lcm(h, state_period, smooth)
            chosen = choose_shift(x, k, step, p, p, digits, n, upper)
            if chosen is None:
                failed = True
                break
            x, k = chosen
            completed *= p
            assert x % completed == 0

            for a in range(1, exponent):
                step = lcm(h * p**a, state_period, smooth)
                chosen = choose_shift(
                    x, k, step, p, p ** (a + 1), digits, n, upper
                )
                if chosen is None:
                    failed = True
                    break
                x, k = chosen
                completed *= p
                assert x % completed == 0
            if failed:
                break
            state_period = lcm(
                state_period, p**exponent * order_mod(10, p**exponent)
            )

        if not failed:
            assert x % n == 0
            assert prefix_mod(k, n, digits) == 0
            return k, digits
        digits += digit_period
    raise AssertionError(f"digit-window search failed for n={n}")


def verify_oeis_initial_terms() -> None:
    computed = [
        direct_first_witness(n, OEIS_A075002_1_TO_60[n - 1])
        for n in range(1, 61)
    ]
    assert computed == OEIS_A075002_1_TO_60
    print("PASS OEIS A075002 terms n=1..60")


def verify_a075001() -> None:
    for n in range(1, 2001):
        start, digits = a075001_witness(n)
        assert 10 ** (digits - 1) <= start
        assert start + n - 1 < 10**digits
        assert block_residue(start, n, digits, n) == 0
    print("PASS A075001 construction n=1..2000")


def verify_special_three_shift() -> None:
    tests = 0
    for digits in range(2, 7):
        lower = 10 ** (digits - 1)
        upper = 10**digits - 1
        for a in range(1, 6):
            modulus = 3 ** (a + 1)
            for coefficient in (2, 4, 8, 10):
                if coefficient % 3 == 0:
                    continue
                step = coefficient * 3**a
                k = lower + 7
                if k + step > upper:
                    continue
                x = prefix_mod(k, modulus, digits)
                y, _ = advance(x, k, step, digits, modulus)
                expected = x + step * k + step * (step + 1) // 2
                assert (y - expected) % modulus == 0
                tests += 1
    assert prefix_mod(2, 3) == 0
    assert prefix_mod(8, 9) == 0
    print(f"PASS 3-adic block-shift congruence ({tests} cases), plus 3 and 9")


def verify_unit_translation_lift() -> None:
    tests = 0
    for p in (7, 11, 13, 17, 19, 37, 53):
        h = order_mod(10, p)
        digits = h + 1
        k = 10 ** (digits - 1) + 3
        base = pow(10, digits, p)
        assert base == 10 % p and gcd(base - 1, p) == 1
        unit = (-h * pow(base - 1, -1, p)) % p
        assert unit
        for a in range(3):
            for coefficient in (1, 2, 4):
                if coefficient % p == 0:
                    continue
                modulus = p ** (a + 1)
                step = coefficient * h * p**a
                x = prefix_mod(k, modulus, digits)
                y, _ = advance(x, k, step, digits, modulus)
                assert (y - x - coefficient * p**a * unit) % modulus == 0
                tests += 1
    print(f"PASS unit-translation prime lift ({tests} cases)")


def verify_paper_prime_power_construction() -> None:
    tests = 0
    for p in (2, 5):
        for a in range(1, 9):
            modulus = p**a
            digits = max(a, 1)
            while True:
                lower = 10 ** (digits - 1)
                upper = 10**digits - 1
                k = lower + ((-lower) % modulus)
                if k <= upper:
                    break
                digits += 1
            assert prefix_mod(k, modulus, digits) == 0
            tests += 1

    for p in (7, 11, 13, 17, 19, 23, 37, 53):
        for a in (1, 2):
            modulus = p**a
            full_order = order_mod(10, modulus)
            p_part = 1
            reduced = full_order
            while reduced % p == 0:
                p_part *= p
                reduced //= p
            t = 0
            while True:
                digits = p_part * (1 + t * full_order)
                lower = 10 ** (digits - 1)
                upper = 10**digits - 1
                base = pow(10, digits, modulus)
                h = order_mod(base, modulus)
                if lower - 1 + (modulus - 1) * h <= upper:
                    break
                t += 1
            assert h == reduced and h > 1
            assert gcd(base - 1, modulus) == 1
            translation = (-h * pow(base - 1, -1, modulus)) % modulus
            assert gcd(translation, modulus) == 1
            x0 = prefix_mod(lower - 1, modulus, digits - 1)
            orbit_index = (-x0 * pow(translation, -1, modulus)) % modulus
            k = lower - 1 + orbit_index * h
            assert k <= upper
            assert prefix_mod(k, modulus, digits) == 0
            tests += 1

    assert prefix_mod(2, 3) == 0
    assert prefix_mod(8, 9) == 0
    tests += 2
    print(f"PASS paper prime-power construction ({tests} cases)")


def verify_naive_global_orbit_obstructions() -> None:
    failures = []
    for modulus in range(7, 5000):
        if gcd(modulus, 30) != 1:
            continue
        full_order = order_mod(10, modulus)
        works = False
        for digits in range(1, full_order + 1):
            base = pow(10, digits, modulus)
            h = order_mod(base, modulus)
            if gcd(base - 1, modulus) == 1 and gcd(h, modulus) == 1:
                works = True
                break
        if not works:
            failures.append(modulus)
    assert failures == [689, 1027, 1673, 3403, 4823]
    print("PASS exhaustive naive-global-orbit obstruction scan Q<5000")


def verify_full_construction() -> None:
    largest_digits = (0, 0)
    for n in range(1, 501):
        witness, digits = construct_a075002(n)
        assert prefix_mod(witness, n, digits) == 0
        if digits > largest_digits[1]:
            largest_digits = (n, digits)
    for n in (689, 1027, 1673, 3403, 4823):
        witness, digits = construct_a075002(n)
        assert prefix_mod(witness, n, digits) == 0
    print(
        "PASS full common-index construction n=1..500 and five global-orbit "
        f"failure moduli; largest digit length in range={largest_digits}"
    )


def main() -> None:
    verify_transition_engine()
    verify_oeis_initial_terms()
    verify_a075001()
    verify_special_three_shift()
    verify_unit_translation_lift()
    verify_paper_prime_power_construction()
    verify_naive_global_orbit_obstructions()
    verify_full_construction()
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()

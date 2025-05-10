#!/usr/bin/env python
import cmath
import math
import sys
import numpy

#%%%%%%%%%%%%%%%%
# Get a value for the limit of the range to be sieved
limit = int(input("limit value here: "))
limit = int(limit)
#%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%
# Epoch calculation
h = limit
epoch = 90 * (h * h) - 12 * h + 1
print("The epoch range is", epoch)
limit = epoch
base10 = (limit * 90) + 11
print("This is the base-10 limit:", base10)
#%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%
# Get RANGE for number of iterations x
a = 90
b = -300
c = 250 - limit
d = (b ** 2) - (4 * a * c)
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print('The solutions are {0} and {1}'.format(sol1, sol2))
new_limit = sol2
#%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%
# Initialize arrays
A224854 = [0] * int(limit + 100)  # (11, 13)
A224855 = [0] * int(limit + 100)  # (17, 19)
A224856 = [0] * int(limit + 100)  # (29, 31)
A224857 = [0] * int(limit + 100)  # (41, 43)
A224859 = [0] * int(limit + 100)  # (47, 49)
A224860 = [0] * int(limit + 100)  # (59, 61)
A224862 = [0] * int(limit + 100)  # (71, 73)
A224864 = [0] * int(limit + 100)  # (77, 79)
A224865_89 = [0] * int(limit + 100)  # For 90n + 89
A224865_91 = [0] * int(limit + 100)  # For 90n + 91
#%%%%%%%%%%%%%%%%

# Composite generating function
def drLD(x, l, m, z, o, listvar):
    y = 90 * (x * x) - l * x + m
    if 0 <= y < len(listvar):
        listvar[y] = listvar[y] + 1
    else:
        print(f"Failed to mark y={y} for x={x}, z={z}, o={o}")
    p = z + (90 * (x - 1))
    q = o + (90 * (x - 1))
    for n in range(1, int(((limit - y) / p) + 1)):
        idx = y + (p * n)
        if 0 <= idx < len(listvar):
            listvar[idx] = listvar[idx] + 1
        else:
            print(f"Failed to mark y+p*n={idx} for p={p}, n={n}")
    for n in range(1, int(((limit - y) / q) + 1)):
        idx = y + (q * n)
        if 0 <= idx < len(listvar):
            listvar[idx] = listvar[idx] + 1
        else:
            print(f"Failed to mark y+q*n={idx} for q={q}, n={n}")

# Prime testing and factorization functions
def is_prime(n):
    if n == 1:  # Accept 1 as prime for this context
        return True
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def factorize(n):
    factors = []
    if n < 2:
        return factors
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1 if i == 2 else 2
    if n > 1:
        factors.append(n)
    return factors

# Apply operators
for x in range(1, int(new_limit.real)):
    # A224854 (11, 13)
    drLD(x, 120, 34, 7, 53, A224854)
    drLD(x, 132, 48, 19, 29, A224854)
    drLD(x, 120, 38, 17, 43, A224854)
    drLD(x, 90, 11, 13, 77, A224854)
    drLD(x, 78, -1, 11, 91, A224854)
    drLD(x, 108, 32, 31, 41, A224854)
    drLD(x, 90, 17, 23, 67, A224854)
    drLD(x, 72, 14, 49, 59, A224854)
    drLD(x, 60, 4, 37, 83, A224854)
    drLD(x, 60, 8, 47, 73, A224854)
    drLD(x, 48, 6, 61, 71, A224854)
    drLD(x, 12, 0, 79, 89, A224854)
    drLD(x, 76, -1, 13, 91, A224854)
    drLD(x, 94, 18, 19, 67, A224854)
    drLD(x, 94, 24, 37, 49, A224854)
    drLD(x, 76, 11, 31, 73, A224854)
    drLD(x, 86, 6, 11, 83, A224854)
    drLD(x, 104, 29, 29, 47, A224854)
    drLD(x, 86, 14, 23, 71, A224854)
    drLD(x, 86, 20, 41, 53, A224854)
    drLD(x, 104, 25, 17, 59, A224854)
    drLD(x, 14, 0, 77, 89, A224854)
    drLD(x, 94, 10, 7, 79, A224854)
    drLD(x, 76, 15, 43, 61, A224854)

    # A224855 (17, 19)
    drLD(x, 72, -1, 17, 91, A224855)
    drLD(x, 108, 29, 19, 53, A224855)
    drLD(x, 72, 11, 37, 71, A224855)
    drLD(x, 18, 0, 73, 89, A224855)
    drLD(x, 102, 20, 11, 67, A224855)
    drLD(x, 138, 52, 13, 29, A224855)
    drLD(x, 102, 28, 31, 47, A224855)
    drLD(x, 48, 3, 49, 83, A224855)
    drLD(x, 78, 8, 23, 79, A224855)
    drLD(x, 132, 45, 7, 41, A224855)
    drLD(x, 78, 16, 43, 59, A224855)
    drLD(x, 42, 4, 61, 77, A224855)
    drLD(x, 70, -1, 19, 91, A224855)
    drLD(x, 106, 31, 37, 37, A224855)
    drLD(x, 34, 3, 73, 73, A224855)
    drLD(x, 110, 27, 11, 59, A224855)
    drLD(x, 110, 33, 29, 41, A224855)
    drLD(x, 56, 6, 47, 77, A224855)
    drLD(x, 74, 5, 23, 83, A224855)
    drLD(x, 124, 40, 13, 43, A224855)
    drLD(x, 70, 7, 31, 79, A224855)
    drLD(x, 70, 13, 49, 61, A224855)
    drLD(x, 106, 21, 7, 67, A224855)
    drLD(x, 20, 0, 71, 89, A224855)
    drLD(x, 74, 15, 53, 53, A224855)
    drLD(x, 146, 59, 17, 17, A224855)

    # A224856 (29, 31)
    drLD(x, 60, -1, 29, 91, A224856)
    drLD(x, 150, 62, 11, 19, A224856)
    drLD(x, 96, 25, 37, 47, A224856)
    drLD(x, 24, 1, 73, 83, A224856)
    drLD(x, 144, 57, 13, 23, A224856)
    drLD(x, 90, 20, 31, 59, A224856)
    drLD(x, 90, 22, 41, 49, A224856)
    drLD(x, 36, 3, 67, 77, A224856)
    drLD(x, 156, 67, 7, 17, A224856)
    drLD(x, 84, 19, 43, 53, A224856)
    drLD(x, 30, 0, 61, 89, A224856)
    drLD(x, 30, 2, 71, 79, A224856)
    drLD(x, 58, -1, 31, 91, A224856)
    drLD(x, 112, 32, 19, 49, A224856)
    drLD(x, 130, 45, 13, 37, A224856)
    drLD(x, 40, 4, 67, 73, A224856)
    drLD(x, 158, 69, 11, 11, A224856)
    drLD(x, 122, 41, 29, 29, A224856)
    drLD(x, 50, 3, 47, 83, A224856)
    drLD(x, 140, 54, 17, 23, A224856)
    drLD(x, 68, 10, 41, 71, A224856)
    drLD(x, 32, 0, 59, 89, A224856)
    drLD(x, 50, 5, 53, 77, A224856)
    drLD(x, 130, 43, 7, 43, A224856)
    drLD(x, 58, 9, 61, 61, A224856)
    drLD(x, 22, 1, 79, 79, A224856)

    # A224857 (41, 43)
    drLD(x, 48, -1, 41, 91, A224857)
    drLD(x, 42, 0, 49, 89, A224857)
    drLD(x, 102, 24, 19, 59, A224857)
    drLD(x, 120, 39, 23, 37, A224857)
    drLD(x, 108, 25, 11, 61, A224857)
    drLD(x, 72, 7, 29, 79, A224857)
    drLD(x, 90, 22, 43, 47, A224857)
    drLD(x, 150, 62, 13, 17, A224857)
    drLD(x, 78, 12, 31, 71, A224857)
    drLD(x, 30, 2, 73, 77, A224857)
    drLD(x, 60, 9, 53, 67, A224857)
    drLD(x, 90, 6, 7, 83, A224857)
    drLD(x, 46, -1, 43, 91, A224857)
    drLD(x, 154, 65, 7, 19, A224857)
    drLD(x, 64, 6, 37, 79, A224857)
    drLD(x, 46, 5, 61, 73, A224857)
    drLD(x, 116, 32, 11, 53, A224857)
    drLD(x, 134, 49, 17, 29, A224857)
    drLD(x, 44, 0, 47, 89, A224857)
    drLD(x, 26, 1, 71, 83, A224857)
    drLD(x, 136, 50, 13, 31, A224857)
    drLD(x, 64, 10, 49, 67, A224857)
    drLD(x, 116, 36, 23, 41, A224857)
    drLD(x, 44, 4, 59, 77, A224857)

    # A224859 (47, 49)
    drLD(x, 42, -1, 47, 91, A224859)
    drLD(x, 78, 5, 19, 83, A224859)
    drLD(x, 132, 46, 11, 37, A224859)
    drLD(x, 78, 11, 29, 73, A224859)
    drLD(x, 108, 26, 13, 59, A224859)
    drLD(x, 72, 8, 31, 77, A224859)
    drLD(x, 108, 30, 23, 49, A224859)
    drLD(x, 102, 17, 7, 71, A224859)
    drLD(x, 48, 0, 43, 89, A224859)
    drLD(x, 102, 23, 17, 61, A224859)
    drLD(x, 48, 4, 53, 79, A224859)
    drLD(x, 72, 12, 41, 67, A224859)
    drLD(x, 40, -1, 49, 91, A224859)
    drLD(x, 130, 46, 19, 31, A224859)
    drLD(x, 76, 13, 37, 67, A224859)
    drLD(x, 94, 14, 13, 73, A224859)
    drLD(x, 140, 53, 11, 29, A224859)
    drLD(x, 86, 20, 47, 47, A224859)
    drLD(x, 14, 0, 83, 83, A224859)
    drLD(x, 104, 27, 23, 53, A224859)
    drLD(x, 50, 0, 41, 89, A224859)
    drLD(x, 50, 6, 59, 71, A224859)
    drLD(x, 86, 10, 17, 77, A224859)
    drLD(x, 166, 76, 7, 7, A224859)
    drLD(x, 94, 24, 43, 43, A224859)
    drLD(x, 40, 3, 61, 79, A224859)

    # A224860 (59, 61)
    drLD(x, 30, -1, 59, 91, A224860)
    drLD(x, 120, 38, 19, 41, A224860)
    drLD(x, 66, 7, 37, 77, A224860)
    drLD(x, 84, 12, 23, 73, A224860)
    drLD(x, 90, 9, 11, 79, A224860)
    drLD(x, 90, 19, 29, 61, A224860)
    drLD(x, 126, 39, 7, 47, A224860)
    drLD(x, 54, 3, 43, 83, A224860)
    drLD(x, 114, 31, 13, 53, A224860)
    drLD(x, 60, 0, 31, 89, A224860)
    drLD(x, 60, 8, 49, 71, A224860)
    drLD(x, 96, 18, 17, 67, A224860)
    drLD(x, 28, -1, 61, 91, A224860)
    drLD(x, 82, 8, 19, 79, A224860)
    drLD(x, 100, 27, 37, 43, A224860)
    drLD(x, 100, 15, 7, 73, A224860)
    drLD(x, 98, 16, 11, 71, A224860)
    drLD(x, 62, 0, 29, 89, A224860)
    drLD(x, 80, 17, 47, 53, A224860)
    drLD(x, 80, 5, 17, 83, A224860)
    drLD(x, 100, 19, 13, 67, A224860)
    drLD(x, 118, 38, 31, 31, A224860)
    drLD(x, 82, 18, 49, 49, A224860)
    drLD(x, 80, 9, 23, 77, A224860)
    drLD(x, 98, 26, 41, 41, A224860)
    drLD(x, 62, 10, 59, 59, A224860)

    # A224862 (71, 73)
    drLD(x, 18, -1, 71, 91, A224862)
    drLD(x, 72, 0, 19, 89, A224862)
    drLD(x, 90, 21, 37, 53, A224862)
    drLD(x, 90, 13, 17, 73, A224862)
    drLD(x, 138, 51, 11, 31, A224862)
    drLD(x, 102, 27, 29, 49, A224862)
    drLD(x, 120, 36, 13, 47, A224862)
    drLD(x, 30, 1, 67, 83, A224862)
    drLD(x, 150, 61, 7, 23, A224862)
    drLD(x, 78, 15, 41, 61, A224862)
    drLD(x, 42, 3, 59, 79, A224862)
    drLD(x, 60, 6, 43, 77, A224862)
    drLD(x, 16, -1, 73, 91, A224862)
    drLD(x, 124, 41, 19, 37, A224862)
    drLD(x, 146, 58, 11, 23, A224862)
    drLD(x, 74, 8, 29, 77, A224862)
    drLD(x, 74, 14, 47, 59, A224862)
    drLD(x, 56, 3, 41, 83, A224862)
    drLD(x, 106, 24, 13, 61, A224862)
    drLD(x, 106, 30, 31, 43, A224862)
    drLD(x, 124, 37, 7, 49, A224862)
    drLD(x, 34, 2, 67, 79, A224862)
    drLD(x, 74, 0, 17, 89, A224862)
    drLD(x, 56, 7, 53, 71, A224862)

    # A224864 (77, 79)
    drLD(x, 12, -1, 77, 91, A224864)
    drLD(x, 138, 52, 19, 23, A224864)
    drLD(x, 102, 28, 37, 41, A224864)
    drLD(x, 48, 5, 59, 73, A224864)
    drLD(x, 162, 72, 7, 11, A224864)
    drLD(x, 108, 31, 29, 43, A224864)
    drLD(x, 72, 13, 47, 61, A224864)
    drLD(x, 18, 0, 79, 83, A224864)
    drLD(x, 78, 0, 13, 89, A224864)
    drLD(x, 132, 47, 17, 31, A224864)
    drLD(x, 78, 16, 49, 53, A224864)
    drLD(x, 42, 4, 67, 71, A224864)
    drLD(x, 10, -1, 79, 91, A224864)
    drLD(x, 100, 22, 19, 61, A224864)
    drLD(x, 136, 48, 7, 37, A224864)
    drLD(x, 64, 8, 43, 73, A224864)
    drLD(x, 80, 0, 11, 89, A224864)
    drLD(x, 80, 12, 29, 71, A224864)
    drLD(x, 116, 34, 17, 47, A224864)
    drLD(x, 44, 2, 53, 83, A224864)
    drLD(x, 154, 65, 13, 13, A224864)
    drLD(x, 100, 26, 31, 49, A224864)
    drLD(x, 46, 5, 67, 67, A224864)
    drLD(x, 134, 49, 23, 23, A224864)
    drLD(x, 80, 16, 41, 59, A224864)
    drLD(x, 26, 1, 77, 77, A224864)

    # A224865 (89, 91) - Separate arrays
    # Operators for 90n + 89
    drLD(x, 0, -1, 89, 1, A224865_89)
    drLD(x, 90, 14, 19, 71, A224865_89)
    drLD(x, 126, 42, 17, 37, A224865_89)
    drLD(x, 54, 6, 53, 73, A224865_89)
    drLD(x, 120, 35, 11, 49, A224865_89)
    drLD(x, 120, 39, 29, 31, A224865_89)
    drLD(x, 66, 10, 47, 67, A224865_89)
    drLD(x, 84, 5, 13, 83, A224865_89)
    drLD(x, 114, 34, 23, 43, A224865_89)
    drLD(x, 60, 5, 41, 79, A224865_89)
    drLD(x, 60, 9, 59, 61, A224865_89)
    drLD(x, 96, 11, 7, 77, A224865_89)
    # Operators for 90n + 91
    drLD(x, -2, 0, 1, 1, A224865_91)
    drLD(x, 142, 56, 19, 19, A224865_91)
    drLD(x, 70, 10, 37, 73, A224865_91)
    drLD(x, 128, 43, 11, 41, A224865_91)
    drLD(x, 92, 21, 29, 59, A224865_91)
    drLD(x, 110, 32, 23, 47, A224865_91)
    drLD(x, 20, 1, 77, 83, A224865_91)
    drLD(x, 160, 71, 7, 13, A224865_91)
    drLD(x, 88, 19, 31, 61, A224865_91)
    drLD(x, 52, 5, 49, 79, A224865_91)
    drLD(x, 70, 12, 43, 67, A224865_91)
    drLD(x, 110, 30, 17, 53, A224865_91)
    drLD(x, 38, 4, 71, 71, A224865_91)
    drLD(x, 2, 0, 89, 89, A224865_91)

# Trim padding and remove first element for A224865_91
A224854 = A224854[:-100]
A224855 = A224855[:-100]
A224856 = A224856[:-100]
A224857 = A224857[:-100]
A224859 = A224859[:-100]
A224860 = A224860[:-100]
A224862 = A224862[:-100]
A224864 = A224864[:-100]
A224865_89 = A224865_89[:-100]
A224865_91 = A224865_91[:-100]
A224865_91.pop(0)  # Remove first term for alignment

# Generate and verify twin primes
sequences = [
    {"name": "A224854", "k1": 11, "k2": 13, "array": A224854},
    {"name": "A224855", "k1": 17, "k2": 19, "array": A224855},
    {"name": "A224856", "k1": 29, "k2": 31, "array": A224856},
    {"name": "A224857", "k1": 41, "k2": 43, "array": A224857},
    {"name": "A224859", "k1": 47, "k2": 49, "array": A224859},
    {"name": "A224860", "k1": 59, "k2": 61, "array": A224860},
    {"name": "A224862", "k1": 71, "k2": 73, "array": A224862},
    {"name": "A224864", "k1": 77, "k2": 79, "array": A224864},
    {"name": "A224865", "k1": 89, "k2": 91, "array1": A224865_89, "array2": A224865_91},
]

# Expected sequence for A224865
expected_n_A224865 = [0, 1, 2, 8, 17, 25, 30, 32, 36, 44, 46, 64, 69, 72, 73, 83, 88, 97, 99, 106, 107, 116, 118, 120, 122, 123, 129, 132, 135, 151, 184, 186, 190, 198, 205, 211, 220, 233, 239, 253, 255, 262, 282, 296, 305, 314, 317, 331, 342, 347, 352, 365, 374, 382, 384, 391, 396, 409]

total_twin_primes = 0
for seq in sequences:
    name = seq["name"]
    k1 = seq["k1"]
    k2 = seq["k2"]

    if name == "A224865":
        # Separate arrays for A224865
        array1 = seq["array1"]
        array2 = seq["array2"]
        address_1 = [i for i, x in enumerate(array1) if x == 0]
        address_2 = [i for i, x in enumerate(array2) if x == 0]
        print(f"\nPotential primes for 90n + {k1} ({name}): {len(address_1)}")
        print(f"Potential primes for 90n + {k2} ({name}): {len(address_2)}")
        address = [n for n in address_1 if n in address_2]
    else:
        # Single array for other sequences
        array = seq["array"]
        address = [i for i, x in enumerate(array) if x == 0]
        print(f"\nNumber of potential twin prime pairs for {name} ({k1}, {k2}): {len(address)}")

    address1 = [90 * n + k1 for n in address]
    address2 = [90 * n + k2 for n in address]
    total_twin_primes += len(address)

    # Verify twin primes
    print(f"\nVerifying twin prime pairs for {name} ({k1}, {k2}):")
    valid_pairs = []
    false_positives = []
    for i, (p1, p2) in enumerate(zip(address1, address2)):
        n = address[i]
        is_p1_prime = is_prime(p1)
        is_p2_prime = is_prime(p2)
        if is_p1_prime and is_p2_prime:
            valid_pairs.append((n, p1, p2))
            print(f"n={n}: {p1}, {p2} - Both prime (Valid twin prime pair)")
        else:
            p1_factors = factorize(p1) if not is_p1_prime else None
            p2_factors = factorize(p2) if not is_p2_prime else None
            error_msg = f"n={n}: {p1} (prime={is_p1_prime}"
            if p1_factors:
                error_msg += f", factors={p1_factors}"
            error_msg += f"), {p2} (prime={is_p2_prime}"
            if p2_factors:
                error_msg += f", factors={p2_factors}"
            error_msg += ") - Invalid pair"
            print(error_msg)
            false_positives.append((n, p1, p2, p1_factors, p2_factors))

    print(f"\nSummary for {name}: {len(valid_pairs)}/{len(address)} pairs are valid twin primes")
    if len(valid_pairs) == len(address):
        print(f"All pairs in {name} are correctly identified as twin primes.")
    else:
        print(f"Some pairs in {name} are not twin primes. Check sieve operators or implementation.")
        print("\nFalse positives:")
        for n, p1, p2, p1_factors, p2_factors in false_positives:
            print(f"n={n}: {p1} (factors={p1_factors}), {p2} (factors={p2_factors})")

    print(f"\nList of verified twin prime pairs for {name} (90n + {k1}, 90n + {k2}):")
    for n, p1, p2 in valid_pairs:
        print(f"n={n}: ({p1}, {p2})")

    # Verify against expected sequence for A224865
    if name == "A224865":
        print("\nChecking against expected sequence for A224865 (first 57 terms):")
        expected_found = [n for n in expected_n_A224865 if n in address]
        missing_n = [n for n in expected_n_A224865 if n not in address]
        print(f"Found {len(expected_found)}/{len(expected_n_A224865)} expected n: {expected_found}")
        if missing_n:
            print(f"Missing n: {missing_n}")
        else:
            print("All expected n found.")
        unexpected_n = [n for n in address if n not in expected_n_A224865]
        if unexpected_n:
            print(f"Unexpected n: {unexpected_n}")
        else:
            print("No unexpected n found.")

print(f"\nTotal twin primes across all sequences: {total_twin_primes}")
#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    # Initialize an array to track prime status of each number
    is_prime = [True] * (n + 1)
    p = 2
    # Implement the sieve algorithm
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    # Count the number of primes up to n
    prime_count = sum(1 for p in range(2, n + 1) if is_prime[p])
    return prime_count


def isWinner(x, nums):
    if (x == 0):
        return None
    if (len(nums) == 0):
        return "Ben"
    # Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for i in range(x):
        n = nums[i]
        prime_count = sieve_of_eratosthenes(n)

        # Determine winner based on the count of primes
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # If it's a tie

# Example usage:
# print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))  # Output: "Maria"

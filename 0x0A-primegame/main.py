#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(1, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(1, [10, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [1, 2, 3])))
print("Winner: {}".format(isWinner(0, [])))


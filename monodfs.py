import random
import argparse


# utility function to check the monopole constraint
def check_sum(nums, m):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == m:
                return True
    return False


class Puzzle(object):
    def __init__(self, m, n, verbose=False):
        self.m = m
        self.n = n
        self.verbose = verbose

        # Monopoles numbered 1..m
        self.monopoles = [i + 1 for i in range(m)]

        # Rooms is a dictionary ranging keys from 0..n-1. Each room is a list of monopoles
        self.rooms = dict()
        for r in range(n):
            self.rooms[r] = list()

        if verbose:
            print(f"Monopoles: {self.monopoles}")
            print(f"Rooms:\n{self.rooms}")

    # calculates all possible places/moves for a given monopole m
    # returns the moves in tuples (m, r) where monopole m can be placed in room r
    def moves(self, m):
        ms = list()
        for r in self.rooms:
            ms.append((m, r))
        return ms

    # Makes the move run by DFS and updates the room dictionary
    def move(self, mv):
        monopole = mv[0]
        room = mv[1]
        self.rooms[room].append(monopole)

    # Simple logic to check whether the final state of rooms
    # has all monopoles placed
    def solved(self):
        placed_monopoles = list()
        for _, values in self.rooms.items():
            placed_monopoles.append(values)
        flattened = list()

        for l in placed_monopoles:
            for m in l:
                flattened.append(m)
        flattened.sort()

        return flattened == self.monopoles

    # Runs the DFS algorithm iteratively in attempt of finding a solution
    def solve_dfs(self):

        # Run DFS
        for m in self.monopoles:
            next_monopole = m
            if self.verbose:
                print("=========================")
                print(f"Next monopole : {m}")
            monopole_placed = False
            for r in self.rooms:
                if not check_sum(self.rooms[r], m) and not monopole_placed:
                    monopole_placed = True
                    self.rooms[r].append(next_monopole)
                    if self.verbose:
                        for key, value in p.rooms.items():
                            print(f"Room {key} : {value}")


parser = argparse.ArgumentParser(description="Monopoles using DFS")
parser.add_argument('integers', metavar='N', type=int, nargs=2,
                    help='Give number of monopoles and number of rooms')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Show how algorithm works')

args = parser.parse_args()

p = Puzzle(m=args.integers[0], n=args.integers[1], verbose=args.verbose)

p.solve_dfs()

if p.solved():
    print("============================")
    print("\nSolution:\n")
    for key, value in p.rooms.items():
        print(f"Room {key} : {value}")
else:
    print("unsat")

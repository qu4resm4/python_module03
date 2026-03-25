#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    index: int = 1
    while index < len(sys.argv):
        try:
            scores.append(int(sys.argv[index]))
        except Exception:
            print(f"Invalid parameter: '{sys.argv[index]}'")
        index += 1
    if (len(scores) == 0):
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              " <score1> <score2> ...")
    else:
        print("Scores processed:", scores)
        print("Total players:", len(scores))
        print("Total score:", sum(scores))
        print("Average score:", sum(scores) / len(scores))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))
        print()

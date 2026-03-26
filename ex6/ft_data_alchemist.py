#!/usr/bin/env python3
import random


if __name__ == "__main__":
    initial_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                    'Gregory', 'john', 'kevin', 'Liam']
    print("=== Game Data Alchemist ===")
    print()
    print("Initial list of players:", initial_list)
    list_captalize = [x.capitalize() for x in initial_list]
    print("New list with all names capitalized:", list_captalize)
    list_only_captalize = [x for x in initial_list if x.capitalize() == x]
    print("New list of capitalized names only:", list_only_captalize)
    print()
    score_dict = {key: random.randint(50, 1000) for key in list_captalize}
    print("Score dict:", score_dict)
    average = round(sum(score_dict.values()) / 9, 2)
    print("Score average is", average)
    high_score = {k: v for k, v in score_dict.items() if v > average}
    print("High scores:", high_score)

#!/usr/bin/env python3
import random


def gen_player_achievements(achievements: list[str]) -> set:
    player_achievements: set[str] = set()
    for _ in range(random.randint(4, 10)):
        player_achievements.add(achievements[random.randint(0, 12)])
    return player_achievements


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    achievements = [
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Unstoppable',
        'First Steps',
        'Collector Supreme',
        'Untouchable',
        'Sharp Mind',
        'Boss Slayer',
        'Hidden Path Finder'
    ]
    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)
    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)
    print()
    all_distinct = set.union(alice, bob, charlie, dylan)
    print("All distinct achievements:", all_distinct)
    print()
    print("Common achievements:", set.intersection(alice, bob, charlie, dylan))
    print()
    print("Only Alice has:", set.difference(alice, all_distinct))
    print("Only Bob has:", set.difference(bob, all_distinct))
    print("Only Charlie has:", set.difference(charlie, all_distinct))
    print("Only Dylan has:", set.difference(dylan, all_distinct))
    print()
    print("Alice is missing:", set.difference(all_distinct, alice))
    print("Bob is missing:", set.difference(all_distinct, bob))
    print("Charlie is missing:", set.difference(all_distinct, charlie))
    print("Dylan is missing:", set.difference(all_distinct, dylan))

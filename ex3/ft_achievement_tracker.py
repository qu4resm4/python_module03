#!/usr/bin/env python3
import random


def gen_player_achievements(achievements: set) -> set:
    achievements = set(achievements)
    for i in random.randint(4, 10):
        


if __name__ == "__main__":
    achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer']
    gen_player_achievements(achievements)
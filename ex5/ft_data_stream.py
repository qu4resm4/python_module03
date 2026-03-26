#!/usr/bin/env python3
import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    list_actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release"
    ]
    list_players: list[str] = ["alice", "bob", "dylan", "charlie"]
    while True:
        random_index = random.randint(0, 3)
        random_player = list_players[random_index]
        random_index = random.randint(0, 7)
        random_action = list_actions[random_index]
        event: tuple[str, str] = (random_player, random_action)
        yield event


def consume_event(events: list[tuple[str, str]]) -> typing.Generator[
                      tuple[str, str], None, None]:
    removed_indexs: list[int] = [0] * 10
    for i in range(0, 10):
        random_gen = False
        while not random_gen:
            for r in removed_indexs:
                remove_index = random.randint(1, len(events)) - 1
                if r != remove_index:
                    random_gen = True
        removed_indexs[i] = remove_index
        temp = events[remove_index]
        del events[remove_index]
        yield temp


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    list_events: list[tuple[str, str]] = [("", "")] * 1001
    gen = gen_event()
    index = 0
    while index < 1000:
        list_events[index] = next(gen)
        print(f"Event {index}: Player {list_events[index][0]} "
              f"did action {list_events[index][1]}")
        index += 1
    list_events = [("", "")] * 10
    index = 0
    while index < 10:
        list_events[index] = next(gen)
        index += 1
    print("Built list of 10 events:", list_events)
    gen = consume_event(list_events)
    while len(list_events) != 0:
        removed_event = next(gen)
        print("Got event from list:", removed_event)
        print("Remains in list:", list_events)

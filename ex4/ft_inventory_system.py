#!/usr/bin/env python3
import sys


def split_arg(s: str) -> list[str]:
    result = []
    param = ""
    for char in s:
        if char == ":":
            result.append(param)
            param = ""
        else:
            param += char
    result.append(param)
    return result


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    index: int = 1
    while index < len(sys.argv):
        if sys.argv[index].find(":") == -1:
            print(f"Error - invalid parameter '{sys.argv[index]}'")
            index += 1
            continue
        try:
            params = split_arg(sys.argv[index])
            qtty = int(params[1])
            redundant: bool = False
            for key in inventory.keys():
                if key == params[0]:
                    print(f"Redundant item '{params[0]}' - discarding")
                    redundant = True
            if not redundant:
                inventory.update({params[0]: qtty})
        except Exception as e:
            print("Quantity error for 'key':", e)
        index += 1
    if (len(inventory) > 0):
        print("Got inventory:", inventory)
        print("Item list:", inventory.keys())
        total: int = sum(inventory.values())
        print(f"Total quantity of the {len(inventory.keys())} items: {total}")
        for key in inventory:
            print(f"Item {key} represents "
                  f" {round(inventory[key] / total * 100, 1)}%")
        most: str
        least: str
        most_value: int = 0
        least_value: int = total
        for key in inventory:
            if inventory[key] > most_value:
                most_value = inventory[key]
                most = key
        for key in inventory:
            if inventory[key] < least_value:
                least_value = inventory[key]
                least = key
        print(f"Item most abundant: {most} with quantity {most_value}")
        print(f"Item least abundant: {least} with quantity {least_value}")
        inventory.update({"magic_item": 1})
        print("Updated inventory:", inventory)

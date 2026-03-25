#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float]:
    tuple_coords: tuple = tuple()
    while len(tuple_coords) == 0:
        str_coord: str = input("Enter new coordinates as floats "
                               "in format 'x,y,z': ")
        coords = []
        if str_coord.find(",") == -1:
            print("Invalid syntax")
            continue
        else:
            try:
                for coord in str_coord.split(","):
                    coords.append(float(coord))
            except Exception as e:
                print(f"Error on parameter '{coord}':", e.args[0])
                continue
        if len(coords) > 3:
            print("Invalid syntax")
            continue
        tuple_coords = tuple(coords)
    return tuple_coords


def distance_formula(fisrt: tuple[float], second: tuple[float]) -> float:
    x1 = fisrt[0]
    y1 = fisrt[1]
    z1 = fisrt[2]
    x2 = second[0]
    y2 = second[1]
    z2 = second[2]
    result = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2), 4)
    return (result)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first_tuple = get_player_pos()
    print("Got a first tuple:", first_tuple)
    print(f"It includes: X={first_tuple[0]}, "
          f"Y={first_tuple[1]}, Z={first_tuple[2]}")
    distance = distance_formula(first_tuple, (0, 0, 0))
    print("Distance to center:", distance)
    print()
    print("Get a second set of coordinates")
    second_tuple = get_player_pos()
    distance = distance_formula(first_tuple, second_tuple)
    print("Distance between the 2 sets of coordinates:", distance)

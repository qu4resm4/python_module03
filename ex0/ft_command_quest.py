import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    if (len(sys.argv) == 1):
        print("No arguments provided!")
    else:
        index: int = 1
        while index < len(sys.argv):
            print(f"Argument {index}:", sys.argv[index])
            index += 1
    print("Total arguments:", len(sys.argv))

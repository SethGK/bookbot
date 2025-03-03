import sys
from stats import num_count

def character_count(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    char_count = {}
    lower = file_contents.lower()
    for i in lower:
        if i.isalpha():
            char_count[i] = char_count.get(i, 0) + 1
    return char_count

def report(char_count):
    for char, count in sorted(char_count.items()):
        print(f"'{char}: {count}'")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    num_count()
    char_count = character_count(file_path)
    report(char_count)

if __name__ == "__main__":
    main()

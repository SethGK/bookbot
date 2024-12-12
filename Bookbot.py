
def num_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    count = len(words)        
    print(f"There are '{count}' words in the document")

def character_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    char_count = {}
    lower = file_contents.lower()
    for i in lower:
        if i.isalpha():
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1     
    return char_count

def report(char_count):
    for char, count in sorted(char_count.items()):
        print(f"The '{char}' character was found '{count}' times ")
        

def main():
    num_count()
    char_count = character_count()
    report(char_count)

main()
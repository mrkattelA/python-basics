from pathlib import Path

def search(word,text):
    for line in enumerate(text,1):
        if line[1].find(word) >= 0:
            return line
    return None

def main():
    zop = Path("file-processing\Demos\my_files\zen_of_python.txt")

    with open(zop, encoding="utf-8") as f:
        zop_lines = f.readlines()

    word = input("Enter Search word: ")
    result = search(word,zop_lines)
    if result:
        print(f"{word} first appear in line {result[0]} : {result[1]}")
    else:
        print(f"{word} was not found. ")

main()
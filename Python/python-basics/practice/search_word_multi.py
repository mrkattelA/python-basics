from pathlib import Path

def search(word,text):
    results = []
    for line in enumerate(text, 1):
        if line[1].find(word) >= 0:
            results.append(line)
    return results

def main():
    zop = Path(r"file-processing\Demos\my_files\zen_of_python.txt")
    with open(zop, encoding="utf-8") as f:
    #with open(r"file-processing\Demos\my_files\zen_of_python.txt") as f:
        zop_lines = f.readlines()

    word = input("Enter Search word: ")
    results = search(word,zop_lines)
    if not results:
        print(f"{word} was not found. ")

    for result in results:
        #print(f"{word} appear in line {results[0]}:{results[1]}", end="")
        print(word, " appears on line ", result[0],
               ":", result[1], sep="", end="")

main()
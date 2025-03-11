from pathlib import Path

zop = Path("file-processing\Demos\my_files\zen_of_python.txt")

with open(zop, encoding="utf-8") as f:
    poem = f.read()

for i,line in enumerate(poem.splitlines(),1):
    print(f"{i}.{line}")
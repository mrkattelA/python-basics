from pathlib import Path

write_practice = Path(r"python-basics\practice\write_practice.txt")
with open(write_practice, "a+", encoding="utf-8") as f:
    f.write("This is testing again again,333 ")
    f.seek(0)
    print(f.read())
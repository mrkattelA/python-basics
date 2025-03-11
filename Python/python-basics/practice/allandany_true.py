def all_true(iterable):
    for item in iterable:
        if not item:
            return False
    return True

def any_true(iterable):
    for item in iterable:
        if item:
            return True
    return False

def main():
    a = all_true([1,0,1,1,1])
    b = all_true([1,1,1,1,1])
    c = any_true([0,0,0,1,1])
    d = any_true([0,0,0,0,0])

    print(a, b, c, d)

main()
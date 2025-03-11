try:
    1/0
except Exception as f:
    print(type(f))
    print(f)
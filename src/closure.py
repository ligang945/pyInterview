def generate_counter():
    count = 0

    def add_one():
        nonlocal count
        count += 1
        return count
    return add_one
counter = generate_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3

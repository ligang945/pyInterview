def generate_counter():
    CNT = [0]

    def add_one():
        CNT[0] = CNT[0] + 1
        return CNT[0]
    return add_one
counter = generate_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3

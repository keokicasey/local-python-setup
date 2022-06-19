def hello():
    print("Hello, user")

hello()


def pack(a, b, c):
    return[a, b, c]

print(pack(1, 2, 3))


def eat_lunch(items):
    if len(items) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(items)):
            if i == 0:  
                print(f"First I eat {items[0]}")
            else:   
                print(f"Next I eat {items[i]}")

eat_lunch([])
eat_lunch(["sandwhich", "chips", "juice"])
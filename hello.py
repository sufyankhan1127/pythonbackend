
def add(*numbers):
    total=0

    for number in numbers:
        total += number
    return total

print(add(10,20,30))
print(add(10,20,30,40,50))


def userinfo(**details):
    print(details)

userinfo(name="John", age=30, city="New York")
userinfo(name="Alice", age=25, street="123 Main St", country="USA", profession="Engineer")

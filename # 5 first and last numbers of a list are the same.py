import random
print("This program will tell you in a random list if the first and last number of the list are same or not")

num_x = []
num_y = []
for num in range(5):
    num_x.append(random.randint(0, 100))
    num_y.append(random.randint(0, 100))

print(f"The given list is x: {num_x}")
if num_x[0] == num_x[4]:
    print("result is True")
else:
    print("result is False")

print(f"The given list is y: {num_y}")
if num_y[0] == num_y[4]:
    print("result is True")
else:
    print("result is False")
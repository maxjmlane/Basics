for val in range(1, 21):
    if (val % 5 == 0 and val % 3 == 0):
        print("FizzBuzz")
    else if (val % 3 == 0):
        print("Fuzz")
    else if (val % 5 == 0):
        print("Buzz")
    else:
        print(val)
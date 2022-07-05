favorite_numbers = {
    'khair': [42, 17],
    'rahat': [42, 39, 56],
    'mahir': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")
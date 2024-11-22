for country, capital in questions:
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("Correct!")
    else:
        print(f"Oops! The correct answer is {capital}.")

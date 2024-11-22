# Primitive Quiz Advance 

# List of 10 European countries and their capitals

Capital_Questions = [
("What is the capital of Denmark?", "Copenhagen"),
("What is the capital of Finland?", "Hesinki"),
("What is the capital of Greece?", "Athens"),
("What is the capital of Germany?", "Berlin"),
("What is the capital of Ireland?", "Dublin"),
("What is the capital of Italy?", "Rome"),
("What is the capital of Norway?", "Oslo"),
("What is the capital of Poland?", "Warsaw"),
("What is the capital of Russia?", "Moscov"),
("What is the capital of Spain?", "Madrid")]

for Country, Captital_City in Capital_Questions:
    Correct_Answer= input(f"What is the capital of {Country}? ").strip().lower()
    if Correct_Answer == Captital_City.lower():
        print("Correct!")
    else:
        print(f"Oops! The correct answer is {Captital_City}.")

# Positional vs Keyword Arguments


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"You are from {location}")


greet_with("Gautam", "New Zealand")  # Positional

greet_with(location="New Zealand 2", name="Gautam")  # Keyword

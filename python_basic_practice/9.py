# Write a lambda function that sorts a list of tuples (name, age ) by age in descending order.

sample = [
    ("Alice", 22),
    ("Edward", 24),
    ("Iris", 25),
    ("Bob", 29),
    ("Mathew", 23)
]

print(sorted(sample, key=lambda x: x[1]))
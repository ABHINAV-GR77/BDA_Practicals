
numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
words = ["apple", "banana", "cherry", "date", "elderberry"]


squared_evens = [num**2 for num in numbers if num % 2 == 0]
print(f"List Comprehension (squared evens): {squared_evens}")

cubed_dict = {num: num**3 for num in numbers}
print(f"Dictionary Comprehension (cubed numbers): {cubed_dict}")

long_word_lengths = {word: len(word) for word in words if len(word) > 5}
print(f"Dictionary Comprehension (long word lengths): {long_word_lengths}")

first_letters = {word[0].upper() for word in words}
print(f"Set Comprehension (unique first letters): {first_letters}")

even_numbers_set = {num for num in numbers if num % 2 == 0}
print(f"Set Comprehension (even numbers): {even_numbers_set}")

squared_odds_generator = (num**2 for num in numbers if num % 2 != 0)
print(f"Generator Comprehension (squared odds): {squared_odds_generator}")
print("Iterating through generator comprehension:")
for i in squared_odds_generator:
    print(i)



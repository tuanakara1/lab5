import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi"]

def passGen(num_words):
    if num_words < 3 or num_words > 7:
        print("Invalid input")
    else:
        password = ""
        for i in range(num_words):
            password += random.choice(words)
        return password[::-1]

def rep_with_upper(s):
    char_to_replace = random.choice(s)
    new_s = s.replace(char_to_replace, char_to_replace.upper())
    return new_s

def swap_letters(s):
    if len(s) < 2:
        return s
    else:
        return s[-2:] + s[2:-2] + s[:2]

def search_letter(source_str, key_letter):
    if key_letter in source_str:
        return True
    else:
        return False

user_number = int(input("Please enter a value (from 3 to 7) for the number of words: "))
password_initial = passGen(user_number)
password_rep_upper = rep_with_upper(password_initial)
password_final = swap_letters(password_rep_upper)

print("Initial password:", password_initial)
print("Final version of the password:", password_final)

name_first_letter = input("Please enter your name's first letter: ")
if search_letter(password_final, name_first_letter):
    print(f"The letter '{name_first_letter}' is in the final password.")
else:
    print(f"The letter '{name_first_letter}' is not in the final password.")

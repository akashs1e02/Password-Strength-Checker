password = input("Enter a password: ")

length = len(password)

has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

score = 0

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1

if score <= 2:
    strength = "Weak"
elif score == 3:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Analysis")
print("-----------------")
print("Length:", length)
print("Contains Uppercase:", has_upper)
print("Contains Number:", has_digit)
print("Contains Symbol:", has_symbol)
print("Password Strength:", strength)
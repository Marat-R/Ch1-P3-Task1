users_text = input("Input your text: ")

counter_up = 0            # Счетчик букв в верхнем регистре
counter_low = 0           # Счетчик букв в нижнем регистре

for letter in users_text:
    if letter.isupper():
        counter_up += 1
    elif letter.islower():
        counter_low += 1

print(counter_up)
print(counter_low)
print("Up %: ", round(counter_up / ((counter_up + counter_low) / 100)))
print("Low %: ", round(counter_low / ((counter_up + counter_low) / 100)))

# one_percent = (counter_up + counter_low) / 100
# print(round(counter_up / one_percent), 2)
# print(round(counter_low / one_percent), 2)
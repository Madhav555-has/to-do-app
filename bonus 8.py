date = input("Enter today's date:")
mood = input("How would you rate your mood from 1 to 10?")
thought = input("Let Your thought flow:")
with open(f'{date}', 'w') as file:
    line = file.write(f"{thought}")

a = input("Enter any value between (5 and 9) or press 'quit' to quit : ")
if a.lower() == 'quit':
    exit()

try:
    if (int(a) < 5 or int(a) > 9):
        raise ValueError("Value should be between 5 and 9.")
    else:
        print(f'valid input {a} ')
except Exception as e:
    print(e)




# chatGPT CODE
while True:
    a = input("Enter any value between 5 and 9, or type 'quit' to quit: ").lower()

    if a == 'quit':
        exit()

    try:
        a = int(a)  # Convert to integer after checking for 'quit'
        if 5 <= a <= 9:
            print(f'Valid input: {a}')
        else:
            print("Value should be between 5 and 9.")
    except ValueError as ve:
        print(f"Error: {ve}. Please enter a valid number or 'quit'.")

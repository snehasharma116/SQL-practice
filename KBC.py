questions = [
    ["Which of these is a mutable data type in Python?", "List", "Tuple", "String", "Integer", 1],
    ["What is the capital city of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Who developed the Python programming language?", "Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup", 2],
    ["Which planet is known as the Red Planet?", "Venus", "Jupiter", "Mars", "Saturn", 3],
    ["What is the maximum length of a Python identifier?", "31", "63", "79", "No fixed length", 4]
]

levels = [1000, 5000, 10000, 50000,    ]
money = 0

print("--- KBC Quiz Game ---")                

for i in range(len(questions)):
    current_q = questions[i]
    
    print(f"\nQuestion {i + 1} for Rs. {levels[i]}")
    print(f"Q: {current_q[0]}")
    print(f"1. {current_q[1]}          2. {current_q[2]}")
    print(f"3. {current_q[3]}          4. {current_q[4]}")
    
    user_choice = int(input("\nEnter choice (1-4) or 0 to quit: "))

    if user_choice == 0:
        break

    if user_choice == current_q[5]:
        print(f"Correct! You won Rs. {levels[i]}")
        money = levels[i]
    else:
        print("Wrong answer!")
        if i >= 3:
            money = 10000
        elif i >= 1:
            money = 1000
        else:
            money = 0
        break

print("-" * 20)
print(f"Take Home Amount: Rs. {money}")
print("-" * 20)
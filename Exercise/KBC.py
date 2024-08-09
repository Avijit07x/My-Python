lst = [["1. Who is the father of Computers?",
        "a) James Gosling",
        "b) Charles Babbage",
        "c) Dennis Ritchie",
        "d) Bjarne Stroustrup", "b"],
       ["2. What is the full form of CPU?",
        "a) Computer Processing Unit",
        "b) Computer Principle Unit",
        "c) Central Processing Unit",
        "d) Control Processing Unit", "c"],
       ["Which of the following is the brain of the computer?",
        "a) Central Processing Unit",
        "b) Memory",
        "c) Arithmetic and Logic unit",
        "d) Control unit", "a"],
       ["Which of the following is not a characteristic of a computer?",
        "a) Versatility",
        "b) Accuracy",
        "c) Diligence",
        "d) I.Q.", "d"]]


questions = [item for item in lst if len(item) > 1]
# print(f"{question[0][0]}")

levels = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]


for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f"{question[1]} {question[2]}\n{question[3]} {question[4]}")
    User_input = input("Enter Your Option(a,b,c,d) or '0' to quit:")
    # lower_case = User_input.lower()
    if User_input.lower() == question[5]:
        print(f"Correct Answer!!   You have won Rs {levels[i]}")
    elif User_input == "0":
        print('You Quit')
        break
    elif User_input.lower() != question[5]:
        print("Wrong Answer")
        break

print(f"your take home money is {levels[i-1]}")

print()
print()

Qustions = ("Which planet is closest to the Sun? ",
           "What is the chemical symbol for gold? ",
           "Which of the following is a primary color? ",
           "What is the largest mammal in the world? ",
           "Who painted the Mona Lisa? ")

Options = (("A. Earth", "B. Mars", "C. Venus", "D. Mercury"), 
           ("A. Go", "B. Au", "C. Ag", "D. G"), 
           ("A. Purple", "B. Green", "C. Yellow", "D. Orange"), 
           ("A. Elephant", "B. Blue whale", "C. Giraffe", "D. Hippopotamus"), 
           ("A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo Buonarroti"))

Answers = ("D", "B", "C", "A", "B")
Guesses = []
score = 0
num_Question = 0

for question in Qustions:
    print("-------------------------")
    print(question)
    for oprion in Options[num_Question]:
        print(oprion)

    guess = input("Enter (A,B,C,D): ").upper()
    Guesses.append(guess)

    if guess == Answers[num_Question]:
        score += 1
        print("CORRECT!!! :)")
    else:
        print("INCPRRECT!!! :(")
        print(f"{Answers[num_Question]} is the correct answer")
    num_Question += 1

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

print("answers: ", end="")
for answer in Answers:
    print(answer, end=" ")

print("guesses: ", end="")
for guess in Guesses:
    print(guess, end=" ")
print()

score = int(score / len(Qustions) * 100)
print(f"your score is: {score}%")


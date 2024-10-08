def tally_score():
    score = 0
    if question_one.lower() == "blue":
        score = score + 1

    if question_two.lower() == "crows":
        score = score + 1

    if question_three.title() == "Anthony Dale Engebretson Jr":
        score = score + 1

    if question_four.lower() == 32:
        score = score + 1

    if question_five.lower() == "beige":
        score = score + 1

    print(score)

question_one = input("question 1) what is the color of the sky\n>")
question_two = input("question 2) what is my favorite animal\n>")
question_three = input("question 3) what is my full legal name\n")
question_four = int(input("question 4) what is my favorite number\n>"))
question_five = input("question 5) what is the average color of the universe\n>")

tally_score

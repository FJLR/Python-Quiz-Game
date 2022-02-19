print("Welcome to the real quiz-game")

playing = input("Do you want to play on my Game...! ")

if playing.lower() !="yes":
    quit()

print("Sure - lets play...!")

score = 0

question = input("What is Capital of Canada? ")
if question == "Ottawa":
    print("that is correct answer...!")
    score += 1
else:
    print("Incorrect answer...!")

question = input("What is Capital of Chile? ")
if question == "Santiago":
    print("that is correct answer...!")
    score += 1
else:
    print("Incorrect answer...!")

question = input("is Javascript same as Java? ")
if question.lower() == "no":
    print("that is correct answer...!")
    score += 1
else:
    print("Incorrect answer...!")

question = input("is Python same as Lotus123? ")
if question.lower() == "no":
    print("that is correct answer...!")
    score += 1
else:
    print("Incorrect answer...!")

question = input("what is RAM stand for? ")
if question == "Ramdon Access Memory":
    print("that is correct answer...!")
    score += 1
else:
    print("Incorrect answer...!")

print("you did get " + str(score) + " points...!")
print("you did get " + str((score/5) * 100) + "%")

print("🎮 Welcome to the Quiz Game!")

score = 0

answer1 = input("What is the capital of India? ")

if answer1.lower() == "delhi":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong ❌")

answer2 = input("Which language are you learning? ")

if answer2.lower() == "python":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong ❌")

answer3 = input("How many days are there in a week? ")

if answer3 == "7":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong ❌")

print("🎉 Quiz Finished!")
print("Your final score is:", score)
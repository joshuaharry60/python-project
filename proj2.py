print("Welcome to my word_list Game_1!")


playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Ok! lets play:")
score = 0
answer = input("what is the full meaning of RAM? ")
if answer.lower() == "random access memory":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    print("You got the answer wrong!!!")
    

answer = input("what is the full meaning of ROM? ")
if answer.lower() == "read only memory":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    print("You got the answer wrong!!!")


answer = input("what is the full meaning of HDD? ")
if answer.lower() == "hard disk drive":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    print("You got the answer wrong!!!")

answer = input("what does http stand for? ")
if answer.lower() == "hypertext tranfer protocol":
    print("You are  very correct!! ")
    score +=1
else:
    print(" Incorrect answer!!")

answer = input("what does GPU ")
if answer.lower() == "graphics processing unit":
    print("Correct")
else:
    print("Incorrect answer")

print("You got " + str(score) + " Questions Correct!")
print(f"Thats impresive ...You got {score} Question correct!...")


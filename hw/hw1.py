
number = int(input("Which number you would like to practice: "))

iteration = int(1)
correctAnswer = int(0)

while iteration<=10:    
 
    print(iteration, "x", number,":",end="")
    answer = int(input(" "))
    if answer == number*iteration:
        correctAnswer += 1
        print("Correct !")
        
    else:
        print("Wrong!, Answer is ", number * iteration)
    iteration += 1
print("Practice completed")
print("Accuracy:", correctAnswer, "/", iteration-1)


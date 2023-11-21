num_of_iter = int(input("How many notes do you want to enter?"))
count = 1
notes = []

while count <= num_of_iter:
    print("Enter" + str(count) + ". note:")
    note = int(input())
    if note < 0 or note > 100: 
        print("Notes must be between 0 - 100")
        continue
    notes.append(note)
    count += 1

print("the notes you entered: " + str(notes))

sum_notes = 0 
for note in notes:
    sum_notes += note

avr_notes = sum_notes / num_of_iter

print("the average of notes: " + str(avr_notes))
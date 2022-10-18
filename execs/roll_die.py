import random

global x
x = 5

def roll(times=0):
    face1 = face2 = face3 = face4 = face5 = face6 = 0
    x = 2
    print(x)
    for roll in range(times):
        random_generated = random.randrange(1, 7)
        if random_generated == 1:
            face1 += 1

        if random_generated == 2:
            face2 += 1

        if random_generated == 3:
            face3 += 1

        if random_generated == 4:
            face4 += 1

        if random_generated == 5:
            face5 += 1

        if random_generated == 6:
            face6 += 1

    print(f'face1:  {face1:>13}')
    print("face2: ", face2)
    print("face3: ", face3)
    print("face4: ", face4)
    print("face5: ", face5)
    print("face6: ", face6)
    return face1, face2, face3, face4, face5, face6



def average(*faces):
    print(faces[0])


tuple_faces = roll(times=100)
print(tuple_faces)
print(average(tuple_faces))
# average()

print(x)
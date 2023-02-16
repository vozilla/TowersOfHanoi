#programmers: Ronin Sloan, Tuan Le
#Lab 5 towers of hanoi
#date: 2/16/23
#purpose: create a program that can solve the towers of hanoi puzzle.

#Extra credit: Done in python 3.10

#recursive method
def tower(plate, tower1, tower2, tower3):
    #when puzzel completes, end program
    if plate == 0:
        return
    #moves plates until puzzle completes.
    tower(plate - 1, tower1, tower3, tower2)
    print("Move plate", plate, "from tower", tower1, "to tower", tower2)
    tower(plate - 1, tower3, tower2, tower1)

#initialize plate and call method.
plate = 4
tower(plate, '1', '2', '3')
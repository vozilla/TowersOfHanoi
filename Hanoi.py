def tower(plate, tower1, tower2, tower3):
    if plate == 0:
        return
    tower(plate - 1, tower1, tower3, tower2)
    print("Move plate", plate, "from tower", tower1, "to tower", tower2)
    tower(plate - 1, tower3, tower2, tower1)

plate = 4
tower(plate, '1', '2', '3')
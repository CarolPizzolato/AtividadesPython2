
def sonegativo (x):
    if x < 0:
        return True
    else:
        return False

lista = [x for x in range(-10,5)]

print (list (filter(sonegativo, lista)))

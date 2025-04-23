
def list (c,b):
    a = 4
    vet = [None]*a
    vet.append(c)
    vet.append(b)
    return vet

c = int(input() )
b = int(input() )

print (list (c,b))
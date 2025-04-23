
''' O ideal seria ser assim
def funcao():
    a = [i for i in range(1, 21) if i % 2 == 0]
    print(*a)

funcao()
'''


def funcao():
    a = []
    for i in range (1,21):
        if i % 2 == 0:
            a.append(i)
    print (*a)         

funcao()
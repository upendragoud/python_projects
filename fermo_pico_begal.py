import random
n = int(input('select the size of the digit to be gussed: '))
a = 10**(n-1)
b = '9'*n
guessed = random.randrange(a, int(b))
print(guessed)

N = list(str(guessed))

print(N)

n = int(input("Enter your guess: "))
while n != guessed:
    if n > guessed :
        print()
        n = int(input(f'Enter your another guess where {n} > computer guessed: '))
    else:
        print()
        n = int(input(f'Enter your another guess where {n} <  computer guessed: '))
    for i in list(str(n)):
        l = list(str(n))
        if i in N and l.index(i) == N.index(i):
            print('Fermo', end=" ")
        elif i in N and l.index(i) != N.index(i):
            print('Pico', end=" ")
        else:
            print('Begal', end=" ")






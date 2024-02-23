import random
import string
from collections import defaultdict

lower_case = list(string.ascii_lowercase)
# print(lower_case)
L = []
l = []
C = ["It floats like a log. It looks like a log. But it isn't a log. What is it?",
"I am white when I am dirty, and black when I am clean. What am I?",
"I have two hands, but I can not scratch myself. What am I?",
"What is the hardest key to turn?",
"I walked through a field of wheat, I picked up something good to eat, It was white and had no bone, In twenty-one days it walked alone. What did I pick up?",
"I run all around the pasture but never move. What am I?",
"Four fingers and a thumb, Yet flesh and blood, I have none. What am I?",
"The more you take away, the more I become. What am I?",
"I scream, You scream, We all scream. For what?",
"What jack has a head but no body?",
"I act like a cat, I look like a cat, Yet I am not a cat. What am I?",
"My fleece is white as snow. Everywhere that Mary goes, I go. What am I?",
"I make two people out of one. What am I?",
"What has one eye but cannot see?",
"Who is the strange one who lives in the sea, he has eight arms but no legs. Who is it?",
"I have a thousand needles but I do not sew. What am I?",
"Who is next to a king on his throne?",
"I run in and out of town all day and night. What am I?",
"I have no feet, no hands, no wings, but I climb to the sky. What am I?",
"What pets make stirring music?",
"Roses are red, Violets are blue; And I'm forever saying: I love you. What am I?",
"It shouts along the street, hasn't any lungs, It tugs at leaves and hurls them at people old and young. What is it?",
"Through me, you see through things. What am I?",
"I'm found in socks, scarves, and mittens. I'm found in the paws of playful kittens. What am I?",
"Saws sing it, We snore it, Bees drone it, And one alone ends the alphabet. What is it?",
"What goes up when the rain comes down?"]
D = defaultdict(list)
for i in lower_case:
    D[i].append(C[lower_case.index(i)])
# print(D)
n = int(input("Enter a range: "))
for i in range(n):
    alpha = random.choice(lower_case)
    L.append(alpha)
    l.append(alpha)
# print(L)
WA = []
if n < 9:
    g = n - 3
    for i in range(g):
        ran = random.choice(L)
        WA.append(ran)
        L[L.index(ran)] = '_'
else:
    g = n - 4
    for i in range(g):
        ran = random.choice(L)
        WA.append(ran)
        L[L.index(ran)] = '_'

print("".join(L).capitalize())
w = "".join(WA).replace('_', '')
# print(list(w))
print('Qlues')
for i in range(len(w)):
    print(D[list(w)[i]][0])
j = len(w)*2
for i in range(len(w)*2):
    print(f'you have {j} number of guess left')
    n = input("Enter your guess")
    j -= 1
    if n not in list(w):
        print('You lost the game')
        break
    else:
        print(f'you have {j} number of guess left')
        j -= 1
        L[l.index(n)] = n
        print("".join(L))
        if "".join(L) == "".join(l):
            print('congracts you won the game')
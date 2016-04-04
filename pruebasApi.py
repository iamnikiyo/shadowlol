import random

x = random.randint(0, 4)
mapa = {}
for i in range (4):
	mapa[i] = "background{}.png".format(i)

print (mapa[x])
# opgave 2
mijn_lijst = [5, 12, 19, 27 ,3]
# print(*mijn_lijst)


# opgave 3
mijn_lijst.append(25)
# print(*mijn_lijst)


# opgave 4
lengte_lijst = len(mijn_lijst)
# print(lengte_lijst)


# opgave 5
mijn_lijst.remove(12)
# print(*mijn_lijst)


# opgave 6
#print(*mijn_lijst)
mijn_lijst.remove(5)
#print(*mijn_lijst)


# opgave 7
mijn_lijst.insert(0, 36)
# print(*mijn_lijst)


# opgave 8
test = sum(mijn_lijst)
# print(test)


# opgave 9
mijn_lijst.clear()
# print(*mijn_lijst)


# opgave 10
mijn_lijst.extend([1, 2, 3])
# print(*mijn_lijst)


# opgave 11
mijn_lijst = [1, 2, 3] + list(range(4, 51))
# print(*mijn_lijst)


# opgave 12
positie = mijn_lijst.index(25)
# print(positie)


# opgave 13
# print(*mijn_lijst)
mijn_lijst[0], mijn_lijst[-1] = mijn_lijst[-1], mijn_lijst[0]
# print(*mijn_lijst)


# opgaeve 14
tweede_lijst = [1, "aap", 2, "apen", 3, "watermeloen", 15, 27, 15, "lekker bezig", "6"]
aantal_integers = 0
for item in tweede_lijst:
    if type(item) == int:
        aantal_integers += 1
print(aantal_integers)

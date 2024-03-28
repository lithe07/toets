# zorg ervoor dat test_lib.py in dezelfde directory zit als de toets
from test_lib import test, report

def is_even(getal: int) -> bool:
    return getal % 2 == 0

def get_even_list(lijst: list) -> list:
    even_lijst = []
    for getal in lijst:
        if is_even(getal):
            even_lijst.append(getal)
    return even_lijst

def omgedraaid_even(lijst: list) -> list:
    even_lijst = [getal for getal in lijst if is_even(getal)]
    return list(reversed(even_lijst))

def aantal_even_getallen(lijst: list) -> int:
    count = 0
    for getal in lijst:
        if is_even(getal):
            count += 1
    return count

def is_palindroom(woord: str) -> bool:
    return woord == woord[::-1]


def omgedraaid(lijst: list) -> list:
    reversed_list = []
    for i in range(len(lijst) - 1, -1, -1):
        reversed_list.append(lijst[i])
    return reversed_list


def lijsten_samenvoegen(lijst1: list, lijst2: list) -> list:
    lijst1.extend(lijst2)
    return lijst1

def aantal_palindromen(lijst: list) -> int:
    count = 0
    for woord in lijst:
        if is_palindroom(woord):
            count += 1
    return count

def aantal_even_getallen_op_even_index(lijst: list) -> int:
    count = 0
    for i in range(len(lijst)):
        if i % 2 == 0:
            count += 1
    return count


# opdracht 1a
# bepaal of een getal even is.
# schrijf minimaal 2 extra testen. De eerste 2 testcases zijn weggegeven.
expected = True
result = is_even(2)
test('Opdracht 1a (test 1) is correct', expected, result)

expected = True
result = is_even(0)
test('Opdracht 1a (test 2) is correct', expected, result)

expected = False
result = is_even(3)
test('Opdracht 1a (test 3) is correct', expected, result)

expected = False
result = is_even(5)
test('Opdracht 1a (test 4) is correct', expected, result)


# vraag 1b
# Zorg ervoor dat de functie get_even_list() enkel de even getallen uit de lijst teruggeeft.
# schrijf daarna per opgave minimaal 2 extra testen. De eerste 2 testcases zijn weggegeven.
expected = [2,4]
result = get_even_list([1,2,3,4,5])
test('Opdracht 1b (test 1) is correct', expected, result)

expected = [6,8]
result = get_even_list([1,6,3,8,5])
test('Opdracht 1b (test 2) is correct', expected, result)

expected = [10,16]
result = get_even_list([1,10,3,16])
test('Opdracht 1b (test 3) is correct', expected, result)

expected = [24, 26, 20, 4]
result = get_even_list([27, 15, 24, 26, 7, 20, 1, 4])
test('Opdracht 1b (test 4) is correct', expected, result)

# vraag 2
# Hoeveel even getallen zitten er in de lijst?
# Voeg minimaal 2 testen toe!
expected = 2
result = aantal_even_getallen([1,2,3,4,5])
test('Opdracht 2 (test 1) is correct', expected, result)

expected = 3
result = aantal_even_getallen([8,2,3,4,5])
test('Opdracht 2 (test 2) is correct', expected, result)

expected = 4
result = aantal_even_getallen([4,2,6,4,5])
test('Opdracht 2 (test 3) is correct', expected, result)

# vraag 3
# reversed is een leuke functie, die je echter prima zelf kunt schrijven. Schrijf een functie die een lijst reversed (zonder reversed).
# voeg 2 testen toe!
expected = [5, 4, 3, 2, 1]
result = omgedraaid([1, 2, 3, 4, 5])
test('Opdracht 3 (test 1) is correct', expected, result)

expected = [8, 6, 4, 2, 0]
result = omgedraaid([0, 2, 4, 6, 8])
test('Opdracht 3 (test 2) is correct', expected, result)

expected = [9, 7, 5, 3, 1]
result = omgedraaid([1, 3, 5, 7, 9])
test('Opdracht 3 (test 3) is correct', expected, result)

# vraag 4
# schrijf een functie die een lijst teruggeeft met alle even getallen uit de lijst, maar dan reversed.
# voeg 2 testen toe!
expected = [4, 2]
result = omgedraaid_even([1, 2, 3, 4, 5])
test('Opdracht 4 (test 1) is correct', expected, result)

expected = [8, 6]
result = omgedraaid_even([1, 6, 3, 8, 5])
test('Opdracht 4 (test 2) is correct', expected, result)

expected = [10, 0]
result = omgedraaid_even([1, 0, 3, 10, 5])
test('Opdracht 4 (test 3) is correct', expected, result)


# vraag 5
# Voeg twee lijsten samen.
# voeg 2 testen toe!
expected = [1, 2, 3, 4, 5, 6]
result = lijsten_samenvoegen([1, 2, 3],  [4, 5, 6])
test('Opdracht 5 (test 1) is correct', expected, result)

expected = [1, 2, 3, 6, 7, 8]
result = lijsten_samenvoegen([1, 2, 3],  [6, 7, 8])
test('Opdracht 5 (test 2) is correct', expected, result)

expected = [0, 0, 0, 1, 1, 1]
result = lijsten_samenvoegen([0, 0, 0],  [1, 1, 1])
test('Opdracht 5 (test 3) is correct', expected, result)


# vraag 6
# Schrijf een functie die true teruggeeft als een woord een palindroom is. (voorbeelden hiervan zijn: anna, lepel, parterretrap)
# ook nu weer: voeg 2 testen toe!
expected = True
result = is_palindroom('anna')
test('Opdracht 6 (test 1) is correct', expected, result)

expected = True
result = is_palindroom('lepel')
test('Opdracht 6 (test 2) is correct', expected, result)

expected = True
result = is_palindroom('parterretrap')
test('Opdracht 6 (test 3) is correct', expected, result)


# vraag 7
# Hoeveel palindromen zitten er in de lijst?
# voeg 2 testen toe!
expected = 3
result = aantal_palindromen(['anna', 'lepel', 'developer', 'parterretrap', 'test'])
test('Opdracht 7 (test 1) is correct', expected, result)

expected = 1
result = aantal_palindromen(['anna',  'developer',  'test'])
test('Opdracht 7 (test 2) is correct', expected, result)

expected = 2
result = aantal_palindromen(['anna',  'developer', 'parterretrap', 'test'])
test('Opdracht 7 (test 3) is correct', expected, result)


# vraag 8
# Breinkraker: hoeveel even getallen bevinden zich op een even index in de lijst? (index  0 is ook even)
# voeg 2 testen toe!
expected = 3
result = aantal_even_getallen_op_even_index([2, 3, 4, 5, 6])
test('Opdracht 8 (test 1) is correct', expected, result)

expected = 3
result = aantal_even_getallen_op_even_index([1, 2, 3, 4, 5, 6])
test('Opdracht 8 (test 2) is correct', expected, result)

expected = 4
result = aantal_even_getallen_op_even_index([1, 2, 3, 4, 5, 6, 8])
test('Opdracht 8 (test 3) is correct', expected, result)


expected = 4
result = aantal_even_getallen_op_even_index([1, 2, 3, 4, 5, 6, 7, 8])
test('Opdracht 8 (test 4) is correct', expected, result)


report()










# zorg ervoor dat test_lib.py in dezelfde directory zit als de toets
from test_lib import test, report

def is_even(getal: int) -> bool:
    return getal % 2 == 0

def get_even_list(lijst: list) -> list:
    return list(filter(is_even, lijst))

def omgedraaid_even(lijst: list) -> list:
    new = []
    for el in lijst:
        if is_even(el):
            new.insert(0, el)
    return new

def aantal_even_getallen(lijst: list) -> int:
    return len(get_even_list(lijst))
def is_palindroom(woord: str) -> bool:
    return woord == woord[::-1]

def omgedraaid(lijst: list) -> list:
    new = []
    for el in lijst:
        new.insert(0, el)
    return new

def lijsten_samenvoegen(lijst1: list, lijst2: list) -> list:
    return lijst1 + lijst2

def aantal_palindromen(lijst: list) -> int:
    return len(list(filter(is_palindroom, lijst)))

def aantal_even_getallen_op_even_index(lijst: list) -> int:
    teller = 0
    for idx, el in enumerate(lijst):
        if is_even(idx) and is_even(el):
            teller += 1
    return teller

# opdracht 1a
# bepaal of een getal even is.
# schrijf minimaal 2 extra testen. De eerste 2 testcases zijn weggegeven.
expected = True
result = is_even(2)
test('Opdracht 1a (test 1) is correct', expected, result)

expected = False
result = is_even(3)
test('Opdracht 1a (test 2) is correct', expected, result)

expected = False
result = is_even(27)
test('Opdracht 1a (test 2) is correct', expected, result)

expected = False
result = is_even(28)
test('Opdracht 1a (test 2) is correct', expected, result)

# haal deze regel uit commentaar om de uitslag te laten zien. (en verplaats de regel naar je volgende opdracht)
#report()

# vraag 1b
# Zorg ervoor dat de functie get_even_list() enkel de even getallen uit de lijst teruggeeft.
# schrijf daarna per opgave minimaal 2 extra testen. De eerste 2 testcases zijn weggegeven.
expected = [2,4]
result = get_even_list([1,2,3,4,5])
test('Opdracht 1b (test 1) is correct', expected, result)

expected = [24, 16, 12, 2]
result = get_even_list([27, 15, 24, 16, 7, 12, 1, 2])
test('Opdracht 1b (test 2) is correct', expected, result)

expected = [2]
result = get_even_list([1, 1, 2, 1, 1])
test('Opdracht 1b (test 3) is correct', expected, result)

expected = []
result = get_even_list([1, 1,  1, 1])
test('Opdracht 1b (test 4) is correct', expected, result)

# vraag 2
# Hoeveel even getallen zitten er in de lijst?
# Voeg minimaal 2 testen toe!
expected = 2
result = aantal_even_getallen([1,2,3,4,5])
test('Opdracht 2 (test 1) is correct', expected, result)

expected = 1
result = aantal_even_getallen([1,2,3,17,5])
test('Opdracht 2 (test 2) is correct', expected, result)

expected = 5
result = aantal_even_getallen([4,2,6,8,12])
test('Opdracht 2 (test 2) is correct', expected, result)

# vraag 3
# reversed is een leuke functie, die je echter prima zelf kunt schrijven. Schrijf een functie die een lijst reversed (zonder reversed).
# voeg 2 testen toe!
expected = [5, 4, 3, 2, 1]
result = omgedraaid([1, 2, 3, 4, 5])
test('Opdracht 3 (test 1) is correct', expected, result)

expected = [1, 2, 3, 4, 5]
result = omgedraaid([5, 4, 3, 2, 1])
test('Opdracht 3 (test 2) is correct', expected, result)

expected = [1, 2]
result = omgedraaid([2, 1])
test('Opdracht 3 (test 3) is correct', expected, result)

# vraag 4
# schrijf een functie die een lijst teruggeeft met alle even getallen uit de lijst, maar dan reversed.
# voeg 2 testen toe!
expected = [4, 2]
result = omgedraaid_even([1, 2, 3, 4, 5])
test('Opdracht 4 (test 1) is correct', expected, result)

expected = [6, 4, 2]
result = omgedraaid_even([1, 2, 3, 4, 5, 47, 15, 15, 6, 23, 17])
test('Opdracht 4 (test 2) is correct', expected, result)

expected = []
result = omgedraaid_even([1, 3, 5, 47, 15, 15, 23, 17])
test('Opdracht 4 (test 3) is correct', expected, result)

# vraag 5
# Voeg twee lijsten samen.
# voeg 2 testen toe!
expected = [1, 2, 3, 4, 5, 6]
result = lijsten_samenvoegen([1, 2, 3],  [4, 5, 6])
test('Opdracht 5 (test 1) is correct', expected, result)

expected = []
result = lijsten_samenvoegen([],  [])
test('Opdracht 5 (test 2) is correct', expected, result)

expected = [1, 2]
result = lijsten_samenvoegen([1],  [2])
test('Opdracht 5 (test 3) is correct', expected, result)

# vraag 6
# Schrijf een functie die true teruggeeft als een woord een palindroom is. (voorbeelden hiervan zijn: anna, lepel, parterretrap)
# ook nu weer: voeg 2 testen toe!
expected = True
result = is_palindroom('anna')
test('Opdracht 6 (test 1) is correct', expected, result)

expected = False
result = is_palindroom('fiets')
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

expected = 0
result = aantal_palindromen(['sanne', 'lepels', 'developers', 'trap', 'test'])
test('Opdracht 7 (test 2) is correct', expected, result)

expected = 1
result = aantal_palindromen(['sanne', 'lepel', 'developers', 'trap', 'test'])
test('Opdracht 7 (test 3) is correct', expected, result)

# vraag 8
# Breinkraker: hoeveel even getallen bevinden zich op een even index in de lijst? (index  0 is ook even)
# voeg 2 testen toe!
expected = 3
result = aantal_even_getallen_op_even_index([2, 3, 4, 5, 6])
test('Opdracht 8 (test 1) is correct', expected, result)

expected = 0
result = aantal_even_getallen_op_even_index([1, 2, 3, 4, 5, 6])
test('Opdracht 8 (test 2) is correct', expected, result)

expected = 3
result = aantal_even_getallen_op_even_index([2, 3, 4, 5, 6])
test('Opdracht 8 (test 3) is correct', expected, result)

report()










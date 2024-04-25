# zorg ervoor dat test_lib.py in dezelfde directory zit als de toets
from test_lib import test, report
import random

def is_even(getal: int) -> bool:
    return getal % 2 == 0

def get_even_list(lijst: list) -> list:
    evens = []
    for nr in lijst:
        if is_even(nr):
            evens.append(nr)
    return evens

def omgedraaid_even(lijst: list) -> list:
    evens = get_even_list(lijst)
    return omgedraaid(evens)

def aantal_even_getallen(lijst: list) -> int:
    evens = get_even_list(lijst)
    return len(evens)

def is_palindroom(woord: str) -> bool:
    omgekeerd = ''
    for character in woord:
        omgekeerd  = character + omgekeerd
    return woord == omgekeerd

def omgedraaid(lijst: list) -> list:
    lijst_omgedraaid = []
    for nr in lijst:
        lijst_omgedraaid.insert(0,nr)
    return lijst_omgedraaid

def lijsten_samenvoegen(lijst1: list, lijst2: list) -> list:
    return lijst1 + lijst2
 
def aantal_palindromen(lijst: list) -> int:
    count = 0
    for woord in lijst:
        if is_palindroom(woord):
            count += 1
    return count

def aantal_even_getallen_op_even_index(lijst: list) -> int:
    count = 0
    for index in range(0,len(lijst),2):
        if is_even(lijst[index]):
            count += 1
    return count

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
result = is_even(-3)
test('Opdracht 1a (test 3) is correct', expected, result)

expected = True
result = is_even(random.randint(1,10000)*2)
test('Opdracht 1a (test 4) is correct', expected, result)

# vraag 1b
# Zorg ervoor dat de functie get_even_list() enkel de even getallen uit de lijst teruggeeft.
# schrijf daarna per opgave minimaal 2 extra testen. De eerste 2 testcases zijn weggegeven.

even = random.randint(1,20000) * 2
oneven = random.randint(1,20000) * 2 + 1

getal1 = random.randint(1,200)
getal2 = random.randint(1,200)
getal3 = random.randint(1,200)

expected = [2,4]
result = get_even_list([1,2,3,4,5])
test('Opdracht 1b (test 1) is correct', expected, result)

expected = [24, 16, 12, 2]
result = get_even_list([27, 15, 24, 16, 7, 12, 1, 2])
test('Opdracht 1b (test 2) is correct', expected, result)

even = random.randint(1,20000) * 2
expected = [even]
result = get_even_list([3,-1,7,even,121])
test('Opdracht 1b (test 3) is correct', expected, result)

expected = [-400000]
result = get_even_list([3,-1,7,121, -400000])
test('Opdracht 1b (test 4) is correct', expected, result)

# vraag 2
# Hoeveel even getallen zitten er in de lijst?
# Voeg minimaal 2 testen toe!
expected = 2
result = aantal_even_getallen([1,2,3,4,5])
test('Opdracht 2 (test 1) is correct', expected, result)

expected = 3
result = aantal_even_getallen([1,2,3,4,5, even, oneven])
test('Opdracht 2 (test 2) is correct', expected, result)

expected = 0
result = aantal_even_getallen([])
test('Opdracht 2 (test 3) is correct', expected, result)
# vraag 3
# reversed is een leuke functie, die je echter prima zelf kunt schrijven. Schrijf een functie die een lijst reversed (zonder reversed).
# voeg 2 testen toe!
expected = [5, 4, 3, 2, 1]
result = omgedraaid([1, 2, 3, 4, 5])
test('Opdracht 3 (test 1) is correct', expected, result)

expected = [getal3, 5, getal2, 3, getal1, 1]
result = omgedraaid([1, getal1, 3, getal2, 5, getal3])
test('Opdracht 3 (test 2) is correct', expected, result)

expected = [getal3]
result = omgedraaid([getal3])
test('Opdracht 3 (test 3) is correct', expected, result)

# vraag 4
# schrijf een functie die een lijst teruggeeft met alle even getallen uit de lijst, maar dan reversed.
# voeg 2 testen toe!
expected = [4, 2]
result = omgedraaid_even([1, 2, 3, 4, 5])
test('Opdracht 4 (test 1) is correct', expected, result)

expected = [getal1 * 2, getal2 * 2]
result = omgedraaid_even([1, expected[1], 3, expected[0], 5])
test('Opdracht 4 (test 2) is correct', expected, result)

expected = []
result = omgedraaid_even([1])
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

# vraag 6
# Schrijf een functie die true teruggeeft als een woord een palindroom is. (voorbeelden hiervan zijn: anna, lepel, parterretrap)
# ook nu weer: voeg 2 testen toe!
expected = True
result = is_palindroom('anna')
test('Opdracht 6 (test 1) is correct', expected, result)

# vraag 7
# Hoeveel palindromen zitten er in de lijst?
# voeg 2 testen toe!
expected = 3
result = aantal_palindromen(['anna', 'lepel', 'developer', 'parterretrap', 'test'])
test('Opdracht 7 (test 1) is correct', expected, result)

# vraag 8
# Breinkraker: hoeveel even getallen bevinden zich op een even index in de lijst? (index  0 is ook even)
# voeg 2 testen toe!
expected = 3
result = aantal_even_getallen_op_even_index([2, 3, 4, 5, 6])
test('Opdracht 8 (test 1) is correct', expected, result)

expected = 0
result = aantal_even_getallen_op_even_index([1, 2, 3, 4, 5, 6])
test('Opdracht 8 (test 2) is correct', expected, result)

report()










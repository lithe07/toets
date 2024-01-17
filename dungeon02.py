import time, math
import random

player_attack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
schatkist = 'sleutel'

eerste_getal = random.randint(10, 25)
tweede_getal = random.randint(-5, 75)
juiste_antwoord = eerste_getal + tweede_getal

print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')

print(f'Daarboven zie je een som staan {eerste_getal} + {tweede_getal}')
antwoord = int(input('Wat toest je in? '))

if antwoord == juiste_antwoord:
    print("Juist je hebt goed gerekent")
    print(f"Hier bij krijg je de {schatkist} van de schatkist")
else:
    print("helaas dat is niet de juiste antwoord")
print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(1) 

# === [kamer 6] === # de oude zombie is verhuisd 
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)
    player_health -= player_attack_amount * zombie_hit_damage

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
print('')
time.sleep(1)

# === [kamer 3] === #
item = random.choice(["schild", "Zwaard"])

print('Je duwt hem open en stap een hele lange kamer binnen.')
if item == "schild":
    print(f"Je hebt {item} gerkregen en je hebt 1 punt extra voor je defense")
    player_defense += 1
else:
    print(f"Je hebt {item} gekregen en je hebt 2 punten extra voor je attack ")
    player_attack += 2
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === # de niewue plek zombie 
zombie_attack = 2
zombie_defense = 0
zombie_health = 3
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')   
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if antwoord == juiste_antwoord:
    print("Je kan de schatkist open maken je hebt gewonnen")
else:
    print("Je kan de schatkist niet open maken. je verliest")
    print("Game over")
exit()
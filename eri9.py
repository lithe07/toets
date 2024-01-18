# # kamer1 #
# print("Dat is kamer-1")

# #kamer7 #
# print('Dat is kamer-7')
# kamer_kiezen = int(input("Welke kamer wil je heen gaan 8/2? "))
# if kamer_kiezen == 2:
#     # kamer2 #
#     print("Dat is kamer-2")
#     kamer_kiezen = int(input("Welke kamer wil je heen gaan 8/6? "))
#     if kamer_kiezen == 6:
#         # kamer6 #
#         print("Dat is kamer-6")
#         kamer_kiezen = int(input("Welke kamer wil je heen gaan 8/3? "))
#         if kamer_kiezen == 8:
#             # kamer8 #
#             print("Dat is kamer-8")
#             kamer_kiezen = int(input("Welke kamer wil je heen gaan 9/3? "))
#             if kamer_kiezen == 9:
#                 # kamer9 #
#                 print("Dat is kamer-9")
# # kamer3 #
# print("Dat is kamer-3")



# kamer1 #
print("Dat is kamer-1")

# kamer7 #
print('Dat is kamer-7')
kamer_kiezen = int(input("Welke kamer wil je heen gaan 8/2? "))
if kamer_kiezen == 2:
    # kamer2 #
    print("Dat is kamer-2")
    kamer_kiezen = int(input("Welke kamer wil je heen gaan 8/6? "))
    if kamer_kiezen == 6:
        # kamer6 #
        print("Dat is kamer-6")
        kamer_kiezen = int(input("Welke kamer wil je heen gaan 8/3? "))
        if kamer_kiezen == 8:
            # kamer8 #
            print("Dat is kamer-8")
            kamer_kiezen = int(input("Welke kamer wil je heen gaan 9/3? "))
            if kamer_kiezen == 9:
                # kamer9 #
                print("Dat is kamer-9")
            elif kamer_kiezen == 3:
                # kamer3 #
                print("Dat is kamer-3")
    elif kamer_kiezen == 8:
        # kamer8 #
        print("Dat is kamer-8")
        kamer_kiezen = int(input("Welke kamer wil je heen gaan 9/3? "))
        if kamer_kiezen == 9:
            # kamer9 #
            print("Dat is kamer-9")
        elif kamer_kiezen == 3:
            # kamer3 #
            print("Dat is kamer-3")
elif kamer_kiezen == 3:
    # kamer3 #
    print("Dat is kamer-3")






























def ga_naar_kamer(kamer_nummer):
    print(f"Dat is kamer-{kamer_nummer}")

# kamer1 #
ga_naar_kamer(1)

# kamer7 #
ga_naar_kamer(7)
kamer_kiezen = int(input("Welke kamer wil je heen gaan 8/2? "))
if kamer_kiezen == 2:
    # kamer2 #
    ga_naar_kamer(2)
    kamer_kiezen = int(input("Welke kamer wil je heen gaan 8/6? "))
    if kamer_kiezen == 6:
        # kamer6 #
        ga_naar_kamer(6)
        kamer_kiezen = int(input("Welke kamer wil je heen gaan 8/3? "))
        if kamer_kiezen in [8, 3]:
            # kamer8 of kamer3 #
            ga_naar_kamer(kamer_kiezen)
elif kamer_kiezen == 3:
    # kamer3 #
    ga_naar_kamer(3)


























    
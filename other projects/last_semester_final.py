import random

player = {
    "wins": 0,
    "money": 500000,
    "car": "",
    "skill": 7.5,
    "titles": [],
    "tire_age": 0
}
cars = {
    "ae86": {"name": "Toyota AE86 Trueno", "tires": 40000, "grip": 5, "hp": 130, "price": 120000},
    "fd_rx7": {"name": "Mazda RX-7 FD3S", "tires": 100000, "grip": 8, "hp": 200, "price": 350000},
    "nismo": {"name": "nismo", "tires": 500000, "grip": 25, "hp": 600, "price": 1500000},
    "ae85": {"name": "Toyota AE85 Levin", "tires": 60000, "grip": 4, "hp": 85, "price": 90000},
    "supra_rz": {"name": "Toyota Supra RZ", "tires": 150000, "grip": 9, "hp": 320, "price": 420000},
    "mr2_sw20": {"name": "Toyota MR2 SW20", "tires": 90000, "grip": 7, "hp": 200, "price": 220000},
    "celica_st204": {"name": "Toyota Celica ST204", "tires": 95000, "grip": 7, "hp": 170, "price": 180000},
    "fc_rx7": {"name": "Mazda RX-7 FC3S", "tires": 90000, "grip": 7, "hp": 180, "price": 200000},
    "roadster_na6ce": {"name": "Mazda Eunos Roadster NA6CE", "tires": 70000, "grip": 6, "hp": 115, "price": 140000},
    "eg6_civic": {"name": "Honda Civic SiR-II EG6", "tires": 85000, "grip": 7, "hp": 170, "price": 170000},
    "ek9_civic": {"name": "Honda Civic Type R EK9", "tires": 95000, "grip": 8, "hp": 185, "price": 240000},
    "nsx_na1": {"name": "Honda NSX NA1", "tires": 150000, "grip": 10, "hp": 280, "price": 600000},
    "crx_ef8": {"name": "Honda CR-X EF8", "tires": 80000, "grip": 6, "hp": 150, "price": 150000},
    "silvia_s13": {"name": "Nissan Silvia S13", "tires": 80000, "grip": 7, "hp": 160, "price": 160000},
    "silvia_s14": {"name": "Nissan Silvia S14", "tires": 85000, "grip": 7, "hp": 200, "price": 190000},
    "silvia_s15": {"name": "Nissan Silvia S15", "tires": 95000, "grip": 8, "hp": 250, "price": 260000},
    "skyline_r32": {"name": "Nissan Skyline GT-R R32", "tires": 140000, "grip": 10, "hp": 280, "price": 550000},
    "skyline_r34": {"name": "Nissan Skyline GT-R R34", "tires": 160000, "grip": 10, "hp": 320, "price": 750000},
    "180sx": {"name": "Nissan 180SX", "tires": 85000, "grip": 7, "hp": 170, "price": 170000},
    "sil80": {"name": "Nissan SilEighty", "tires": 80000, "grip": 7, "hp": 175, "price": 175000},
    "evo3": {"name": "Mitsubishi Lancer Evolution III", "tires": 130000, "grip": 9, "hp": 270, "price": 300000},
    "evo4": {"name": "Mitsubishi Lancer Evolution IV", "tires": 135000, "grip": 9, "hp": 280, "price": 320000},
    "evo5": {"name": "Mitsubishi Lancer Evolution V", "tires": 140000, "grip": 9, "hp": 280, "price": 340000},
    "evo6": {"name": "Mitsubishi Lancer Evolution VI", "tires": 145000, "grip": 9, "hp": 280, "price": 360000},
    "impreza": {"name": "Subaru Impreza WRX STi GC8", "tires": 120000, "grip": 9, "hp": 280, "price": 300000},
    "cappuccino": {"name": "Suzuki Cappuccino EA11R", "tires": 60000, "grip": 6, "hp": 65, "price": 70000},
    "benz_190e": {"name": "Mercedes-Benz 190E W201", "tires": 110000, "grip": 8, "hp": 170, "price": 230000},
    "porsche_911": {"name": "Porsche 911 Turbo 964", "tires": 160000, "grip": 10, "hp": 320, "price": 900000},
    "alfa_romeo_4c": {"name": "Alfa Romeo 4C", "tires": 140000, "grip": 9, "hp": 240, "price": 380000}
}
enemies = {
    "takahashi": {"name": "Ryosuke Takahashi", "car": "fc_rx7", "track": "Akagi", "skill": 9, "beaten": 0},
    "impact_blue": {"name": "Mako Sato & Sayuki", "car": "sil80", "track": "Usui Pass", "skill": 6, "beaten": 0},
    "bunta": {"name": "Bunta Fujiwara", "car": "impreza", "track": "Akina", "skill": 12, "beaten": 0},
    "takeshi": {"name": "Takeshi Nakazato", "car": "skyline_r32", "track": "Myogi", "skill": 8, "beaten": 0},
    "shingo": {"name": "Shingo Shoji", "car": "eg6_civic", "track": "Myogi", "skill": 6, "beaten": 0},
    "kyoichi": {"name": "Kyoichi Sudo", "car": "evo3", "track": "Akagi", "skill": 8, "beaten": 0},
    "seiji": {"name": "Seiji Iwaki", "car": "evo4", "track": "Akina", "skill": 7, "beaten": 0},
    "hideo": {"name": "Hideo Minagawa", "car": "supra_rz", "track": "Nikko", "skill": 7, "beaten": 0},
    "kai": {"name": "Kai Kogashiwa", "car": "mr2_sw20", "track": "Nikko", "skill": 8, "beaten": 0},
    "tomoyuki": {"name": "Tomoyuki Tachi", "car": "evo5", "track": "Shomaru", "skill": 7, "beaten": 0},
    "daiki": {"name": "Daiki Ninomiya", "car": "ek9_civic", "track": "Shomaru", "skill": 7, "beaten": 0},
    "hiroya": {"name": "Hiroya Okuyama", "car": "silvia_s15", "track": "Nagao", "skill": 7, "beaten": 0},
    "go": {"name": "Go Hojo", "car": "nsx_na1", "track": "Tsuchisaka", "skill": 9, "beaten": 0},
    "kozo": {"name": "Kozo Hoshino", "car": "cappuccino", "track": "Tsuchisaka", "skill": 8, "beaten": 0},
    "wataru": {"name": "Wataru Akiyama", "car": "ae86", "track": "Shomaru", "skill": 7, "beaten": 0},
    "shinji": {"name": "Shinji Inui", "car": "roadster_na6ce", "track": "Nagao", "skill": 9, "beaten": 0},
    "ryo": {"name": "Ryo Shinigami", "car": "evo6", "track": "Tsuchisaka", "skill": 9, "beaten": 0}
}

def akina(player, cars, enemies):
    print("Welcome to Mount Akina.")
    akinas = []
    for e in enemies:
        if "Akina" == enemies[e]["track"]:
            akinas.append(e)
    enemy = random.choice(akinas)
    turns = 25
    player, enemies = combat(turns, enemy, player, cars, enemies)
    if player["car"] != "supra_rz":
        inp = input("Well, I don't really care the result. Here's a supra if you want it. (y/n) ")
        if inp == "y":
            player["car"] = "supra_rz"
    return player, enemies
def akagi(player, cars, enemies):
    print("Welcome to Mount Akagi.")
    akagis = []
    for e in enemies:
        if "Akagi" in enemies[e]["track"]:
            akagis.append(e)
    enemy = random.choice(akagis)
    turns = 30
    player, enemies = combat(turns, enemy, player, cars, enemies)
    if player["car"] != "180sx":
        inp = input("Well, I don't really care the result. Here's a 180sx if you want it. (y/n) ")
        if inp == "y":
            player["car"] = "180sx"
    return player, enemies
def myogi(player, cars, enemies):
    print("Welcome to Mount Myogi.")
    myogis = []
    for e in enemies:
        if "Myogi" in enemies[e]["track"]:
            myogis.append(e)
    enemy = random.choice(myogis)
    turns = 18
    player, enemies = combat(turns, enemy, player, cars, enemies)
    if player["car"] != "evo5":
        inp = input("Well, I don't really care the result. Here's a evo if you want it. (y/n) ")
        if inp == "y":
            player["car"] = "evo5"
    return player, enemies
def usui(player, cars, enemies):
    print("Welcome to Usui Pass.")
    usuis = []
    for e in enemies:
        if "Usui" in enemies[e]["track"]:
            usuis.append(e)
    enemy = random.choice(usuis)
    turns = 50
    player, enemies = combat(turns, enemy, player, cars, enemies)
    if player["car"] != "skyline_r32":
        inp = input("Well, I don't really care the result. Here's a r32 if you want it. (y/n) ")
        if inp == "y":
            player["car"] = "skyline_r32"
    return player, enemies
def nikko(player, cars, enemies):
    print("Welcome to Mount Nikko.")
    nikkos = []
    for e in enemies:
        if "Nikko" in enemies[e]["track"]:
            nikkos.append(e)
    enemy = random.choice(nikkos)
    turns = 20
    player, enemies = combat(turns, enemy, player, cars, enemies)
    if player["car"] != "cappuccino":
        inp = input("Well, I don't really care the result. Here's a cappuccino if you want it. (y/n) ")
        if inp == "y":
            player["car"] = "cappuccino"
    return player, enemies
def shomaru(player, cars, enemies):
    print("Welcome to Mount Shomaru.")
    shomarus = []
    for e in enemies:
        if "Shomaru" in enemies[e]["track"]:
            shomarus.append(e)
    enemy = random.choice(shomarus)
    turns = 20
    player, enemies = combat(turns, enemy, player, cars, enemies)
    if player["car"] != "ek9_civic":
        inp = input("Well, I don't really care the result. Here's a ek9 if you want it. (y/n) ")
        if inp == "y":
            player["car"] = "ek9_civic"
    return player, enemies
def tsuchisaka(player, cars, enemies):
    print("Welcome to Mount Tsuchisaka.")
    tsuchisakas = []
    for e in enemies:
        if "Tsuchisaka" in enemies[e]["track"]:
            tsuchisakas.append(e)
    enemy = random.choice(tsuchisakas)
    turns = 15
    player, enemies = combat(turns, enemy, player, cars, enemies)
    if player["car"] != "fd_rx7":
        inp = input("Well, I don't really care the result. Here's a rx7 if you want it. (y/n) ")
        if inp == "y":
            player["car"] = "fd_rx7"
    return player, enemies
def nagao(player, cars, enemies):
    print("Welcome to Mount Nagao.")
    nagaos = []
    for e in enemies:
        if "Nagao" in enemies[e]["track"]:
            nagaos.append(e)
    enemy = random.choice(nagaos)
    turns = 15
    player, enemies = combat(turns, enemy, player, cars, enemies)
    if player["car"] != "impreza":
        inp = input("Well, I don't really care the result. Here's an impreza if you want it. (y/n) ")
        if inp == "y":
            player["car"] = "impreza"
    return player, enemies
def haruna(player, cars, enemies):
    print("Welcome to Mount Haruna.")
    harunas = []
    for e in enemies:
        if "Akina" == enemies[e]["track"]:
            harunas.append(e)
    enemy = random.choice(harunas)
    turns = 25
    player, enemies = combat(turns, enemy, player, cars, enemies)
    if player["car"] != "nsx_na1":
        inp = input("Well, I don't really care the result. Here's a nsx if you want it. (y/n) ")
        if inp == "y":
            player["car"] = "nsx_na1"
    return player, enemies

def combat(turns, enemy, player, cars, enemies):
    if random.choice([0, 1]) == 0:
        order = 0
    else:
        order = 1
    print(f"You have engaged in combat with {enemies[enemy]["name"]} in their {cars[enemies[enemy]["car"]]["name"]}")
    while turns > 0:
        if order == 0:
            act = input("You're approaching the turn...\n Defend inside (di)\n Defend outside (do)\n Give position (g)\nWhat would you like to do? ").strip().lower()
            while act != "di" and act != "do" and act != "g":
                act = input("That was not a valid action. What would you like to do? ")
            print("\033c", end="")
            botpass = (random.random() * 5) + (cars[enemies[enemy]["car"]]["hp"] / 100) + (cars[enemies[enemy]["car"]]["grip"] / 15) + (enemies[enemy]["skill"] / 5) - .5
            if act == "di":
                if botpass > 8.5:
                    print("Your opponent passes you...")
                    order = 1
                else:
                    print("You successfully fend off your opponent...")
            elif act == "do":
                if botpass > 8:
                    print("Your opponent passes you...")
                    order = 1
                else:
                    print("You successfully fend off your opponent...")
            else:
                print("You give away your position to your opponent...")
        else:
            act = input("You're approaching the turn...\n Take inside (ti)\n Take outside (to)\n Stay (s)\nWhat would you like to do? ").strip().lower()
            while act != "ti" and act != "to" and act != "s":
                act = input("That was not a valid action. What would you like to do? ")
            print("\033c", end="")
            playerpass = (random.random() * 5) + (cars[player["car"]]["hp"] / 100) + (cars[player["car"]]["grip"] / 15) + (enemies[enemy]["skill"] / 5) - player["tire_age"]
            if act == "ti":
                if playerpass > 8.5:
                    print("You succesfully pass your opponent...")
                    order = 0
                else:
                    print("You failed to pass your opponent...")
            elif act == "to":
                if playerpass > 8:
                    print("You succesfully pass your opponent...")
                    order = 0
                else:
                    print("You failed to pass your opponent...")
            else:
                print("You give away your position to your opponent...")
        if cars[enemies[enemy]["car"]]["hp"] > cars[player["car"]]["hp"] and order == 1:
            valid = True
        elif cars[enemies[enemy]["car"]]["hp"] < cars[player["car"]]["hp"] and order == 0:
            valid = True
        else:
            valid = False
        if valid == True and order == 1 and input("Would you like to try and overtake in the straightaway (y/n) ") == "y" or valid == True and order == 0 and random.choice([0, 1]) == 0:
            if order == 0:
                print("Your opponent is attempting to overtake...")
                act = input("You're approaching the straightaway...\n Defend left (l)\n Defend right (r)\n Give position (g)\nWhat would you like to do? ").strip().lower()
                while act != "l" and act != "r" and act != "g":
                    act = input("That was not a valid action. What would you like to do? ").strip().lower()
                print("\033c", end="")
                botpass = (random.random() * 5) + (cars[enemies[enemy]["car"]]["hp"] / 100) + (cars[enemies[enemy]["car"]]["grip"] / 15) + (enemies[enemy]["skill"] / 5) - .5
                if botpass > 10:
                    print("Your opponent passes you...")
                    order = 1
                else:
                    print("You successfully fend off your opponent...")
            else:
                act = input("You're approaching the straightaway...\n Attack left (l)\n Attack right (r)\nWhat would you like to do? ").strip().lower()
                while act != "l" and act != "r":
                    act = input("That was not a valid action. What would you like to do? ").strip().lower()
                print("\033c", end="")
                playerpass = (random.random() * 5) + (cars[player["car"]]["hp"] / 100) + (cars[player["car"]]["grip"] / 15) + (enemies[enemy]["skill"] / 5) - player["tire_age"]
                if playerpass > 8:
                    print("You succesfully pass your opponent...")
                    order = 0
                else:
                    print("You failed to pass your opponent...")
        turns -= 1
    if order == 0:
        print("Congratulations! You won the battle! Your skill increases and you gain 25000 yen.")
        player["money"] += 25000
        player["wins"] += 1
        player["skill"] += .5
        enemies[enemy]["beaten"] += 1
    else:
        print("welp. you lost...")
    return player, enemies

def main(player, cars, enemies):
    while True:
        akina_wins = 0
        akagi_wins = 0
        myogi_wins = 0
        nikko_wins = 0
        shomaru_wins = 0
        tsuchi_wins = 0
        nagao_wins = 0
        for e in enemies:
            if enemies[e]["track"] == "Usui" and enemies[e]["beaten"] > 0:
                player["titles"].append("Usui Pass")
            if enemies[e]["track"] == "Akina" and enemies[e]["beaten"] > 0:
                akina_wins += 1
            if akina_wins >= 2:
                player["titles"].append("Mt. Akina")
            if enemies[e]["track"] == "Akagi" and enemies[e]["beaten"] > 0:
                akagi_wins += 1
            if akagi_wins >= 2:
                player["titles"].append("Mt. Akagi")
            if enemies[e]["track"] == "Myogi" and enemies[e]["beaten"] > 0:
                myogi_wins += 1
            if myogi_wins >= 2:
                player["titles"].append("Mt. Myogi")
            if enemies[e]["track"] == "Nikko" and enemies[e]["beaten"] > 0:
                nikko_wins += 1
            if nikko_wins >= 2:
                player["titles"].append("Mt. Nikko")
            if enemies[e]["track"] == "Shomaru" and enemies[e]["beaten"] > 0:
                shomaru_wins += 1
            if shomaru_wins >= 3:
                player["titles"].append("Mt. Shomaru")
            if enemies[e]["track"] == "Tsuchisaka" and enemies[e]["beaten"] > 0:
                tsuchi_wins += 1
            if tsuchi_wins >= 3:
                player["titles"].append("Mt. Tsuchisaka")
            if enemies[e]["track"] == "Nagao" and enemies[e]["beaten"] > 0:
                nagao_wins += 1
            if nagao_wins >= 2:
                player["titles"].append("Mt. Nagao")
        if len(player["titles"]) >= 3:
            keep = input("You won! Would you like to keep playing? (yes/no)").strip().lower()
            if keep == "yes":
                pass
            else:
                break
        act = input(f"Would you like to buy new tires or a new car? Your money: {player['money']} (tires/car/no) ").strip().lower()
        if act == "tires":
            print(f"You spent {cars[player["car"]]["tires"]} on new tires.")
        elif act == "car":
            print(f"These are your options for cars:")
            for car in cars:
                print(f" {car}; {cars[car]['price']}")
            new_car = input("What car would you like? (make sure it's exactly the same) ").strip().lower()
            while new_car not in cars or player["money"] < cars[new_car]["price"]:
                if new_car not in cars:
                    new_car = input("That was not a valid car. Choose again: ").strip().lower()
                else:
                    new_car = input("You do not have enough money for that car. Choose again: ").strip().lower()
            print(f"You bought a(n) {new_car}")
            player["car"] = new_car
            player["money"] -= cars[new_car]["price"]
        goto = input("Where would you like to go to?\n Your options are: akina, akagi, myogi, usui, nikko, shomaru, tsuchisaka, and nagao\n ").strip().lower()
        while goto != "akina" and goto != "akagi" and goto != "myogi" and goto != "usui" and goto != "nikko" and goto != "shomaru" and goto != "tsuchisaka" and goto != "nagao":
            goto = input("That's not a valid location, where would you like to go to?\n Your options are: akina, akagi, myogi, usui, nikko, shomaru, tsuchisaka, and nagao\n ").strip().lower()
        if goto == "akina":
            player, enemies = akina(player, cars, enemies)
        elif goto == "akagi":
            player, enemies = akagi(player, cars, enemies)
        elif goto == "myogi":
            player, enemies = myogi(player, cars, enemies)
        elif goto == "usui":
            player, enemies = usui(player, cars, enemies)
        elif goto == "nikko":
            player, enemies = nikko(player, cars, enemies)
        elif goto == "shomaru":
            player, enemies = shomaru(player, cars, enemies)
        elif goto == "tsuchisaka":
            player, enemies = tsuchisaka(player, cars, enemies)
        elif goto == "nagao":
            player, enemies = nagao(player, cars, enemies)
    print("Thank you for playing.")

print(f"These are your options for cars:")
for car in cars:
    print(f" {car}")
new_car = input("What car would you like? (make sure it's exactly the same) ").strip().lower()
while new_car not in cars:
    new_car = input("That was not a valid car, what car would you like? ").strip().lower()
print(f"You bought a(n) {new_car}")
player["car"] = new_car
main(player, cars, enemies)
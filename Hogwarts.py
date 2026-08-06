import time
import random
import json
import os

# Save and Quit
def save_and_quit(character):
    with open('save_game.json', 'w') as file:
        json.dump(character, file, indent=4)

# Load game

def load_game():
    if os.path.exists('save_game.json'):
        with open('save_game.json', 'r') as file:
            character = json.load(file)
        return character
    return None


#Sorting hat function
def sorting_hat(name):
    
    answers = []
    count ={'A':0, 'B':0, 'C':0, 'D':0}
    
    print('''\n✨ The Great Hall falls silent...

    🕯️ Hundreds of enchanted candles float above.

    👀 Every student turns to watch as an old,
    patched wizard's hat is placed upon your head.

    🎩 "Ahh..."

    🎩 "Another young mind..."

    🎩 "Let's see where you truly belong..."

    🎩 "Answer honestly."

    🎩 "Your heart knows the truth."\n
          ''')
    
    input(" ✨ Press ENTER to begin...\n")
    
    Q1 =input('''A troll is blocking the corridor. What do you do?
    A) Charge at it bravely — I'll fight it head on!
    B) Study its weaknesses first, then outsmart it
    C) Protect my friends and find another way around
    D) Use it to my advantage and make a deal with it\n
    
    Answer---> ''').upper().strip()
    time.sleep(2)

    print("🎩 Hmm...")
    time.sleep(3)

    Q2 =input('''What would you see in the Mirror of Erised?
    A) Yourself as the greatest hero the wizarding world has ever seen
    B) Yourself surrounded by ancient books and unsolved mysteries
    C) Yourself surrounded by all your friends, happy and safe
    D) Yourself powerful, respected and at the top of the wizarding world\n
    
    Answer---> ''').upper().strip()
    time.sleep(2)
    print("🎩 Curious...")
    time.sleep(3)


    Q3 =input('''You find a powerful spell that is forbidden. What do you do?
    A) Use it immediately — rules exist to be broken for a good cause!
    B) Research it thoroughly to understand it before deciding
    C) Report it to a teacher — some rules exist for good reason
    D) Keep it secret and use it only when it benefits you\n
    
    Answer---> ''').upper().strip()
    time.sleep(2)


    answers.append(Q1)
    answers.append(Q2)
    answers.append(Q3)

    # print(answers)

    for ans in answers:
        count[ans]+=1

    

    #print(count)

    maxi = max(count, key=count.get)

    #print(maxi)

    if max(count.values())>=2:
        if maxi=='A':
            print("🎩 I know exactly where you belong...")
            time.sleep(3)
            print("🦁 GRYFFINDOR! 🦁")
            return "GRYFFINDOR"
        elif maxi=='B':
            print("Interesting...")
            time.sleep(3)
            print("Ravenclaw 🦅")
            return "Ravenclaw"
        elif maxi=='C':
            print("Aahhhh...")
            time.sleep(3)
            print("Hufflepuff 🦡")
            return "Hufflepuff"
        elif maxi=='D':
            print("uh ohh...So...")
            time.sleep(3)
            print("It's Slytherin 🐍 ")
            return "Slytherin"

    else:
        

        Q4 =input('''\nThe Sorting Hat is confused! One final question...
        What do you value MOST above everything?
        A) Courage
        B) Knowledge  
        C) Loyalty
        D) Ambition\n
    
        Answer---> ''').upper().strip()

        answers.append(Q4)

        if Q4 =='A':
            time.sleep(3)
            print("🎩 I know exactly where you belong...")
            time.sleep(3)
            print("🦁 GRYFFINDOR! 🦁")
            return "GRYFFINDOR"
        elif Q4=='B':
            time.sleep(3)
            print("Interesting...")
            time.sleep(3)
            print("Ravenclaw 🦅")
            return "Ravenclaw"
        elif Q4=='C':
            print("Aahhhh...")
            time.sleep(3)
            
            print("Hufflepuff 🦡")
            return "Hufflepuff"
        else:
            print("uh ohh...So...")
            time.sleep(3)
            print("It's Slytherin 🐍 ")
            return "Slytherin"


# Explore Hogwarts

def explore_hogwarts(character):
    time.sleep(2)
    print('''\n 

    🕯️ The castle grows strangely quiet...
    Ancient portraits watch as you wander through forgotten corridors.
    Every door hides a new secret...
    ''')
    time.sleep(2)

    events = [
    {
        "message": "🌟 You find a Health Potion hidden behind a painting!",
        "type": "item",
        "value": "Health Potion"
    },
    {
        "message": "💰 You discover 5 gold coins on the floor!",
        "type": "gold",
        "value": 5
    },
    {
        "message": "👻 A ghost teaches you a new spell! +10 spell power",
        "type": "spell",
        "value": 10
    },
    {
        "message": "🕸️ Nothing interesting here... just cobwebs.",
        "type": "nothing",
        "value": 0
    },
    {
        "message": "⚡ You find an Elder Wand in an old chest!",
        "type": "item",
        "value": "Elder Wand"
    },
    {
        "message": "📖 You find a rare spell book! +15 spell power",
        "type": "spell",
        "value": 15
    },
    {
        "message": "💰 A lucky coin pouch! +10 gold",
        "type": "gold",
        "value": 10
    }
]

    print("\n🏰 You wander through the corridors of Hogwarts...")
    time.sleep(2)

    selected_event = random.choice(events)
    print(f"\n✨ {selected_event['message']}")
    time.sleep(2)

    if selected_event['type']=='item':
        character['inventory'].append(selected_event['value'])
        time.sleep(2)
        print(f"🎒 {selected_event['value']} added to inventory!")
    elif selected_event['type']=='gold':
        character['gold']+=selected_event['value']
        time.sleep(2)
        print(f"💰 Gold: {character['gold']}")
    elif selected_event['type']=='spell':
        character['spell_power']+=selected_event['value']
        time.sleep(2)
        print(f"✨ Spell Power: {character['spell_power']}")
    



    input("\nPress ENTER to return to menu...")


# Visits Diagon Valley

def visit_diagon_alley(character):
    print("✨ Magic fills the air...")

    time.sleep(2)

    shop = {
    "Health Potion":  {"price": 5,  "effect": "health",      "value": 30},
    "Spell Book":     {"price": 8,  "effect": "spell_power",  "value": 20},
    "Golden Cloak":   {"price": 15, "effect": "item",         "value": "Golden Cloak"},
                
    }

    while True:
        print(''' 🛍️  Welcome to Diagon Alley.
        What treasures will you take home today?''')

        time.sleep(1)

        print(f"\n your gold - {character['gold']}\n")
        time.sleep(2)


        

        

        for number, (item_name, details) in enumerate(shop.items(), start = 1):
            print(number, item_name, "-",  details['price'], "gold")

        print("4. Leave Shop")
        time.sleep(1)

        print('''\n🛒 Which item would you like to buy?
        Enter your choice (1-4):''')


        try:
            choice = int(input())
            found = False

            if choice == 4:
                print("👋 Thanks for visiting Diagon Alley!")
                break

            for number, (item_name, details) in enumerate(shop.items(), start = 1):
                
                
                if choice==number:
                    found = True
                    if character['gold']>=details['price']:
                        character['gold']-=details['price']
                        if details['effect'] == 'health':
                            character['health'] = min(100, character['health'] + details['value'])
                            print("❤️ You drink the potion. Strength flows through you!")
                            print(f"❤️ Health restored! Health: {character['health']}")
                            time.sleep(2)
                        elif details['effect'] == 'spell_power':
                            character['spell_power'] += details['value']
                            print("✨ Ancient magic courses through your wand!")
                            print(f"✨ Spell Power increased! Power: {character['spell_power']}")
                            time.sleep(2)
                        elif details['effect'] == 'item':
                            character['inventory'].append(item_name)
                            print(f"🎒 {item_name} added to inventory!")
                            time.sleep(2)
                        print(f'''
                        ✨ The shopkeeper nods approvingly.

                        "May it serve you well, young wizard."
                        ''')
                        time.sleep(1)
                        print(f" 💰 Remaining gold {character['gold']}")
                        break
                    else:
                        print("Not enough gold!")
                        break
                

            if not found:
                print("Not a valid Choice!")

        except ValueError:
            print("Please Enter valid number")


# Villain Generator

def villain_generator():
    villains = [
        {"name": "Dementor",    "health": 50,  "attack": 15},
        {"name": "Voldemort",   "health": 100, "attack": 30},
        {"name": "Basilisk",    "health": 70,  "attack": 20},
        {"name": "Death Eater", "health": 40,  "attack": 12},
        {"name": "Troll",       "health": 60,  "attack": 18},
    ]

    while True:
        yield random.choice(villains).copy()

villain_gen = villain_generator()

# Visit Forbidden Forest
def visit_forbidden_forest(character):
    time.sleep(2)
    print(f'''
    🌲 You stand before the entrance to the Forbidden Forest...

    The trees whisper secrets.
    An icy wind brushes past your robes.
    Even the bravest witches and wizards think twice before entering.''')

    time.sleep(2)

    print(f'''
    ⚠️ Danger lurks in every shadow.

    Do you wish to continue?

    1. 🌟 Enter the Forbidden Forest
    2. 🏰 Return to Hogwarts''')

   
    spells = ["⚡ Expelliarmus", "💫 Stupefy", "🌟 Expecto Patronum", "🔥 Incendio"]


    try:
        choice = int(input())
        found = False
        if choice==1:
            found = True
            villain = next(villain_gen)
            print("🌲 You slowly walk toward the edge of the Forbidden Forest...")
            time.sleep(4)
            print(f"⚠️ {villain['name']} appears from the shadows!")
            time.sleep(2)

            while character['health']>0 and villain['health']>0:
                time.sleep(2)
                print(f"\n ❤️ Your Health: {character['health'] } | ☠️  {villain['name']} Health : {villain['health']}")

                for i, spell in enumerate(spells, start = 1):
                    print(f"{i} - {spell}")
                print("\n Choose your Spell")

                try:
                    spell_choice = int(input("\n Cast Spell (1-4):"))
                    if 1<=spell_choice<=4:
                        villain_damage = random.randint(character['spell_power']//2, character['spell_power'])
                        time.sleep(2)
                        print(f'''✨ You cast {spells[spell_choice-1]}!
                        💥 You dealt {villain_damage} damage!''')
                        time.sleep(2)
                        villain['health']-=villain_damage
                        print(f"☠️  {villain['name']} has {max(0, villain['health'])} health remaining.")

                        if villain['health']>0:
                            player_damage = random.randint(villain['attack']//2, villain['attack'])
                            time.sleep(2)
                            print(f"💀 {villain['name']} strikes back! You take {player_damage} damage!")
                            time.sleep(2)
                            character['health']-=player_damage
                            if character['health']<=0:
                                break
                    else:
                        print("Invalid Spell Choice")

                    
                except ValueError:
                    print("Please Enter a valid number")

            if character['health']>0:
                gold_won = random.randint(5, 20)
                character['gold']+=gold_won
                time.sleep(4)
                print(f"\n🏆 Victory! You defeated the {villain['name']}!")
                character["villains_defeated"] += 1
                print(f"💰 You earned {gold_won} gold! Total gold: {character['gold']}")
                print(f"Villains defeated: {character['villains_defeated']}")

                loot = random.choice([
                "Phoenix Feather",
                "Dragon Scale",
                "Crystal Orb",
                "Ancient Rune"
                ])

                character["inventory"].append(loot)

                print(f"🎁 You found: {loot}")

                if character["villains_defeated"] >= 5:
                    print(f"""

                    ✨✨✨ CONGRATULATIONS! ✨✨✨

                    You have defeated five dark creatures.

                    The Headmaster awards you
                    "The Order of Merlin"

                    🏆 You have become
                    Hero of Hogwarts!

                    Thank you for playing.
                    """)
                    exit()

            else:
                time.sleep(4)

                print(f"\n💀 You were defeated by the {villain['name']}...")
                print("🏥 Madam Pomfrey heals you back to 30 health.")
                character['health'] = 30

            input("\n Press ENTER to return to main menu...")

        if choice==2:
            found = True
            return
        if not found:
            print("Please enter a valid choice")
    except ValueError:
        print("Please Enter a Valid Choice")







# View Stats
def view_stats(character):
    inventory_text = ""
    if len(character['inventory'])==0:
        inventory_text = "Empty"
    else:
        inventory_text = ",".join(character['inventory'])
    
    
    print("\n⚡Your Wizard Profile⚡")
    print(f"""
          🧙 Name       : {character['name']}\n
          🏰 House      : {character['house']}\n
          ❤️ Health     : {character['health']}\n
          ✨ Spell Power : {character['spell_power']}\n
          💰 Gold        : {character['gold']}\n
          🎒 Inventory   : {inventory_text}\n
          ⚔️ Villains Defeated : {character['villains_defeated']}
          """)
    time.sleep(2)
    input("Press ENTER to return")
    time.sleep(2)







def main_menu(character):
    print(f"\nWelcome to Hogwarts, {character['name']} of {character['house']}!")

    

    while True:

        try:

            choice = int(input('''\nWhat would you like to do?
            
                1. 🏰 Explore Hogwarts
                2. 🛒 Visit Diagon Alley
                3. 🌲 Enter Forbidden Forest
                4. 📊 View your stats
                5. 💾 Save and Quit
            
                Enter your choice (1-5):''' ))
            
            if(choice==1):
                print("Lets 🏰 Explore Hogwarts ")
                explore_hogwarts(character)
                
            elif(choice==2):
                print("Let's 🛒 Visit Diagon Alley ")
                visit_diagon_alley(character)
                
            elif(choice==3):
                
                visit_forbidden_forest(character)
                
            elif(choice==4):
                
                view_stats(character)
                
            elif(choice==5):
                save_and_quit(character)
                print("\n💾 Game Saved Successfully!")
                print("👋 Goodbye from Hogwarts!")
                time.sleep(2)
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Please enter number between 1 and 5")
            time.sleep(3)






saved = load_game()

if saved:
    cont = input("💾 Saved game found! Continue? (Y/N): ").upper().strip()

    if cont=='Y':
        character = saved
        main_menu(character)
        exit()



# Starting of game --> Welcome message
print('''\n🪄✨ Magic cannot begin
until your name is known...\n''')

name = input("📜 Enter your name:\n")

print(f"Welcome, {name}!\n The castle has been expecting you. ")


house =sorting_hat(name)
# print(house)

character = {
    "name": name,
    "house": house, 
    "health":100,
    "spell_power": 50,
    "gold": 10,
    "inventory":[],
    "villains_defeated": 0
}

# print(character)


main_menu(character)

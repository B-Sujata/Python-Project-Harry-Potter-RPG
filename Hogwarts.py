import time


print('''\n🪄✨ Magic cannot begin
until your name is known...\n''')

name = input("📜 Enter your name:\n")

print(f"Welcome, {name}!\n The castle has been expecting you. ")


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

house =sorting_hat(name)
# print(house)

character = {
    "name": name,
    "house": house, 
    "health":100,
    "spell_power": 50,
    "gold": 10,
    "inventory":[]
}

# print(character)

def view_stats(character):
    inventory_text = ""
    if len(character['inventory'])==0:
        inventory_text = "Empty"
    else:
        inventory_text = ",".join(character['inventory'])
    
    
    print("\n⚡Your Wizard Profile⚡")
    print(f"""
          🧙 Name       : {character['name']}
          🏰 House      : {character['house']}
          ❤️ Health     : {character['health']}
          ✨ Spell Power : {character['spell_power']}
          💰 Gold        : {character['gold']}
          🎒 Inventory   : {inventory_text}
          """)
    time.sleep(2)
    input("Press Enter to return")
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
                
            elif(choice==2):
                print("Let's 🛒 Visit Diagon Alley ")
                
            elif(choice==3):
                print("Let's 🌲 Enter Forbidden Forest")
                
            elif(choice==4):
                
                view_stats(character)
                
            elif(choice==5):
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Please enter number between 1 and 5")
            time.sleep(3)

main_menu(character)




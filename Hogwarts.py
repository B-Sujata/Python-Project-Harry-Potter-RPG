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

print(character)
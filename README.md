# 🧙‍♀️ Hogwarts: Your Story — A Harry Potter Text RPG

A fully interactive Harry Potter themed text adventure game built in Python.
You are the hero. Your choices shape the story.

---

## 🎮 How to Play

```bash
python Hogwarts.py
```

No external libraries needed — only Python standard library!

---

## ✨ Features

- 🎩 **Sorting Hat Quiz** — Answer 3 questions to discover your Hogwarts house (Gryffindor, Ravenclaw, Hufflepuff, or Slytherin). Tiebreaker included!
- 🏰 **Explore Hogwarts** — Wander the castle corridors and discover random treasures, gold, and spell power boosts
- 🛒 **Diagon Alley Shop** — Buy Health Potions, Spell Books, and rare items using gold
- 🌲 **Forbidden Forest Battles** — Fight 5 different dark creatures using 4 spells. Random damage system makes every battle unique
- 🏆 **Win Condition** — Defeat 5 villains to earn the Order of Merlin and become Hero of Hogwarts
- 💾 **Save & Load System** — Your progress is saved to a JSON file and loaded automatically next time
- 📊 **View Stats** — Track your health, spell power, gold, inventory, and villains defeated

---

## 🗺️ Game Structure

Start Game
↓
Load saved game? (Y/N)
↓
Enter your name
↓
Sorting Hat Quiz → House assigned
↓
Main Menu
├── 1. Explore Hogwarts → Random event (item/gold/spell power)
├── 2. Diagon Alley → Buy items with gold
├── 3. Forbidden Forest → Battle villain, earn gold + loot
├── 4. View Stats → See all character stats
└── 5. Save & Quit → Save to file, exit game

Win: Defeat 5 villains → Order of Merlin 🏆

---

## 🐍 Python Concepts Used

Built this project to practice and apply core Python concepts:

- **Data types** — strings, integers, booleans
- **Collections** — lists, dictionaries, nested dictionaries
- **Control flow** — if/elif/else, while loops, for loops
- **Functions** — parameters, return values, modular design
- **Exception handling** — try/except for all user inputs
- **Modules** — time, random, json, os
- **File handling** — save/load game using JSON
- **Generators** — `villain_generator()` using `yield`
- **String methods** — .upper(), .strip(), .join()
- **Built-ins** — enumerate(), min(), max(), random.choice(), random.randint()

---

## 📁 Project Structure
Harry Potter/
└── Hogwarts.py # Complete game — ~600 lines

---

## 💡 What I Learned

Built this project from scratch while learning Python fundamentals.
The hardest parts were:
- Implementing the generator for infinite villain spawning
- Designing the save/load system with JSON file handling
- Building the battle loop with proper health tracking for both player and villain

The most fun part was the Sorting Hat quiz — designing questions that actually map to the four Hogwarts houses!

---

## 🚀 Future Improvements

- [ ] Separate into modules (character.py, battle.py, shop.py)
- [ ] Add OOP — Character class with methods
- [ ] Use inventory items (Health Potion) during battle
- [ ] Add screen clearing between scenes
- [ ] Add more villains, spells, and locations

---

## 👩‍💻 Author

**Sujata Bhadke** — B.Tech IT, VIIT Pune
Part of my 6-month ML Engineer learning journey.

[GitHub](https://github.com/B-Sujata) | [LinkedIn](https://www.linkedin.com/in/sujata-bhadke-70a2342ba/)

---

*"It is our choices that show what we truly are, far more than our abilities." — Albus Dumbledore*

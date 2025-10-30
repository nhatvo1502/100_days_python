# capitals = {
#    "Frances": "Paris",
#    "Germany": "Berlin"
# }

# travel_log = {
#    "France" : ["Paris", "Lille", "Digon"],
#    "Germany": ["Stuttgart", "Berlini"]
# }

# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

# travel_log = {
#    "France": {
#       "cities_visited": ["Paris", "Lille", "Dijon"],
#       "total_visits": 12
#    },
#    "Germany": {
#       "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#       "total_visited": 5
#    }
# }
# print(travel_log["Germany"]["cities_visited"][2])

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
# print(dict)
# dict[1]=4
# print(dict)

# name = 'Khoa Hoang'

# for n in name:
#    print(n)
#    if n in 'Nhat':
#       print('yes')
#    else:
#       print('no')

# def calculate_love_score(name1, name2):
#     word = 'true'
#     word2 = 'love'
#     name = name1+name2
#     name = name.lower()
#     total1 = 0
#     total2 = 0
    
#     for w in word:
#         if w in name:
#             count = 0
#             for c in name:
#                 if w==c:
#                     count+=1
#                     total1+=1
#             print(f"{w.upper()} occurs {count} times")
#         else:
#             print (f"{w.upper()} occurs 0 times")
#     print(f"Total={total1}")
    
#     for w in word2:
#         if w in name:
#             count = 0
#             for c in name:
#                 if w==c:
#                     count+=1
#                     total2+=1
#             print(f"{w.upper()} occurs {count} times")
#         else:
#             print (f"{w.upper()} occurs 0 times")
#     print(f"Total={total2}")
    
#     result = total1*10 + total2
#     print(f"Love Score={result}")
    
#     return result

# calculate_love_score("Kanye West", "Kim Kardashian")

# astring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# print(astring.find('G'))
# print(astring[9])
# print(list(astring.lower()))

# year = 2000
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False
# print(is_leap_year(year))

# deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'K']
# newDeck = []
# for card in range(len(deck)):
#     newDeck.append(str(deck[card]))
# print(newDeck)

# cards = [1, 2, 3, 10, 11, 13, 14, 11]
# bcards = []

# def reset_deck():
#     global cards, bcards
#     bcards = cards.copy()

# reset_deck()

# print(cards)
# print(bcards)

# print(cards)
# print(cards.count(11))
# print(len(cards))
# for i in range(len(cards)):
#     print(cards[i])
#     if cards[i] == 11:
#         print('found it')
#         cards[i] = 100

# print(cards)

# print(73%1)
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
# fizz_buzz(89)
# import random
# person_pool = {
#     1: "Camila Cabello, a Musician, from Cuba.",
#     2: "Chris Hemsworth, an Actor, from Australia.",
#     3: "Shakira, a Musician, from Colombia.",
#     4: "Zendaya, an Actress, from United States.",
#     5: "Jungkook, a Musician, from South Korea.",
#     6: "Lionel Messi, an Athlete, from Argentina.",
#     7: "Emma Watson, an Actress, from United Kingdom.",
#     8: "Keanu Reeves, an Actor, from Canada.",
#     9: "Rihanna, a Musician, from Barbados.",
#     10: "Lupita Nyong'o, an Actress, from Kenya."
# }

# print(random.choice(person_pool))
# menu = {
#    "espresso" : {
#       "water": 50,
#       "coffee": 18,
#       "milk": 0,
#       "price": 1.50
#    },
#    "latte": {
#       "water": 200,
#       "coffee": 24,
#       "milk": 150,
#       "price": 2.50
#    },
#    "cappuccino": {
#       "water": 250,
#       "coffee": 24,
#       "milk": 100,
#       "price": 3.00
#    }
# }

# order = {
#    "drink": "",
#    "pay": {
#       "quaters": 0,
#       "nickles": 0,
#       "dimes": 0,
#       "pennies": 0
#    }
# }

# print(menu["espresso"])
# for i in menu:
#    print(f"{i} {menu[i]['price']}")

# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# print(timmy)
# while True:
#     timmy.forward(50)
#     timmy.left(25)

# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)

# from prettytable import PrettyTable
# table = PrettyTable()
# pokemon_list = [
#     ["Pikachu", "Electric"],
#     ["Charizard", "Fire/Flying"],
#     ["Bulbasaur", "Grass/Poison"],
#     ["Squirtle", "Water"],
#     ["Jigglypuff", "Normal/Fairy"],
#     ["Gengar", "Ghost/Poison"],
#     ["Eevee", "Normal"],
#     ["Snorlax", "Normal"],
#     ["Dragonite", "Dragon/Flying"],
#     ["Mewtwo", "Psychic"]
# ]

# # pokemon_name = []
# # pokeon_type = []
# # for i in range(len(data)):
# #     pokemon_name.append(data[i][0])
# #     pokeon_type.append(data[i][1])

# # table.add_column('Name', pokemon_name)
# # table.add_column('Type', pokeon_type)

# for i in range(len(pokemon_list)):
#     row = []
#     for c in range(len(pokemon_list[i])):
#         row.append(pokemon_list[i][c])
#     table.add_row(row)

# table.align = "l"
# print(table)

# true_variants = ["True", "true", "T", "t"]

# answer = "False"

# if answer in true_variants:
#    print("yes")
# else:
#    print("no")

# import requests
# r = requests.get("https://opentdb.com/api.php?amount=20&difficulty=easy&type=boolean")
# r = r.json()
# question_list = []
# print(r["results"])
# for i in r["results"]:
#     print(i["question"])
#     print(i["correct_answer"])

# aString = "&quot;QWEASDZXC"
# aString = aString.replace("&quot;", '"')
# print(aString)

# from tkinter import messagebox, Tk
# import random

# # root = Tk()
# # root.withdraw()
# # messagebox.showinfo("Race Result", f"Nhat wins the race! 🏁")
# # root.destroy()

# colors = ['red', 'blue', 'green']
# random.shuffle(colors)
# print(colors)

aList = ["hello", "bello", "world"]
print(aList[1:])
print(aList)

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
    
#     def breathe(self):
#         print("Inhale, exhale")

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

#     def breathe(self):
#         super().breathe()
#         print("doing this underwater")

#     def swim(self):
#         print("moving in water")

# nemo = Fish()
# nemo.swim()
# nemo.breathe()
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

astring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(astring.find('G'))
print(astring[9])
print(list(astring.lower()))
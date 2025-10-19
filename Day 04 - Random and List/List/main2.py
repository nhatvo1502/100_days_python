fruits = "Strawberries, Nectarines, Apples, Grapes, Peaches, Cherries, Pears"
print(fruits)
fruits = fruits.split(", ")
print(fruits)
vegetables = "Spinach, Kale, Tomatoes, Celery, Potatoes"
print(vegetables)
vegetables = vegetables.split(", ")
print(vegetables)

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)


print(dirty_dozen[1][1])
dirty_dozen.append(['Banana'])
print(dirty_dozen)
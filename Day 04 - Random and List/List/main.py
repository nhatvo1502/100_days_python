states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
                     "Connecticut", "Massachusetts", "Maryland", 
                     "South Carolina", "New Hampshire", "Virginia", 
                     "New York", "North Carolina", "Rhode Island", 
                     "Vermont", "Kentucky", "Tennessee", "Ohio", 
                     "Louisiana", "Indiana", "Mississippi", "Illinois", 
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", 
                     "Minnesota", "Oregon", "Kansas", "West Virginia", 
                     "Nevada", "Nebraska", "Colorado", "North Dakota", 
                     "South Dakota", "Montana", "Washington", "Idaho", 
                     "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
                     "Alaska", "Hawaii"]

a = states_of_america.count("California")
print(a)

fruits = "Strawberries, Nectarines, Apples, Grapes, Peaches, Cherries, Pears"
fruits = fruits.split(", ")
vegetables = "Spinach, Kale, Tomatoes, Celery, Potatoes"
vegetables = vegetables.split(", ")

dirty_dozen = [fruits, vegetables]


print(dirty_dozen[1][1])
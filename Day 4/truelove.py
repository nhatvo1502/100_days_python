print("Welcome to the Love Caluculator!")
# name1 = input("What is their name? \n")
# name2 = input("What is their name? \n")

# name1_lower = name1.lower()
# name2_lower = name2.lower()
name1_lower = "Brad Pitt"
name2_lower = "Jennifer Aniston"

#TRUE
letterT = "true"
num = 0
for i in letterT:
    num += name1_lower.count(i) + name2_lower.count(i)
    print(i)
    print(num)
num = num*10

letterT = "love"
for i in letterT:
    num += name1_lower.count(i) + name2_lower.count(i)
    print(i)
    print(num)

print(num)

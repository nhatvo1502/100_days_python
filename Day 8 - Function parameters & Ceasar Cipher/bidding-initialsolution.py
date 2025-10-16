print("Welcome to bidder")

dict = {}
while True:
    user_name = input("What is your name?: ")
    user_bid = float(input("What is your bid?: $ "))
    dict.update({user_name: user_bid})
    newBidder = input("Are there any other bidders? Type 'yes or no'.\n")
    if newBidder == 'no':
        break

highest_bidder = max(dict, key=dict.get)
highest_bid = dict[highest_bidder]
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
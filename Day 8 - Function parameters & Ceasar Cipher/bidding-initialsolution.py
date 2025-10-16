import os
# import sys

# # Support Functions
# def clear_console():
#     """Clears the console screen based on the operating system."""
#     if sys.platform.startswith('win'):
#         # For Windows
#         os.system('cls')
#     else:
#         # For Linux, macOS, and other Unix-like systems
#         os.system('clear')

# Program

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to bidder")

dict = {}
while True:
    user_name = input("What is your name?: ")
    user_bid = float(input("What is your bid?: $ "))
    dict.update({user_name: user_bid})
    newBidder = input("Are there any other bidders? Type 'yes or no'.\n")
    os.system('cls')
    if newBidder == 'no':
        break

def find_highest_bidder_max(dict):
    highest_bidder = max(dict, key=dict.get)
    highest_bid = dict[highest_bidder]
    return highest_bidder, highest_bid

def find_highest_bidder_loop(dict):
    highest_bidder = ''
    highest_bid = 0
    for bidder in dict:
        if highest_bid < dict[bidder]:
            highest_bid = dict[bidder]
            highest_bidder = bidder
    return highest_bidder, highest_bid

bidder, bid = find_highest_bidder_loop(dict)
print(f"The winner is {bidder} with a bid of ${bid}")
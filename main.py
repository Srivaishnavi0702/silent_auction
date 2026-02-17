# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
#importing the logo
from art import logo
print(logo)
#user input
auction = {}
while True:
    bidder_name = input("What is your name? ")
    bid_cost = float(input("What is your bid cost? $"))
    auction[f"{bidder_name}"] = bid_cost
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if next_bidder == "no":
        break
    print("\n" * 100)
#Calculate the highest bid
winner = ""
winner_cost = 0
for key in auction:
    if auction[key] > winner_cost:
        winner_cost = auction[key]
        winner = key
#Displays the winner
print(f"The winner is {winner} with a bid of ${winner_cost}")

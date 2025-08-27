import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#HINT: You can call clear() to clear the output in the console.

from art import logo
#HINT: You print(logo)


#TODO: function to print the winner
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    clear()
    print(logo)
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bidding_finished = False
while not bidding_finished:
    #TODO: print logo
    print(logo)
    #TODO: Ask for name and bid 
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    #TODO: Add them to Dict
    bids = {}
    bids[name] = price
    #TODO: Ask for another name and bid clear console if yes and ask again , find max bid if no
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

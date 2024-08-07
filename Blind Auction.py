from logo import logo
print(logo)

def find_highest_bidder(bidding_dic):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dic:
        bid_amount = bidding_dic[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bid_offer = {}
flag = True
while flag:
    print(logo)
    name = str(input("What is you name?\n"))
    bid = int(input("How much do you want to bid?\n"))

    
    bid_offer[name] = bid
    choice = str(input("If someone else is bidding, type 'yes'. If not type 'no'\n")).lower()
    
    #checking if program should continue
    if choice == 'no':
        flag = False
        find_highest_bidder(bid_offer)
    elif choice == 'yes':
        print("\n" * 100)





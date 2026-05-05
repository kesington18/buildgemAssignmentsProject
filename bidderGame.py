bidders = {}

'''def bidding(name, bids):
    bidders[name] = bids
    print("\n" * 100)
    # print(bidders)

continueBidding = True
while continueBidding:
    nameOfUser = input("Enter your name?: ").lower()
    biddingPrice = int(input("Enter your bidding price: $"))
    continueBiddingQuestion = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    bidding(name=nameOfUser, bids=biddingPrice)

    if continueBiddingQuestion == "no":
        continueBidding = False
        maxValue = float('-inf')
        maxName = None
        for name, bids in bidders.items():
            if bids > maxValue:
                maxValue = bids
                maxName = name

        print(f"The winner is {maxName} with a bidding price of ${maxValue}")'''

# Angela Yu Solution
def bidding(bids):
    '''winner = ""
    highest = 0
    for bidder in bids:
        bidAmount = bids[bidder]
        if bidAmount > highest:
            highest = bidAmount
            winner = bidder'''

    winner = max(bids, key=bids.get)
    result = bids[winner]

    print(f"The winner is {winner} with a bidding price of ${result}")



continueBidding = True
while continueBidding:
    nameOfUser = input("Enter your name?: ").lower()
    biddingPrice = int(input("Enter your bidding price: $"))
    bidders[nameOfUser] = biddingPrice
    continueBiddingQuestion = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if continueBiddingQuestion == "no":
        continueBidding = False
        bidding(bidders)
    elif continueBiddingQuestion == "yes":
        print("\n" * 20)



bidders = {}

def bidding(name, bids):
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

        print(f"The winner is {maxName} with a bidding price of ${maxValue}")
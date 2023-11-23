# Project

from logo import logo

print(logo)


bids = {}
end_bidding = False


def find_highest_bidder(bid_record):
    max_bid = 0.0
    bid_winner = ""
    for bidder in bid_record:
        # print(bidder["bid_value"])
        if bid_record[bidder] >= max_bid:
            max_bid = bid_record[bidder]
            bid_winner = bidder
    return {"name": bid_winner, "bid_value": max_bid}


while not end_bidding:
    name = input("Your name: ")
    bid_value = float(input("What is your bid? $"))
    bids[name] = bid_value
    bidding_continue = input("Are there any other biders? Type 'yes' or 'no': ")
    if bidding_continue == "no":
        end_bidding = True

winner = find_highest_bidder(bids)
print(winner)

print(
    f"The winner of the bidding is {winner['name']} with a bid of {winner['bid_value']}"
)

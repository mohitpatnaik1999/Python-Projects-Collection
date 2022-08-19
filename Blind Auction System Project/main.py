from replit import clear
from art import logo
print(logo)
print("Welcome to Blind Auction System")
records={}

def highest_bidder(records):
  highest_amount=0
  for bidder_name in records:
    if records[bidder_name]>highest_amount:
      highest_amount=records[bidder_name]
      winner=bidder_name
  clear()
  print(f"The winner is {winner} with a bid of ${highest_amount}")
  
end_of_loop=True
while end_of_loop:
  name=input("What is your name?: ")
  bid_price=int(input("What\'s your bid?: $"))
  records[name]=bid_price
  choice=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  if choice=="yes":
    clear()
  elif choice=="no":
    end_of_loop=False
    highest_bidder(records)
    

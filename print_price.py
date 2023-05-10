import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser(description="Calculate the price of a photographic print")
parser.add_argument("size", type=float, help="The size of the print in inches")
parser.add_argument("edition_size", type=int, help="The size of the limited edition")
parser.add_argument("reputation_factor", type=float, help="The reputation factor of the photographer")
parser.add_argument("production_cost", type=float, help="The production cost of the print in dollars")
parser.add_argument("framing_cost", type=float, help="The framing cost of the print in dollars")
parser.add_argument("subject_value", type=float, help="The subject value multiplier")
args = parser.parse_args()

# Calculate the price of the print using the modified formula
price = ((args.size * args.size) / 144) * (1 + (0.1 * (args.size - 10))) * (1 + (0.2 * (args.edition_size - 1)))
price *= args.subject_value * args.reputation_factor
price += args.production_cost + args.framing_cost

# Print the calculated price
print("${:.2f}".format(price))

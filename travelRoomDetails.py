import json

# Load the JSON file
with open(r"Python-task.json", 'r') as f:
    hotel_data = json.load(f)

# Get the room details and taxes
room_prices = hotel_data['assignment_results'][0]['shown_price']
net_prices = hotel_data['assignment_results'][0]['net_price']
number_of_guests = hotel_data['assignment_results'][0]['number_of_guests']
taxes = json.loads(hotel_data['assignment_results'][0]['ext_data']['taxes'])

# Find the cheapest room function
cheapest_room_type = None
# Any real number compared with float('inf') will be smaller (except inf itself).
cheapest_price = float('inf')

for room, price in room_prices.items():
    if float(price) < cheapest_price:
        cheapest_price = float(price)
        cheapest_room_type = room

# Calculate the total price (net price + taxes) for all rooms
total_prices = []
for room, net_price in net_prices.items():
    total_price = float(net_price) + float(taxes['TAX']) + float(taxes['City tax'])
    total_prices.append(f"{room}: Total Price = ${total_price:.2f}")

# Output the results to a file
with open('hotel_pricing_output_simple.txt', 'w') as f:
    # Write cheapest room details
    f.write(f"Cheapest Room Type: {cheapest_room_type}\n")
    f.write(f"Cheapest Price: ${cheapest_price}\n")
    f.write(f"Number of Guests: {number_of_guests}\n\n")

    # Write total prices for all rooms
    f.write("Total Prices (Net Price + Taxes) for all rooms:\n")
    for total in total_prices:
        f.write(total + '\n')

print("Done")

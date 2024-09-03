# Determines the shipping cost based on the ship_to_state.
# When testing, change the ship_to_state to various state abreviations
# to verify your code works for all conditions.
# Vernice Tanquerido
ship_to_state = input(
    "Enter a state to ship to, e.g TX, NM, OK, NY, AK, HI, etc.:")
if ship_to_state.upper() == "TX" or ship_to_state.upper() == "NM" or ship_to_state.upper() == "OK":
    shipping_cost = 0
elif ship_to_state.upper() == "NY":
    shipping_cost = 7
elif ship_to_state.upper() == "AK":
    shipping_cost = 15.75
elif ship_to_state.upper() == "HI":
    shipping_cost = 20
else:
    shipping_cost = 12.5
print(f"Shipping to {ship_to_state.upper()} costs {shipping_cost}")

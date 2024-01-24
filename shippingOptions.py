""" 
Ground Shipping
Weight of Package Price per Pound Flat Charge

2 lb or less $1.50 $20.00
Over 2 lb but less than or equal to 6 lb $3.00 $20.00
Over 6 lb but less than or equal to 10 lb $4.00 $20.00
Over 10 lb $4.75 $20.00

Ground Shipping Premium
Flat charge: $125.00


Weight of Package Price per Pound Flat Charge

2 lb or less $4.50 $0.00
Over 2 lb but less than or equal to 6 lb $9.00 $0.00
Over 6 lb but less than or equal to 10 lb $12.00 $0.00
Over 10 lb $14.25 $0.00
"""





def shipping_cost_ground(weight):

  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <=10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75

  return 20 + (price_per_pound * weight)

print(shipping_cost_ground(8.4))

shipping_cost_premium = 125.00

def shipping_cost_drone(weight):

  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <=10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25

  return price_per_pound * weight
print(shipping_cost_drone(1.5))

def print_cheapest_shipping_method(weight):
  
  ground = shipping_cost_ground(weight)
  premium = shipping_cost_premium
  drone = shipping_cost_drone(weight)

  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone

  print(
    "The cheapest option available is $%.2f with %s shipping."
    % (cost, method)
    )

print_cheapest_shipping_method(4.8)
print_cheapest_shipping_method(41.5)

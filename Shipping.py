#defining weight variable
weight = 41.5
#Cost of ground shipping
if weight <= 2.0:
  cost = (1.50 * weight) + 20.0
elif weight <= 6.0:
  cost = (3.00 * weight) + 20.0
elif weight <= 10.0:
  cost = (4.00 * weight) + 20.0
else:
  cost = (4.75 * weight) + 20.0
print("Cost of ground shipping:", cost)
#Cost of premium ground shipping
Ground_shipping_premium = 125
print("Cost of premium ground shipping:", Ground_shipping_premium)
#Cost of drone shipping
if weight <= 2.0:
  cost = (4.50 * weight)
elif weight <= 6.0:
  cost = (9.00 * weight)
elif weight <= 10.0:
  cost = (12.00 * weight)
else:
  cost = (14.25 * weight)
print ("Cost of drone shipping", cost)
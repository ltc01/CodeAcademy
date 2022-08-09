#sal's shipping 🚚

weight = 41.5

#Ground shipping
if weight <= 2:
  cost =weight*1.50+20
elif weight<=6:
  cost=weight*3.00+20
elif weight<=10:
  cost=weight*4.00+20
else:
  cost=weight*4.75+20
print("Ground shipping: $" +str(cost))

#Premium ground shipping
cost_ground_shipping=125.00

print("Ground Shipping Premium: $"+str(cost_ground_shipping))

#drone shipping
if weight <= 2:
  cost_droneShipping =weight*4.50
elif weight<=6:
  cost_droneShipping =weight*9.00
elif weight<=10:
  cost_droneShipping =weight*12.00
else:
  cost_droneShipping =weight*14.25
print("Drone shipping cost: $" +str(cost_droneShipping ))

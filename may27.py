#Task 1 : there are few order id's in a list check whether the order id even or odd
# order_id = [101, 102, 103, 104, 105]
# for id in order_id:
#     if id % 2 == 0:
#         print(f"Order ID {id} is even.")
#     else:
#         print(f"Order ID {id} is odd.")

# order_id = [101, 102, 103, 104, 105]
# for id in order_id:
#     print(f"Processing order ID: {id}")

#Task 2 : 

units = float(input("Enter Number of electricity units :"))
price_per_unit = 8.0
total_cost = units * price_per_unit
total_bill = 0

if units >=300:
    total_bill = total_cost+500
else:
    total_bill = total_cost+100
print(f"Your electricity bill is {total_bill}")
gst_amount = total_bill * 0.18
final_bill = total_bill + gst_amount
print(f"Your electricity bill with GST is {final_bill}")
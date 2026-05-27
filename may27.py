#Task 1 : there are few order id's in a list check whether the order id even or odd
# order_id = [101, 102, 103, 104, 105]
# for id in order_id:
#     if id % 2 == 0:
#         print(f"Order ID {id} is even.")
#     else:
#         print(f"Order ID {id} is odd.")

#Task 2 : 

electricity = int(input("Enter Number of electricity units :"))
if electricity >=300:
    extra_surcharge = 500
    print(f"Your electricity bill is {electricity*8 + extra_surcharge}")
elif electricity >= 200:
    surcharge = 100
    print(f"Your electricity bill is {electricity*8 + surcharge}")
elif electricity >= 100:
    gst = (electricity*8 + surcharge) * 0.18
    print(f"Your electricity bill with GST is {electricity*8 + surcharge + gst}")
else:
    print(f"Your electricity bill is {electricity*8}")


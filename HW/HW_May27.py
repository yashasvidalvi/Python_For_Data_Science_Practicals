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

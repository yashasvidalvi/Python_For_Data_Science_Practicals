print("===== Smart Electricity Bill Generator =====")
units = int(input("Enter number of electricity units: "))

if units >= 0 and units <= 50:
    bill = 0
    print("No bill for units between 0 to 50")
elif units >= 51 and units <= 100:
    bill = units * 5
    print("Rate applied: Rs 5 per unit")
else:
    bill = units * 8
    print("Rate applied: Rs 8 per unit")

if units >= 300:
    surcharge = 500
    print("Extra surcharge applied: Rs 500")
else:
    surcharge = 100
    print("Surcharge applied: Rs 100")

bill = bill + surcharge
gst = bill * 0.18
total_bill = bill + gst

print("===== BILL DETAILS =====")
print("Units Consumed :", units)
print("Bill Amount : Rs", bill)
print("GST (18%) : Rs", gst)
print("Total Bill : Rs", total_bill)
print("="*24)

mrp = eval(input("Enter the MRP of the product: "))

discount = eval(input("Enter the discount percentage: "))

selling_price = mrp - (mrp * discount / 100)

print("--- Selling Price Calculation ---")
print("MRP: Rs. " + str(mrp))
print("Discount: " + str(discount) + "%")
print("Selling Price: Rs. " + str(selling_price))

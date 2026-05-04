mrp = float(input("Enter the MRP of the product: "))

discount = float(input("Enter the discount percentage: "))

selling_price = mrp - (mrp * discount / 100)

print("\n--- Selling Price Calculation ---")
print(f"MRP: Rs. {mrp}")
print(f"Discount: {discount}%")
print(f"Selling Price: Rs. {selling_price}")

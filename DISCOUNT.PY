def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    else:
        return price


price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if final_price != price:
    print("Discount applied! Final price:", round(final_price, 2))
else:
    print("No discount applied. Price remains:", round(price, 2))
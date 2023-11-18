total_cost = 0
while True:
    price_input = input("nhap tien")
    
    
    if price_input == "":
        break

    
    try:
        price = float(price_input)
        total_cost += price
    except ValueError:
        print("")


pennies_due = total_cost * 100
remainder = pennies_due % 5


if remainder < 2.5:
    adjusted_total = pennies_due - remainder
else:
    adjusted_total = pennies_due + (5 - remainder)


adjusted_dollars = adjusted_total / 100


print(f"\nTotal cost: ${total_cost:.2f}")
print(f"Amount due for cash payment: ${adjusted_dollars:.2f}")
prices=[4.95, 9.95, 14.95, 19.95, 24.95]
discount=0.6

print("Original Price  |  Discount Amount  |  New Price")
print("------------------------------------------")

for i in prices:
    discount_amount=i*discount
    new_price=i-discount_amount

    print(f"${i:.2f}         |  ${discount_amount:.2f}          |  ${new_price:.2f}")

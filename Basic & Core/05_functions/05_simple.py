def add_vat(price, var_rate):
    return price * (100 + var_rate)/100

orders = [100, 150, 200]
for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")

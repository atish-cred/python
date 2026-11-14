users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

# Below is tuple
# dictionary
discounts = {
    "P20": (0.2, 0), # 20% discount
    "F10": (0.5, 0), # 50% discount
    "P50": (0, 10),  # 10 rupees flat/fixed discount
}


for user in users:
    # user will have whole object --> object will have coupon value
    # coupon value is a key into the discount
    # (0, 0) is default value if nothing is found
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount {discount}")



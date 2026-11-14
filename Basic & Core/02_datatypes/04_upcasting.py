# Upcasting
is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total Actions {total_actions}") # 6. because true consider as 1 and it will ad into 5
print(f"-------------------------\n")

milk_present = 0        # False - no milk
milk_present = 1        # True
milk_present = "Atish"  # True
milk_present = None     #False
print(f"Is there milk? {bool(milk_present)}")
print(f"-------------------------\n")


water_hot = True
tea_added = False
can_serve1 = water_hot and tea_added
can_serve2 = water_hot or tea_added
print(f"Can we serve {can_serve1}")
print(f"Can we serve {can_serve2}")
print(f"-------------------------\n")



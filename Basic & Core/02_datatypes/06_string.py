chai_type = "Ginger chai"
customer_name = "Atish"
print(f"Oder for {customer_name} : {chai_type} please !")

# 0:8 is length it will start from 0 and end will be on 8th character
# :8  is length it will start from 0 and end will be on 8th character
# 0:8:2 means 0 to 8 length and every second character

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"First word: {chai_description[:8]}")
print(f"Every second word: {chai_description[0:8:2]}")

# 12:   means It will start from 12th letter and end with last letter
print(f"last word: {chai_description[12:]}")

# Start :(colon) End :(colon) step 
# Reverse the string.
print(f"First word: {chai_description[::-1]}")

lable_text = "chai spécial"
encoded_label = lable_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
print(f"Non Encoded Label: {lable_text}")
print(f"Encoded Label: {encoded_label}")
print(f"Decoded Label: {decoded_label}")
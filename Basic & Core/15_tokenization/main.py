import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Atish Pawar"
tokens = enc.encode(text)

print("Tokens", tokens)
# Tokens [25216, 3274, 0, 3673, 1308, 382, 3604, 1109, 69254, 277]

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 3604, 1109, 69254, 277])
print("Decoded", decoded)


# Me: "I'm in"
ciphertext_hex = "0c111d3e2b1731351c75173d7837171a79757938"
ciphertext = bytes.fromhex(ciphertext_hex)

# When you know the flag starts with "DTU{"
known_prefix = b"DTU{"

# Finding the key like:
possible_key = b""
for i in range(4):
    possible_key += bytes([ciphertext[i] ^ known_prefix[i]])

# Key: HEHE
# Me: HEHE indeed

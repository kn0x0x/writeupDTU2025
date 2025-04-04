def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

ciphertext_hex = "0c111d3e2b1731351c75173d7837171a79757938"
ciphertext = hex_to_bytes(ciphertext_hex)

known_prefix = b"DTU{"

possible_key = b""
for i in range(min(len(known_prefix), len(ciphertext))):
    possible_key += bytes([ciphertext[i] ^ known_prefix[i]])

print(f"Possible key prefix: {possible_key}")

key_candidate = possible_key

decoded = b""
for i in range(len(ciphertext)):
    decoded += bytes([ciphertext[i] ^ key_candidate[i % len(key_candidate)]])

print(f"Decoded with key {key_candidate}: {decoded}")

# XOR Cryptography Challenge 

## THE CHALLENGE
- **What they gave us**: `0c111d3e2b1731351c75173d7837171a79757938` 
- **Flag format**: `DTU{...something_here...}`
- **The secret sauce**: `xor101.py`

## NOW WE LOOKING AT THE CODE

```python
flag = "DTU{...[BI MAT KHONG TIET LO]...}"
key = "[BI MAT KHONG TIET LO]"
encoded = ""

for i in range(0, len(flag), 4):
    # This bad boy can fit so many XORs in it
    encoded += chr(ord(flag[i:i+1]) ^ ord(key[:1]))
    encoded += chr(ord(flag[i+1:i+2]) ^ ord(key[1:2]))
    encoded += chr(ord(flag[i+2:i+3]) ^ ord(key[2:3]))
    encoded += chr(ord(flag[i+3:i+4]) ^ ord(key[3:]))

print(encoded.encode("hex"))
```

## BRAIN MOMENT

Me realizing XOR is reversible: 
```
a ^ b = c
c ^ b = a
```

## PAYLOAD

```python
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
```

## THE REVELATION

When I ran the script:
```
Possible key prefix: b'HEHE'
Decoded with key b'HEHE': b'DTU{cRypT0_x0r__101}'
```

Me finding the key is "HEHE": Not sure if brilliant or just lucky

## FINAL FLAG

```
Key = "HEHE"
Flag = "DTU{cRypT0_x0r__101}"
```

## LESSONS LEARNED

- XOR crypto: exists

Remember kids, don't use simple XOR for anything important unless you want to be the next example in cybersecurity class :v


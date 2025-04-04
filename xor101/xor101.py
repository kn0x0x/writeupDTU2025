flag = "DTU{...[BI MAT KHONG TIET LO]...}"
key = "[BI MAT KHONG TIET LO]"
encoded = ""

for i in range(0, len(flag), 4):
    encoded += chr(ord(flag[i:i+1]) ^ ord(key[:1]))
    encoded += chr(ord(flag[i+1:i+2]) ^ ord(key[1:2]))
    encoded += chr(ord(flag[i+2:i+3]) ^ ord(key[2:3]))
    encoded += chr(ord(flag[i+3:i+4]) ^ ord(key[3:]))

print(encoded.encode("hex"))

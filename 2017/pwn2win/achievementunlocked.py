a =0xf2, 0x44, 0xc1, 0x7e, 0x2c, 0x9, 0x13, 0x18, 0xf1, 0xf1, 0x94, 0x5b, 0xe0, 0x9d, 0x57, 0x4c, 0x67, 0x96, 0x1d, 0x87, 0xe2, 0x27, 0x4e, 0xff, 0x21, 0x64, 0xd0, 0xd1, 0x8b, 0x4c, 
b = 0xD0, 0x71, 230, 50, 15, 58, 9, 46, 248, 161, 182, 82, 222, 205, 101, 114, 82, 159, 79, 185, 244, 114, 118, 193, 52, 53, 238, 247, 218, 80, 

print len(a)
print len(b)
print `bytearray([x^y^0x61 for x, y in zip(a, b)])`
def dec_num(x):
    bin_result = bin(int(x))
    oct_result = oct(int(x))
    hex_result = hex(int(x))
    return bin_result, oct_result, hex_result
def bin_num(x):
    dec_result = int(x,2)
    oct_result = oct(int(x,2))
    hex_result = hex(int(x,2))
    return dec_result, oct_result, hex_result
def oct_num(x):
    bin_result = bin(int(x,8))
    dec_result = int(x,8)
    hex_result = hex(int(x,8))
    return bin_result, dec_result, hex_result
def hex_num(x):
    bin_result = bin(int(x,16))
    oct_result = oct(int(x,16))
    dec_result = int(x,16)
    return bin_result, oct_result, dec_result

     

while True:
    n = input("number? ")
    if n.startswith("0b", 0, 2):
        d, o, h = bin_num(n)
        o = o.strip("0o")
        h = h.strip("0x")
        print(f"--------------------\nDecimal: {d}\nOctal: {o}\nHexadecimal: {h}\n--------------------")
    elif n.startswith("0o", 0, 2):
        b, d, h = oct_num(n)
        b = b.strip("0b")
        h = h.strip("0x")
        print(f"--------------------\nBinary: {b}\nDecimal: {d}\nHexadecimal: {h}\n--------------------")
    elif n.startswith("0x", 0, 2):
        b, o, d = hex_num(n)
        b = b.strip("0b")
        o = o.strip("0o")
        print(f"--------------------\nBinary: {b}\nOctal: {o}\nDecimal: {d}\n--------------------")
    elif n.isnumeric():
        b, o, h = dec_num(n)
        b = b.strip("0b")
        o = o.strip("0o")
        h = h.strip("0x")
        print(f"--------------------\nBinary: {b}\nOctal: {o}\nHexadecimal: {h}\n--------------------")
        #print(dec_num(int(n)))
    else: 
        print("Invalid number. Try again.")
    dasu = input("Another?(Y/n) ")
    if dasu == "n":
        break
def dec_num(x):
    bin_result = bin(x)
    oct_result = oct(x)
    hex_result = hex(x)
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
        print(bin_num(n))
    elif n.startswith("0o", 0, 2):
        print(oct_num(n))
    elif n.startswith("0x", 0, 2):
        print(hex_num(n))
    elif n.isnumeric():
        print(dec_num(int(n)))
    else: 
        print("Invalid number. Try again.")
    dasu = input("Another?(Y/n) ")
    if dasu == "n":
        break
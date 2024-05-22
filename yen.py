def main():
    x = int(input("How much Yen? "))
    print("Dollar algorithm:", dollar(x))
    print("Simple algorithm:", simp(x))
    print("Diff: ", dollar(x) - simp(x))
    print("The real value: ", real(x))
    print("Dollar algorithm bias: ", dollar(x)-real(x))
    print("Simple algorithm bias: ", simp(x)-real(x))

def dollar(n):
    return n*7 / 150

def simp(n):
    return n / 20

def real(n): # varies over time
    return n / 21.81

while True:
    if __name__ == "__main__":
        main()

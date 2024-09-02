import re

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
n = int(input())

for _ in range(n):
    barcode = input()

    if re.fullmatch(pattern, barcode):

        digits = ''.join(re.findall(r'\d', barcode))

        if digits:
            product_group = digits
        else:
            product_group = "00"

        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

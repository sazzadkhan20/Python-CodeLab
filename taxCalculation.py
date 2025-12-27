price = int(input("Enter a price of a Bike: "))
if price > 10000:
    print("Tax will be 15% of the bike\nand total tax will be: ",price*0.15)
elif price >= 5000 and price <= 9999:
    print("Tax will be 10% of the bike\nand total tax will be: ", price * 0.1)
elif price<5000 and price >= 0:
    print("Tax will be 5% of the bike\nand total tax will be: ",price*0.05)
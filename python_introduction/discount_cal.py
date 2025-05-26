purchase_amount = float(input("Enter your purchases amount: "))

if purchase_amount >= 1000:
    discount = 0.1 #10% discount on 1000 or more
elif purchase_amount >= 500 and purchase_amount < 1000:
    discount = 0.05 #5% discount on 500 to 999
else: 
    discount = 0

final_amount = purchase_amount * (1 - discount)
print("Your  final amount after discount: $" + str(final_amount))
moms = float(input("Please enter the price of your product: "))

VAT = 0.25 * moms
vat = moms - VAT 

print("The VAT amount is", VAT,"kr,")
print("The price without the VAT tax is",moms,"kr")
print("The price reduced with the VAT tax is", vat, "kr.")


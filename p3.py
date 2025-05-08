aa=float(input("How many pounds are you buying?:"))
price_per_pound=0.99
if aa <= 0:
    print ("Error:pounds must be more than zero. :(")
discount_rate=0
if aa >= 10 and aa < 100:
    discount_rate=0.1
elif aa >= 100 and aa < 1000:
    discount_rate=0.2
elif aa >= 1000 and aa < 10000:
    discount_rate=0.3
elif aa >= 10000:
    discount_rate=0.4
else:
    discount_rate=0

gross_sales = aa * 0.99
discount_amount=gross_sales*discount_rate
final_amount=gross_sales-discount_amount

print ("Number of pounds:",aa)
print ("Gross sales:",gross_sales)
print ("discount:",discount_amount)
print ("final amount:",final_amount)

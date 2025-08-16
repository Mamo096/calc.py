# Question 1
def calculate_discount(price,discount_percent):
    if  discount_percent >= 20:
        discount_amount = (discount_percent/100) * price
        original_price = price- discount_amount
        return original_price
    else:
        return price
    
 #  Question 2 
    price = float(input("Enter the original price of the item:"))
    discount_percent = float(input("Enter the discount percentage:"))
    final_price = calculate_discount(price,discount_percent)
    if discount_percent >= 20:
        print("final price after appying a discount is{final price:.2f}")
    else:
        print("original") 


    

